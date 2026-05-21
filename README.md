# Adult Income Prediction System

## Project Overview

The Adult Income Prediction System is a Machine Learning project that predicts whether a person's yearly income is:

- <=50K
- >50K

The project uses multiple Machine Learning classification algorithms along with complete preprocessing pipelines.  
A Streamlit web application and FastAPI backend API are also included for user interaction and deployment purposes.

---

## Features

- Data Cleaning and Preprocessing
- Missing Value Handling
- One Hot Encoding
- Feature Scaling
- Multiple Machine Learning Models
- Model Comparison
- Prediction System
- Streamlit Frontend
- FastAPI Backend API
- Pipeline-Based Workflow
- Real-Time Prediction

---

## Machine Learning Models Used

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Support Vector Classifier (SVC)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- FastAPI
- Joblib

---

## Dataset

The project uses the Adult Income Dataset for predicting income categories based on demographic and work-related features.

### Input Features

- Age
- Workclass
- Education
- Educational Number
- Marital Status
- Occupation
- Relationship
- Race
- Gender
- Capital Gain
- Capital Loss
- Hours Per Week

### Target Variable

- <=50K
- >50K

---

## Project Structure

```bash
Adult-Income-Prediction/
│
├── app.py                 # Streamlit Application
├── api.py                 # FastAPI Backend
├── model.pkl              # Trained Machine Learning Model
├── requirements.txt       # Required Libraries
├── README.md              # Project Documentation
└── notebook.ipynb         # Model Training Notebook
```

---

## Data Preprocessing

The following preprocessing techniques were used:

- Missing Value Imputation
- One Hot Encoding for categorical columns
- Standard Scaling for numerical columns
- ColumnTransformer
- Pipeline Integration

---

## Model Training

The dataset was split into training and testing sets using:

```python
train_test_split(test_size=0.30, random_state=42)
```

Multiple classification models were trained and evaluated using:

- Accuracy Score
- Classification Report
- Precision
- Recall
- F1-Score

---

## Model Accuracy

| Model | Accuracy |
|---|---|
| Logistic Regression | 84% |
| KNN | 84% |
| Decision Tree | 84% |
| SVC | 85% |

---

## Run Streamlit Application

```bash
streamlit run app.py
```

---

## Run FastAPI Server

```bash
uvicorn api:app --reload
```

---

## API Endpoint

### Predict Income

```bash
POST /predict
```

Example Response:

```json
{
    "prediction": ">50K"
}
```

---

## Future Improvements

- Add Random Forest and XGBoost
- Hyperparameter Tuning
- Deploy on Cloud
- Improve User Interface
- Add Authentication System
- Store Predictions in Database

---

## Conclusion

This project demonstrates an end-to-end Machine Learning workflow including:

- Data preprocessing
- Model training
- Model evaluation
- Web application development
- API integration
- Machine Learning deployment basics

The project is suitable for beginners and intermediate learners interested in Machine Learning and deployment.

---

## Author

Minhal Ali Meer

BSCS Student | Machine Learning Learner