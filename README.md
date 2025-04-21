# 🩺 Building an Intelligent Clinical Decision Support System for Predicting Hospital Readmission
## 🔍 Project Context
Hospital readmissions remain a significant challenge in healthcare systems. Unplanned readmissions not only escalate costs but often reflect gaps in care delivery. To address this, I designed a Clinical Decision Support System (CDSS) that predicts the likelihood of patient readmission using demographic and clinical data — helping care teams to act earlier and smarter.

## 🧩 Approach and Tools Used
From the outset, I combined data science and business intelligence techniques to deliver both predictive power and intuitive visualization. Here's how the development unfolded:

1. Data Exploration and Business Intelligence
Using Power BI, I started with a thorough exploratory data analysis (EDA) of the dataset from Kaggle’s Diabetes 130-US Hospitals. The visual dashboard helped reveal crucial insights:

Patients with more inpatient visits, longer hospital stays, and frequent outpatient records were more likely to be readmitted.

Elderly diabetic patients were particularly vulnerable.

Some categorical variables (e.g., race, gender, age group) showed strong class distribution skews — something to keep in mind during modeling.

These insights guided my feature selection and model design.

2. Predictive Modeling with Python
To bring predictive intelligence to life, I developed a classification model using:

Python & Scikit-learn

Random Forest Classifier as the primary algorithm

Label encoding for categorical features

Persistent storage of encoders and models using Joblib and Pickle (.pkl) files

Key features included:
age, race, gender, time_in_hospital, number_inpatient, number_outpatient, diabetesMed, and change.

✅ Highlight: I ensured feature order and structure consistency during both training and inference using a saved feature_columns.pkl file — a key step in avoiding shape mismatches during prediction.

3. Streamlit Dashboard Development
Next, I developed a user-facing web app using Streamlit, allowing users to input patient details and instantly see a "High" or "Low" possibility of readmission.

What makes this interface unique:

Interactive UI elements: sliders, radio buttons, select boxes for seamless input.

Encoders loaded via .pkl: ensuring that what the user sees matches what the model expects.

Bar chart display: A visual breakdown of readmission likelihood to make the result easy to interpret.

## 🧠 Key Debugging Moment: I initially faced issues with LabelEncoder not recognizing inputs due to missing .fit() state. This was resolved by properly saving and loading encoders after training, not just using fit_transform in the script.

💡 Visual Insights + Prediction: A Unified Experience
The Power BI report offers an interactive way to explore patterns and distribution in the data — age groups, length of stay, and diabetic status are visually linked to readmission rates.

Meanwhile, the Streamlit model dashboard provides individual predictions, making it an actionable tool at the point of decision-making.

## ⚙️ Challenges & Solutions

Challenge	Solution
LabelEncoder not fitted error	Saved encoders post-fit, loaded them properly during prediction
Streamlit input mismatches	Used .reindex() and a stored feature order list to match model input
Data leakage concerns	Dropped diag_1, diag_2, and diag_3 which could bias predictions
UI Integration of ML logic	Used .pkl encoders to match user input to model expectations accurately
## 🚀 Outcome
The system combines real-time prediction with rich visual insights — supporting healthcare professionals in:

Early identification of high-risk patients

Tailored discharge planning

Data-driven decisions that reduce readmission costs and improve care quality

This end-to-end project showcases the synergy of machine learning, Python deployment, and BI tools in solving real-world healthcare problems.
 
