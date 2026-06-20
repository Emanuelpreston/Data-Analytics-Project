import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Dynamic Data Visualizer", layout="wide")
st.title("🌍 Fully Dynamic Environmental Chart Explorer")
st.markdown("Upload any dataset, select your columns, choose your chart type, and use the sliders to interact with your data in real-time.")

META_URL = "http://data-backend:8000/get_meta"
DATA_URL = "http://data-backend:8000/get_data"
UPLOAD_URL = "http://data-backend:8000/upload_new_csv"

# 🗂️ 1. File Upload Section in Sidebar
st.sidebar.header("📁 Step 1: Data Management")
uploaded_file = st.sidebar.file_uploader("Upload a completely new CSV dataset:", type=["csv"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
    res = requests.post(UPLOAD_URL, files=files)
    if res.json().get("status") == "success":
        st.sidebar.success(f"Backend updated with: {uploaded_file.name}")

# 🎛️ 2. Fetch Metadata and Dataset Rows
try:
    meta_response = requests.get(META_URL).json()
    data_response = requests.get(DATA_URL).json()
    df = pd.DataFrame(data_response)
    
    # 🎛️ 3. Dynamic Sliders
    st.sidebar.header("🎛️ Step 2: Dynamic Threshold Controls")
    st.sidebar.markdown("*Use sliders to filter data rows below a maximum value threshold:*")
    
    filtered_df = df.copy()
    
    # Loop through columns to build sliders. Moving them will actively filter the rows in the dataset!
    for column_name, stats in meta_response.items():
        user_val = st.sidebar.slider(
            label=f"Max threshold for {column_name}",
            min_value=stats["min"],
            max_value=stats["max"],
            value=stats["max"]  # Default to max so it shows all data initially
        )
        # Filter the dataset dynamically based on your slider position
        filtered_df = filtered_df[filtered_df[column_name] <= user_val]

    # 📊 4. Interactive Chart Configuration Controls
    st.subheader("📊 Chart Customization Studio")
    
    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    
    all_columns = list(df.columns)
    numeric_columns = list(meta_response.keys())
    
    with col_ctrl1:
        chart_type = st.selectbox("🗺️ Choose Chart Type:", ["Line Chart", "Bar Chart", "Area Chart"])
        
    with col_ctrl2:
        # Choose what goes on the horizontal X-Axis (e.g., Date, City, or index)
        default_x = all_columns[0] if all_columns else None
        x_axis = st.selectbox("📏 Select X-Axis (Horizontal):", all_columns, index=0)
        
    with col_ctrl3:
        # Choose which pollution metric values to plot on the vertical Y-Axis
        y_axis = st.multiselect("📈 Select Y-Axis metrics (Vertical):", numeric_columns, default=numeric_columns[:2])

    # 📉 5. Render Selected Chart Automatically
    st.markdown("---")
    if len(filtered_df) == 0:
        st.warning("⚠️ No data matches your slider settings. Drag your sliders to higher values to see the data points.")
    elif not y_axis:
        st.info("💡 Please select at least one Y-Axis metric from the dropdown list above to render the chart.")
    else:
        st.markdown(f"### Live {chart_type}: Displaying {len(filtered_df)} Rows Matching Your Controls")
        
        # Switch between the charts seamlessly based on dropdown selection
        if chart_type == "Line Chart":
            st.line_chart(data=filtered_df, x=x_axis, y=y_axis, use_container_width=True)
        elif chart_type == "Bar Chart":
            st.bar_chart(data=filtered_df, x=x_axis, y=y_axis, use_container_width=True)
        elif chart_type == "Area Chart":
            st.area_chart(data=filtered_df, x=x_axis, y=y_axis, use_container_width=True)

    # 📋 6. Dataset Table Records
    st.markdown("---")
    st.markdown("#### 📋 Active Dataset Records Preview")
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"Waiting for network link to backend container... Error details: {e}")