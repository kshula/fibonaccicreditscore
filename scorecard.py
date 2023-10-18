# Define a function to calculate the demographic score
def calculate_demographic_score(age_input, marital_status_input, enterprise_input, num_accounts_input, occupation_input, home_ownership_input, insurance_services_input, savings_methods_input):
    # ... (rest of the code for demographic scoring)
    age_scores = {
        '0-18': 19.795833,
        '18-24': 39.591666,
        '25-40': 59.387499,
        '41-56': 79.18332,
        '57-75': 98.979168,
        '76+': 118.7755
    }

    marital_status_scores = {
        'single': 11.22,
        'married': 17
    }

    enterprise_scores = {
        'no': 7.992,
        'yes': 12
    }

    num_accounts_scores = {
        '0': 18.37875,
        '1': 36.7575,
        '2': 55.13625,
        '3+': 73.515
    }

    occupation_scores = {
        'no job': 0,
        'primary': 15.08,
        'secondary': 30.16,
        'tertiary': 45.24
    }

    home_ownership_scores = {
        'no': 49.00995,
        'yes': 73.515
    }

    insurance_services_scores = {
        'no': 30.159996,
        'yes': 45.24
    }

    savings_methods_scores = {
        'no': 30.159996,
        'yes': 45.24
    }

    # Ask demographic questions and calculate scores
    age = age_scores.get(age_input, 0.0)
    marital_status = float(marital_status_scores.get(marital_status_input, 0.0))
    enterprise = float(enterprise_scores.get(enterprise_input, 0.0))  
    num_accounts = num_accounts_scores.get(num_accounts_input, 0.0)
    occupation = float(occupation_scores.get(occupation_input, 0.0))
    home_ownership = home_ownership_scores.get(home_ownership_input, 0.0)
    insurance_services = insurance_services_scores.get(insurance_services_input, 0.0)
    savings_methods = savings_methods_scores.get(savings_methods_input, 0.0)

    # Calculate the overall demographic score
    demographic_score = (
        age +
        marital_status +
        enterprise +
        num_accounts +
        occupation +
        home_ownership +
        insurance_services +
        savings_methods
    )

    return demographic_score

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
