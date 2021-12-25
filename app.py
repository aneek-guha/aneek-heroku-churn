from flask import Flask, render_template, request
from keras.models import load_model

load_mod = load_model('churn_modelling.h5')
app_flask = Flask(__name__)

@app_flask.route('/model')
def model():
    return render_template('model.html')

@app_flask.route('/predict', methods = ['POST'])
def predict():
    CreditScore = request.form.get('CreditScore')
    Age = request.form.get('Age')
    Tenure = request.form.get('Tenure')
    Balance = request.form.get('Balance')
    NumOfProducts = request.form.get('NumOfProducts')
    HasCrCard = request.form.get('HasCrCard')
    IsActiveMember = request.form.get('IsActiveMember')
    EstimatedSalary = request.form.get('EstimatedSalary')
    Germany = request.form.get('Germany')
    Spain = request.form.get('Spain')
    Male = request.form.get('Male')
    print(CreditScore, Age, Tenure, Balance,NumOfProducts,HasCrCard, IsActiveMember, EstimatedSalary, Germany,Spain,Male)

    predicted = load_mod.predict([[int(CreditScore), int(Age), int(Tenure), int(Balance),int(NumOfProducts),int(HasCrCard), int(IsActiveMember), int(EstimatedSalary), int(Germany),int(Spain),int(Male)]])
    
    if predicted[0]>=0.5:
        result= 'churn'
    if predicted[0]<0.5:
        result = 'not churn'
    
    return render_template('results.html', value=result)

if __name__ == '__main__':
    app_flask.run(debug=True)

