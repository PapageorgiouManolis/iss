## ISS's Location Forecasting
- In this project we are trying to predict International Space Station's future location.
We are using the Vector Autoregression (VAR) method. The procedure followed to produce our 
VAR model and evaluate it, it is displayed in the ISS jupyter notebook.
- We have built a simple python flask application through which we are using our trained VAR model
 to predict ISS's location on 10/09/2019 @ 12:10:00.


## Install Project
from the content root:

1. docker build -t iss_location -f Dockerfile .
2. docker run -d -p 5000:5000 iss_location

OR
* Python 3 is required
1. pip install -e .
1. pip install -r requirements.txt
2. python app.py

## Results
Go to http://localhost:5000/ in your browser to see the project's results.
