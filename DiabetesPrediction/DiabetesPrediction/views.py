from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    file_path = r'C:\Users\ASUS\Downloads\Project 2 MeriSKILL\diabetes.csv'
    # Use 'r' before the string to indicate a raw string, avoiding issues with escape characters

    data = pd.read_csv(file_path)

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    # Retrieve input values from the form
    val1 = request.GET.get('n1', '')
    val2 = request.GET.get('n2', '')
    val3 = request.GET.get('n3', '')
    val4 = request.GET.get('n4', '')
    val5 = request.GET.get('n5', '')
    val6 = request.GET.get('n6', '')
    val7 = request.GET.get('n7', '')
    val8 = request.GET.get('n8', '')

    # Check if any of the values are empty strings
    if any(not val.strip() for val in [val1, val2, val3, val4, val5, val6, val7, val8]):
        # Handle the case where any input value is empty
        return render(request, 'predict.html', {'error_message': 'Please fill in all fields'})

    # Convert non-empty values to floats
    val1 = float(val1)
    val2 = float(val2)
    val3 = float(val3)
    val4 = float(val4)
    val5 = float(val5)
    val6 = float(val6)
    val7 = float(val7)
    val8 = float(val8)

    result1=""
    if pred == [1]:
        result1 = " Positive"
    else:
        result1 = " Negative"

    return render(request, 'predict.html', {'result2': result1})
