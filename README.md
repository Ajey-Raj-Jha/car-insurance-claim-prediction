# 🚗 Car Insurance Claim Prediction

A machine learning project that predicts whether a policyholder will file a **car insurance claim in the next policy period** using demographic, vehicle, and policy-related features.

The project demonstrates a complete machine learning workflow including **data exploration, preprocessing, model training, and deployment using Streamlit**.

---

## 📌 Project Objective

Insurance companies need to estimate the likelihood of claims in order to:

- Reduce financial risk  
- Detect potential fraud  
- Optimize insurance premiums  
- Improve operational efficiency in claims processing  

This project builds a predictive model that estimates the probability of a customer filing an insurance claim.

---

## 📊 Dataset

The dataset contains information about **policyholders, vehicles, and insurance policies**.

### Target Variable

`is_claim`

Binary classification:

- **0 → No claim**
- **1 → Claim filed**

### Example Features

- Policy tenure  
- Age of car  
- Age of policyholder  
- Population density  
- Vehicle segment  
- Fuel type  
- Engine specifications  
- Safety features  
- NCAP safety rating  

---

## 🔎 Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and identify patterns.

### Analysis Includes

- Feature distribution analysis  
- Claim distribution visualization  
- Correlation analysis  
- Detection of class imbalance  

Visualizations were created using **Matplotlib and Seaborn**.

---

## 🧹 Data Preprocessing

### Steps Performed

- Handling categorical variables  
- Feature grouping and transformation  
- Preparing training features and labels  
- Structuring the dataset for machine learning models  

---

## 🤖 Machine Learning Model

### Model Used

- **Random Forest Classifier**

Tree-based models are effective for structured datasets because they handle:

- Non-linear relationships  
- Mixed feature types  
- Feature interactions  

---

## 📈 Model Evaluation

The model was evaluated using the following metrics:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

These metrics help measure how effectively the model predicts insurance claims.

---

## 🌐 Streamlit Application

A **Streamlit web application** allows users to input policyholder and vehicle details to generate claim predictions.

### Run the Application

```bash
streamlit run Main.py
```


# 👨‍💻 Author

## Ajey Raj Jha

Data Analytics | Machine Learning | Python
