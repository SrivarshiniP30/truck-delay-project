# Truck Delay Classification and ETA Prediction

## 🚀 Project Overview: An End-to-End Machine Learning Solution

This project delivers a comprehensive, end-to-end machine learning pipeline engineered to accurately predict truck delays and estimate arrival times (ETA). It encapsulates the entire lifecycle of a real-world machine learning application, from raw data ingestion and meticulous preprocessing to advanced model deployment and continuous fine-tuning.

The core objective is to analyze multifaceted factors influencing truck delays—such as dynamic weather conditions, evolving traffic patterns, and nuanced driver behavior. By leveraging these insights, the solution builds robust predictive models that **optimize delivery schedules, minimize operational costs, and significantly enhance customer satisfaction** through proactive delay mitigation.

This project demonstrates a strong command of:

* **Data Engineering:** Expertise in data acquisition, cleaning, transformation, and feature engineering to prepare high-quality datasets.
* **Exploratory Data Analysis (EDA):** Proficient application of statistical and visualization techniques to uncover critical data insights and inform modeling strategies.
* **Machine Learning Model Development:** Skill in training, evaluating, and fine-tuning diverse algorithms (Logistic Regression, Random Forest, XGBoost) with a focus on performance, interpretability, and generalization.
* **MLOps Practices:** Practical implementation of MLflow for robust experiment tracking, model versioning, and managing the machine learning lifecycle for reproducibility and scalability.
* **Deployment Readiness:** Designing and structuring the project with an application layer, showcasing readiness for seamless integration into production environments.

## 🌟 Key Features

* **Full ML Lifecycle Implementation:** A complete, demonstrable machine learning workflow from raw data ingestion to a deployable model.
* **Comprehensive Data-Driven Insights:** Conducts in-depth analysis to identify key drivers of delay, informing robust feature selection and model interpretability.
* **Advanced Predictive Modeling:** Develops and rigorously evaluates various supervised learning algorithms, comparing their performance metrics.
* **MLOps Integration with MLflow:** Ensures experiment reproducibility, model versioning, and efficient management of the machine learning lifecycle.
* **Modular & Scalable Design:** Project structured with reusable components and pipelines, promoting maintainability and future expansion.
* **Robust Data Management:** Clear separation of raw and processed data, enhancing data governance and pipeline clarity.

## 🛠️ Technologies Used

* **Programming Languages:** Python
* **Machine Learning Libraries:** Scikit-learn, XGBoost
* **Data Manipulation:** Pandas, NumPy
* **Notebooks:** Jupyter Notebook
* **MLOps:** MLflow
* **Database (Mock/Example):** PostgreSQL (referenced in `truck-eta-postgres.sql`)

## 📁 Project Structure

    .
    ├── app/                          # Application code for deployment/serving the model
    │   ├── app.py                    # Main application entry point
    │   └── modelDeployed.py          # Script for loading and serving the deployed model
    ├── config/                       # Configuration files for the project
    │   └── config.ini
    ├── data/
    │   ├── raw/                      # Original, untouched raw data
    │   │   ├── city_weather.csv
    │   │   ├── drivers_table.csv
    │   │   ├── routes_table.csv
    │   │   ├── routes_weather.csv
    │   │   ├── traffic_table.csv
    │   │   ├── truck_schedule_table.csv
    │   │   └── trucks_table.csv
    │   │   └── truck-eta-postgres.sql
    │   └── processed/                # Cleaned, transformed, or feature-engineered data
    │       ├── cleanedDf.csv
    │       ├── combineddf.csv
    │       ├── final_data.csv        # Final processed data (LFS tracked)
    │       ├── final_data2.csv
    │       ├── X_test.csv
    │       └── y_test.csv
    ├── models/                       # Trained model artifacts and related metadata
    │   ├── best_model.pkl            # Best performing trained machine learning model (LFS tracked)
    │   └── best_params.json          # Best parameters found during hyperparameter tuning
    ├── mlruns/                 # MLflow experiment tracking data and artifacts
    ├── notebooks/                    # Jupyter notebooks for EDA, experimentation, and analysis
    │   ├── Data_Cleaning_Preprocessing.ipynb
    │   ├── Data_Collection_Ingestion.ipynb
    │   ├── EDA_Feature_Engineering.ipynb
    │   ├── EDA_Final.ipynb
    │   ├── EDA_Initial.ipynb
    │   ├── MLflow_Experiment_1.ipynb
    │   ├── MLflow_Experiment_2.ipynb
    │   ├── Model_Development_Exploration.ipynb
    │   ├── Model_Evaluation.ipynb
    │   ├── Model_Training_LogReg.ipynb
    │   ├── Model_Training_LogReg_2.ipynb
    │   ├── Model_Training_RandomForest.ipynb
    │   ├── Model_Training_RandomForest_2.ipynb
    │   ├── Model_Training_XGBoost.ipynb
    │   ├── Model_Training_XGBoost_2.ipynb
    │   └── old_notebooks/            # Older or redundant notebooks for reference
    │       ├── dataCleaning(WRONG).ipynb
    ├── src/                          # Reusable Python source code
    │   ├── components/               # Modular components for data processing, feature engineering, etc.
    │   │   ├── init.py
    │   │   ├── data_cleaning.py
    │   │   └── data_ingestion.py
    │   ├── pipelines/                # Scripts that orchestrate the data flow and ML steps
    │   │   ├── init.py
    │   │   ├── data_cleaning_pipeline.py
    │   │   └── data_ingestion_pipeline.py
    │   ├── models/                   # Python scripts for model definition, training, and prediction logic
    │   │   ├── init.py
    │   │   ├── model_training.py     # (Placeholder for combined model training logic)
    │   │   └── prediction.py         # (Placeholder for inference logic)
    │   └── utils/                    # Utility functions (e.g., for data loading, common helpers)
    │       ├── init.py
    │       ├── data_loader.py
    │       └── mlflow_utils.py       # (Placeholder for MLflow utility functions)
    ├── .gitattributes                # Git LFS tracking configuration
    ├── .gitignore                    # Files/folders to ignore from Git
    ├── README.md                     # Project overview
    ├── requirements.txt              # Python dependencies
    ├── setup.py                      # Project setup script
    ├── data.json                     # Configuration/data metadata
    ├── feature_names.json
    └── logRegMlFlow.py               # (Standalone MLflow script, consider integrating into notebooks/src)



## 🚀 Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SrivarshiniP30/truck-delay-project.git](https://github.com/SrivarshiniP30/truck-delay-project.git)
    cd truck-delay-project
    ```
2.  **Install Git LFS:**
    Ensure Git Large File Storage (LFS) is installed on your system to handle large data and model files.
    ```bash
    git lfs install
    ```
3.  **Pull LFS files:**
    ```bash
    git lfs pull
    ```
4.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure your `requirements.txt` is up-to-date with all project dependencies. If missing, you may need to manually install `pandas`, `numpy`, `scikit-learn`, `xgboost`, `mlflow`, `jupyter`.)*

## 📊 Usage

This project follows a structured data science workflow. Key stages are demonstrated through the Jupyter Notebooks and Python scripts:

* **Data Collection & Ingestion:** Refer to `notebooks/Data_Collection_Ingestion.ipynb` and `src/utils/data_loader.py`.

* **Data Cleaning & Preprocessing:** Explore `notebooks/Data_Cleaning_Preprocessing.ipynb` and `src/components/data_cleaning.py`.

* **EDA & Feature Engineering:** See `notebooks/EDA_Feature_Engineering.ipynb`, `notebooks/EDA_Initial.ipynb`, and `notebooks/EDA_Final.ipynb`.

* **Model Training & Evaluation:** Check notebooks like `notebooks/Model_Training_RandomForest.ipynb`, `notebooks/Model_Training_XGBoost.ipynb`, `notebooks/Model_Training_LogReg.ipynb` for different model approaches.

* **MLflow Tracking:** `notebooks/MLflow_Experiment_1.ipynb`, `notebooks/MLflow_Experiment_2.ipynb`, and `logRegMlFlow.py` (consider moving to `src/utils/mlflow_utils.py` or integrating into notebooks) demonstrate MLflow integration.

* **Model Deployment/Inference:** `app/app.py` and `app/modelDeployed.py` are used for serving the trained model.

To run the Jupyter Notebooks:
```bash
jupyter notebook



