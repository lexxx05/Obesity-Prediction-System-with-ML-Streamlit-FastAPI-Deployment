# WeightWise: Obesity Risk Prediction Pipeline

## Project Overview
This project aims to develop an **end-to-end machine learning pipeline** to predict obesity risk levels based on personal, lifestyle, and dietary factors. The workflow covers all major stages of a data science lifecycle — starting from **Exploratory Data Analysis (EDA)**, through **data preprocessing and model training**, to **deployment via FastAPI and Streamlit**.

---

## Objectives
- Analyze the dataset to understand relationships between lifestyle habits and obesity risk.
- Preprocess and transform raw data for model readiness.
- Train and evaluate machine learning models for obesity classification.
- Build and deploy a REST API using **FastAPI**.
- Develop a simple, interactive **Streamlit frontend** for public use.

---

## 1. Exploratory Data Analysis (EDA)
**File:** `SourceCode.ipynb`  
- Analyzed customer/lifestyle datasets to identify key behavioral and numerical patterns.  
- Verified data completeness (no missing values found).  
- Detected and visualized outliers in numerical columns.  
- Conducted correlation and distribution analysis to understand potential feature relationships.  
- Summary statistics indicated several relevant predictors for obesity estimation.

---

## 2. Data Preprocessing & Modelling
**File:** `Preprocess_and_Modelling_Pipeline_Code.ipynb`  
- Implemented robust preprocessing steps including:
  - Missing value imputation  
  - Encoding categorical variables using **LabelEncoder** and **OneHotEncoder**  
  - Feature scaling with **StandardScaler**  
  - Custom transformation on age column using `CleanAgeTransformer`  
- Built multiple classification models and compared performances:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
- Performed **hyperparameter tuning** and model evaluation using **ROC-AUC**, **accuracy**, and **F1-score** metrics.  
- The final optimized model (`best_pipeline_3.pkl`) was serialized for deployment.

---

## 3. Backend Development (FastAPI)
**Files:**  
- `FastAPI_Backend_SourceCode.ipynb`  
- `backend_script.py`  
- `custom_transformer_2.py`

### Backend Features
- Implemented a REST API using **FastAPI**.  
- Loaded the trained model (`best_pipeline_3.pkl`).  
- Defined a **Pydantic model** for input validation and structured prediction requests.  
- Created API endpoints:
  - `GET /api-endpoint` → Health check endpoint  
  - `POST /predict` → Returns obesity level prediction  

### Prediction Labels
| Code | Category |
|------|-----------|
| 0 | Insufficient Weight |
| 1 | Normal Weight |
| 2 | Overweight Level I |
| 3 | Overweight Level II |
| 4 | Obesity Type I |
| 5 | Obesity Type II |
| 6 | Obesity Type III |

---

## 4. Frontend Development (Streamlit)
**Files:**  
- `Streamlit_Frontend_SourceCode.ipynb`  
- `frontend_script.py`

### Frontend Features
- Simple and clean web interface using **Streamlit**.  
- Allows users to input:
  - Demographic info (Gender, Age, Height, Weight)
  - Lifestyle factors (Physical Activity, Food Habits, Alcohol, Smoking)
  - Behavioral indicators (Smartphone use, Snacking frequency, etc.)
- Sends data via REST API to the backend endpoint `/predict`.  
- Displays the predicted obesity category directly in the app interface.

---

## 6. Deployment Workflow
1. **Train & Export Model:**  
   - Run preprocessing and modelling notebook → save model as `best_pipeline_3.pkl`.

2. **Run Backend API (FastAPI):**
   - `uvicorn backend_script:app --reload`
   - The API runs locally on http://127.0.0.1:8000/.

3. **Run Frontend (Streamlit):**
   - `streamlit run frontend_script.py`
   - The frontend interacts with FastAPI and displays predictions in real time.

---

## 7. Conclusion
This project showcases a complete machine learning lifecycle — from EDA and preprocessing to model deployment.
It demonstrates how data-driven insights and ML models can be integrated into web-based applications, enabling real-time predictions for obesity risk assessment in a user-friendly format.
