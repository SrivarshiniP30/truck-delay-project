import pandas as pd
import pickle 
from sklearn.metrics import accuracy_score 

with open('best_model.pkl', 'rb') as file: 
    model = pickle.load(file)
    
X_test=pd.read_csv('X_test.csv') # Load the dataset
y_test=pd.read_csv('y_test.csv')

predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")