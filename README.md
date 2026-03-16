🚗 Car Insurance Claim Prediction

A machine learning project that predicts whether a policyholder is likely to file a car insurance claim in the next policy period based on vehicle, policy, and demographic features.

The project demonstrates a complete machine learning workflow, including data exploration, preprocessing, model development, and deployment using Streamlit.

📌 Project Objective

Insurance companies need to estimate the likelihood of claims to:

Reduce financial risk

Detect potential fraud

Optimize insurance premiums

Improve operational efficiency in claims processing

This project builds a predictive model that estimates the probability of a customer filing an insurance claim.

🗂 Project Structure
car-insurance-claim-prediction
│
├── data
│   └── raw
│       ├── train.csv
│       ├── test.csv
│       └── sample_submission.csv
│
├── notebooks
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   └── 03_preprocessing.ipynb
│
├── models
│   └── trained models
│
├── outputs
│   └── visualization results
│
├── pages
│   └── Streamlit UI pages
│
├── Main.py
├── requirements.txt
└── README.md
📊 Dataset

The dataset contains policyholder, vehicle, and insurance policy information.

Target Variable : 
is_claim

Binary classification:

0 → No claim
1 → Claim filed

Example features include:
Policy tenure

Age of car

Age of policyholder

Fuel type

Engine specifications

Safety features

Vehicle segment

NCAP safety rating

🔎 Exploratory Data Analysis

The EDA notebook analyzes:

Class distribution of insurance claims

Feature distributions

Potential correlations between features

Dataset structure and missing values

Example analysis includes visualization of claim distribution using Seaborn countplots.

🧹 Data Preprocessing

Data preprocessing steps include:

Feature grouping

Handling categorical variables

Preparing dataset for model training

Feature selection

The dataset is transformed into a format suitable for machine learning models.

🤖 Machine Learning Model

The project uses:

RandomForestClassifier

Tree-based models are well suited for structured insurance datasets because they handle:

Non-linear relationships

Mixed feature types

Feature interactions

📈 Model Evaluation

Model performance is evaluated using common classification metrics:

Accuracy

Precision

Recall

F1 Score

ROC-AUC

These metrics help assess how well the model identifies potential insurance claims.

🌐 Deployment

A Streamlit application is included to allow users to input policy and vehicle details and obtain claim predictions.

Run the app with:

streamlit run Main.py

The application launches locally in the browser.

🛠 Tech Stack

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Random Forest
Streamlit

🚀 Future Improvements

Potential improvements include:

Hyperparameter tuning

Feature importance analysis

Handling class imbalance

Trying additional models such as XGBoost

Cloud deployment

👨‍💻 Author

Ajey Jha

Data Analytics | Machine Learning | Python
