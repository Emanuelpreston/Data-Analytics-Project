# Data-Analytics-Project

# 🌍 Regional Air Quality Analytics and Predictive Modeling

An end-to-end data science and machine learning pipeline designed to investigate fine particulate matter ($PM_{2.5}$) behavior within high-density urban-industrial spaces. This project leverages advanced exploratory data analysis and optimized predictive architectures to map pollution risks and forecast air quality trends.

---

## 📌 Project Objectives
* **Investigate Air Quality Dynamics:** Analyze fine particulate matter ($PM_{2.5}$) levels within high-exposure spatial configurations.
* **Map Spatial Footprints:** Mathematically model the intersection of regional `Population_Density` and `Proximity_to_Industrial_Areas` to pinpoint systemic pollution vulnerabilities.


---

## 📁 Dataset & Source Citation
* **Data Source:** [Air Quality and Pollution Assessment (Kaggle)](https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment)
* **Dataset Profile:** 5,000 environmental observation instances containing key ambient markers ($PM_{10}$, $NO_2$, $SO_2$, $CO$, `Temperature`, `Humidity`) juxtaposed against geographic risk variables (`Population_Density`, `Proximity_to_Industrial_Areas`).
* **Main Data Asset:** `updated_pollution_dataset.csv`

---

## 🛠️ Data Engineering & Feature Design
To reveal hidden atmospheric dynamics, two engineering formulas are injected into the pipeline:

1. **PM Concentration Ratio:** Captures the structural balance of fine versus coarse particulate masses to trace fuel combustion signatures:
   $$PM\_Ratio = \frac{PM_{2.5}}{PM_{10}}$$

2. **Industrial Density Impact Index:** Tracks public danger metrics by weighting urban population centers against physical proximity to factories:
   $$Industrial\_Density\_Impact = \frac{Population\_Density}{Proximity\_to\_Industrial\_Areas}$$

---

## 🤖 Model Evaluation Matrix
Two analytical models were trained over an 80/20 train-test split. Performance was evaluated using Root Mean Squared Error (RMSE) and the Coefficient of Determination ($R^2$):

THE MODELS:

1. Linear Regression
Linear Regression is a baseline statistical model that models the relationship between a dependent scalar variable (target) and one or more explanatory variables (features) by fitting a linear equation (a straight line) to the observed data. It assumes a constant, proportional change between inputs and outputs.

2. Random Forest Regressor
Random Forest Regressor is an advanced ensemble learning method that operates by constructing a multitude of independent decision trees during training. It maps complex, non-linear relationships by forcing separate data splits across various features and aggregates (averages) the individual tree outputs to generate a single, highly accurate final numerical prediction.

| Predictive Model Configuration | $R^2$ Score (Accuracy) | Root Mean Squared Error (RMSE) |
| :--- | :---: | :---: |
| **Linear Regression Baseline** | 0.9539 | 4.1021 |
| **Optimized Random Forest** | **0.9905** | **2.1532** |


* **Statistical Inference:** While the Linear Regression model sets a strong baseline, the Random Forest Regressor drastically reduces average prediction errors down to an RMSE of **2.1532** and accounts for **99.05%** of target variance. This proves that micro-regional atmospheric pollution is controlled by non-linear interactions that linear models fail to completely articulate.

---
IMPORTANT

## 🚀 Environment Setup & Execution Instructions

### Prerequisites
Ensure your local environment has Python 3.10+ installed along with the required libraries. 

### 1. Install Dependencies
Install the required analytical and modeling libraries using pip:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn notebook
