import mlflow1
import sklearn

from sklearn.metrics import accuracy_score

# Start an MLflow run
with mlflow1.start_run(run_name="Random Forest"):
    # Log model parameters
    mlflow1.log_param("n_estimators", 500)
    mlflow1.log_param("max_depth", 100)
    mlflow1.log_param("min_samples_split", 2)
    mlflow1.log_param("min_samples_leaf", 1)
    mlflow1.log_param("max_features", "sqrt")
    mlflow1.log_param("bootstrap", True)
    
    # Train and predict
    best_rf.fit(X_train, y_train)
    y_pred_rf = best_rf.predict(X_test)
    
    # Log metrics
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    mlflow1.log_metric("accuracy", accuracy_rf)