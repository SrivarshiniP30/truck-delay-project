# truck-delay-project
A project to analyze and predict truck delays.
Truck Delay Classification and ETA Prediction
This project focuses on building a machine learning model to predict truck delays and estimate arrival times (ETA). It involves a comprehensive data science workflow, from data collection and cleaning to feature engineering, model training, and evaluation. The solution leverages various machine learning algorithms and MLOps practices for robust model development and deployment.

🌟 Key Features
End-to-End ML Pipeline: Demonstrates a complete machine learning lifecycle, including data ingestion, cleaning, feature engineering, model training, and evaluation.

Data-Driven Insights: Analyzes various factors influencing truck delays, such as weather conditions, traffic patterns, driver behavior, and route characteristics.

Predictive Modeling: Implements and evaluates multiple machine learning algorithms (e.g., Logistic Regression, Random Forest, XGBoost) for delay classification and ETA prediction.

MLOps Integration: Utilizes MLflow for experiment tracking, model versioning, and potential deployment, ensuring reproducibility and efficient model management.

Data Preparation & Cleaning: Includes robust pipelines for handling missing values, outliers, and transforming raw data into a suitable format for modeling.

Exploratory Data Analysis (EDA): In-depth analysis to understand data distributions, correlations, and identify key features impacting truck delays.

🛠️ Technologies Used
Programming Languages: Python

Machine Learning Libraries: Scikit-learn, XGBoost

Data Manipulation: Pandas, NumPy

Notebooks: Jupyter Notebook

MLOps: MLflow

Database (Mock/Example): PostgreSQL (referenced in truck-eta-postgres.sql)

📁 Project Structure
TruckProject/
├── Truck_Delay_Classification/
│   ├── Data/
│   │   ├── Backup/
│   │   └── Training_Data/
│   ├── Notebooks/
│   ├── Pipelines/
│   ├── src/
│   │   └── components/
│   ├── .gitignore
│   ├── 1.Data_Preparation.md
│   ├── README.md
│   ├── requirements.txt
│   └── setup.py
├── mlruns/                 # MLflow experiment tracking data
├── app.py                   # Main application/inference script
├── best_model.pkl           # Trained machine learning model
├── best_params.json         # Best parameters for models
├── cleanedDf.csv            # Cleaned dataset
├── combineddf.csv           # Combined dataset
├── data.json                # Configuration/data metadata
├── dataCleaning(WRONG).ipynb # Example of iterative development/refinement
├── dataCleaningPreprocessing(STEP 3).ipynb
├── dataCollection(STEP 2).ipynb
├── deployed_Model_Eval2.ipynb
├── eda(FINAL STEP4).ipynb
├── eda(STEP 4).ipynb
├── feature_names.json
├── final_data.csv           # Final processed data (large file, handled by LFS)
├── final_data2.csv
├── loadData1(WRONG).py
├── loadData2(WRONG).py
├── loadData3(STEP 1).py
├── logRegMlFlow.py
├── mlflow1.py
├── mlflow2.py
├── modelDeployed.py
├── modelTrainingLogReg.ipynb
├── modelTrainingLogReg2.ipynb
├── modelTrainingRandomForest.ipynb
├── modelTrainingRandomForest2.ipynb
├── modelTrainingXG.ipynb
├── modelTrainingXG2.ipynb
├── models.ipynb
├── model_Data.csv           # Raw/intermediate data (large file, handled by LFS)
├── X_test.csv
└── y_test.csv

🚀 Setup and Installation
To set up and run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/SrivarshiniP30/truck-delay-project.git
cd truck-delay-project

Install Git LFS:
Ensure Git Large File Storage (LFS) is installed on your system to handle large data and model files.

git lfs install

Pull LFS files:

git lfs pull

Create a virtual environment (recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install dependencies:

pip install -r Truck_Delay_Classification/requirements.txt

(Note: If requirements.txt is missing or incomplete, you may need to manually install pandas, numpy, scikit-learn, xgboost, mlflow, jupyter.)

📊 Usage
The project workflow is primarily demonstrated through the Jupyter Notebooks located in the Truck_Delay_Classification/Notebooks/ directory.

Data Collection & Ingestion: Refer to dataCollection(STEP 2).ipynb and loadData3(STEP 1).py.

Data Cleaning & Preprocessing: Explore dataCleaningPreprocessing(STEP 3).ipynb.

EDA & Feature Engineering: See EDA&FeatureEng(STEP 4).ipynb and eda(FINAL STEP4).ipynb.

Model Training & Evaluation: Check modelTrainingRandomForest.ipynb, modelTrainingXG.ipynb, modelTrainingLogReg.ipynb for different model approaches.

MLflow Tracking: mlflow1.py and mlflow2.py demonstrate MLflow integration.

Model Deployment/Inference: modelDeployed.py and app.py are likely used for serving the model.

To run the Jupyter Notebooks:

jupyter notebook

This will open a browser window where you can navigate through the notebooks and execute the code cells.

📞 Contact
For any questions or further information, please feel free to reach out.
