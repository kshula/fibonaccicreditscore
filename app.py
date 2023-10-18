from flask import Flask, render_template, request
from scorecard import calculate_demographic_score, calculate_behavioral_score


app = Flask(__name__)



# Define a function to calculate the behavioral score
def calculate_behavioral_score(impulse_1, impulse_2, impulse_3, time_1, time_2, time_3, risk_1, risk_2, risk_3, trust_1, trust_2, trust_3):
    # ... (rest of the code for behavioral scoring)
    impulse = (impulse_1 + impulse_2 + impulse_3) / 15
    time = (time_1 + time_2 + time_3) / 15
    risk = (risk_1 + risk_2 + risk_3) / 15
    trust = (trust_1 + trust_2 + trust_3) / 15   
    
    
    # Define the weightings for behavioral factors
    impulsivity_weight = 47.125
    time_preference_weight = 47.125
    risk_attitude_weight = 47.125
    trustworthiness_weight = 47.125

    # Calculate the overall behavioral score
    behavioral_score = (
        impulse * impulsivity_weight +
        time * time_preference_weight +
        risk * risk_attitude_weight +
        trust * trustworthiness_weight
    )

    return behavioral_score


# Define a route to handle the form submission
@app.route('/', methods=['GET', 'POST'])
def calculate_credit_score():
    if request.method == 'POST':
        # Get user input from the form
        age_input = request.form['age']
        marital_status_input = request.form['marital_status']
        enterprise_input = request.form['enterprise']
        num_accounts_input = request.form['num_accounts']
        occupation_input = request.form['occupation']
        home_ownership_input = request.form['home_ownership']
        insurance_services_input = request.form['insurance_services']
        savings_methods_input = request.form['savings_methods']

        impulse_1 = int(request.form['impulse_1'])
        impulse_2 = int(request.form['impulse_2'])
        impulse_3 = int(request.form['impulse_3'])
        time_1 = int(request.form['time_1'])
        time_2 = int(request.form['time_2'])
        time_3 = int(request.form['time_3'])
        risk_1 = int(request.form['risk_1'])
        risk_2 = int(request.form['risk_2'])
        risk_3 = int(request.form['risk_3'])
        trust_1 = int(request.form['trust_1'])
        trust_2 = int(request.form['trust_2'])
        trust_3 = int(request.form['trust_3'])

        # Calculate demographic and behavioral scores
        demographic_score = calculate_demographic_score(age_input, marital_status_input, enterprise_input, num_accounts_input, occupation_input, home_ownership_input, insurance_services_input, savings_methods_input)
        behavioral_score = calculate_behavioral_score(impulse_1, impulse_2, impulse_3, time_1, time_2, time_3, risk_1, risk_2, risk_3, trust_1, trust_2, trust_3)

        # ... (rest of the credit score calculation and grade assignment)
        # Define the weights for demographic and behavioral scores
        demographic_weight = 565.5
        behavioral_weight = 188.5

        # Calculate the credit score
        baseline_score = 233
        credit_score = baseline_score + ((demographic_score / demographic_weight) * demographic_weight) + ((behavioral_score / behavioral_weight) * behavioral_weight)

# Define the score ranges
        if 233 <= credit_score <=377:
            grade = 'very poor credit'
        elif 377 <=credit_score <= 534.6:
            grade = 'poor credit'
        elif 534.6 <= credit_score <= 685.4:
            grade = 'fair credit'
        elif 685.4 <= credit_score <= 836.2:
            grade - 'good credit'
        elif 836.2 <= credit_score:
            grade = 'excellent'
        else:
            grade = 'unclassified'
        

        return render_template('result.html', credit_score=credit_score, grade=grade)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
