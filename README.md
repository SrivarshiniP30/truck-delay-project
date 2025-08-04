# Truck Delay Classification and ETA Prediction

This project focuses on building a machine learning model to predict truck delays and estimate arrival times (ETA). It involves a comprehensive data science workflow, from data collection and cleaning to feature engineering, model training, and evaluation. The solution leverages various machine learning algorithms and MLOps practices for robust model development and deployment.

## 🌟 Key Features

* **End-to-End ML Pipeline:** Demonstrates a complete machine learning lifecycle, including data ingestion, cleaning, feature engineering, model training, and evaluation.
* **Data-Driven Insights:** Analyzes various factors influencing truck delays, such as weather conditions, traffic patterns, driver behavior, and route characteristics.
* **Predictive Modeling:** Implements and evaluates multiple machine learning algorithms (e.g., Logistic Regression, Random Forest, XGBoost) for delay classification and ETA prediction.
* **MLOps Integration:** Utilizes MLflow for experiment tracking, model versioning, and potential deployment, ensuring reproducibility and efficient model management.
* **Data Preparation & Cleaning:** Includes robust pipelines for handling missing values, outliers, and transforming raw data into a suitable format for modeling.
* **Exploratory Data Analysis (EDA):** In-depth analysis to understand data distributions, correlations, and identify key features impacting truck delays.

## 🛠️ Technologies Used

* **Programming Languages:** Python
* **Machine Learning Libraries:** Scikit-learn, XGBoost
* **Data Manipulation:** Pandas, NumPy
* **Notebooks:** Jupyter Notebook
* **MLOps:** MLflow
* **Database (Mock/Example):** PostgreSQL (referenced in `truck-eta-postgres.sql`)

## 📁 Project Structure
    .
    ├── src/
    │   ├── main.py
    │   ├── utils.py
    │   └── data/
    │       └── raw_data.csv
    ├── tests/
    │   └── test_main.py
    ├── README.md
    ├── requirements.txt
    └── LICENSE

## 📊 Usage

The project workflow is primarily demonstrated through the Jupyter Notebooks located in the `Truck_Delay_Classification/Notebooks/` directory.

* **Data Collection & Ingestion:** Refer to `dataCollection(STEP 2).ipynb` and `loadData3(STEP 1).py`.
* **Data Cleaning & Preprocessing:** Explore `dataCleaningPreprocessing(STEP 3).ipynb`.
* **EDA & Feature Engineering:** See `EDA&FeatureEng(STEP 4).ipynb` and `eda(FINAL STEP4).ipynb`.
* **Model Training & Evaluation:** Check `modelTrainingRandomForest.ipynb`, `modelTrainingXG.ipynb`, `modelTrainingLogReg.ipynb` for different model approaches.
* **MLflow Tracking:** `mlflow1.py` and `mlflow2.py` demonstrate MLflow integration.
* **Model Deployment/Inference:** `modelDeployed.py` and `app.py` are likely used for serving the model.

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SrivarshiniP30/truck-delay-project.git](https://github.com/SrivarshiniP30/truck-delay-project.git)
    cd truck-delay-project
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3.  **Run the data processing and training pipeline:**
    ```bash
    python src/pipelines/training_pipeline.py
    ```
4.  **Start the prediction web app:**
    ```bash
    python app/app.py
    ```
