# Fibonacci Credit score app

People in low-income communities do not have a credit or bank account because they have insufficient credit history for a credit score to be ascribed to them. Many in Zambia do however have mobile money accounts. A credit score is an important metric in access to credit.  Without alternative data, the type of data that is typically available is demographic data and psychometric variables.
This app Uses Python and Flask to create an a priori credit score app targeting unbanked and banked population. Uses criteria like age, marital status(single, married),enterprise(yes/no), number of accounts), occupation(primary/secondary and tertiary), home ownership(yes/no/rent), monthly income bracket,  access to insurance services (yes/no), savings (yes/no) methods (i.e mobile money, bank, cash, ). These will form a demographic score.
 It will include levels of debt (calculate as percentage of reported income) in future.
 It uses a analyze the user's responses to behavioral questions and calculate a score or rating based on chosen criteria. Assess measures of impulsivity, time preference, risk attitude, and trustworthiness as psychometric variables.
Uses Flask to collect user data, demographic and behavioral responses to show credit score.
Backend algorithm for credit score is based on  a weighted Fibonacci scale from 233 to 987. 
Looking to collaborate on a further front end.


## Authors

- [@kshula](https://github.com/kshula)


## Contributing

Contributions are always welcome!
Changes in the front end are very welcome. For major changes to backend algorithm kindly indicate what changes you would like to make.


## 🚀 About Me
Mathematician, ML Engineer, and Data Analyst with a passion for unlocking the potential of AI. 📊🤖 Let's explore the endless possibilities of data together. 🌟

## Installation
Use package manager to pip install flask

'''bash
pip install flask
'''

## Usage
'''python
from flask import Flask, render_template, request
from scorecard import calculate_demographic_score
from scorecard import calculate_behavioral_score
'''
## cOLLABORATIONS

👯‍♀️ I'm looking to collaborate on involving mathematics at the backend embedded in creative and new algorithms fit for purpose.


## Lessons Learned

Lessons learnt include end to end project from creating score logic and weigting to pychometric questioning to converting to flask for responses using some css and html.
Encountered some challenges on front end to make the score be shown in a gauge meter.


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Tech Stack

**Client:** Flask

**Server:** Python


## Support

For support, email kampambashula@gmail.com 

