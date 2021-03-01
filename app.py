from flask import Flask
from controllers.data_controller import DataController
from predictors.var_forecaster import VarForecaster

app = Flask(__name__)

data_controller = DataController()
var_forecaster = VarForecaster()

df, diff_df = data_controller.get_dataframes()
predicted_latitude, predicted_longitude = var_forecaster.predict(df, diff_df)


@app.route('/')
def predict_location():
    return 'On 10/09/2019 @ 12:10:00 ISS will have: Latitude: ' + str(predicted_latitude) + \
           ' and Longitude: ' + str(predicted_longitude)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
