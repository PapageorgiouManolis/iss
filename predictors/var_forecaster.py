import os
import logging
import pandas as pd
from models import MODELS_BASE_DIR
from statsmodels.iolib.smpickle import load_pickle

logging.basicConfig(format='%(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class VarForecaster(object):
    def __init__(self):
        self.model_filename = os.path.join(MODELS_BASE_DIR, 'final_var_model.pkl')
        self.model = load_pickle(self.model_filename)
        LOGGER.info('VAR Model: ' + self.model_filename.split('/')[-1] + ' is loaded')

    def predict(self, df, diff_df):
        # forecast_observations for next 2 days with 10minute frequency
        FORECAST_OBSERVATIONS = 287
        LAG_ORDER = 16
        final_forecast_input = diff_df.values[-LAG_ORDER:]
        final_fc = self.model.forecast(y=final_forecast_input, steps=FORECAST_OBSERVATIONS)
        LOGGER.info("Final Forecast's length: " + str(len(final_fc)))

        # Create new dataframe for the forecast to include the required date: 10/09/2019 @ 12:10:00.
        input_df = pd.DataFrame(
            {'Time': pd.date_range('2019-09-09', '2019-09-11', freq='10min', closed='left')}
        )
        input_df.index = input_df.Time
        input_df = input_df.drop(['Time'], axis=1)
        # Delete first row with datetime 2019-09-09 00:00:00 as it is the last row of our dataset
        input_df = input_df.iloc[1:]
        LOGGER.info("Input dataframe's length: " + str(len(input_df)))

        final_forecast_df = pd.DataFrame(final_fc, index=input_df.index, columns=df.columns + '_1d')
        final_results = invert_transformation(df, final_forecast_df)

        # We will keep the first 220 results
        final_results = final_results[:220]

        predicted_latitude = round(final_results.loc['2019-09-10 12:10:00'][2], 3)
        predicted_longitude = round(final_results.loc['2019-09-10 12:10:00'][3], 3)
        LOGGER.info('On 10/09/2019 @ 12:10:00 ISS will have: \n Latitude: ' + str(predicted_latitude) +
                    '\n Longitude: ' + str(predicted_longitude))
        return predicted_latitude, predicted_longitude


def invert_transformation(df_train, df_forecast):
    """Revert back the differencing to get the forecast to original scale."""
    df_fc = df_forecast.copy()
    df_tr = df_train.copy()
    columns = df_tr.columns
    for col in columns:
        df_fc[str(col)+'_forecast'] = df_tr[col].iloc[-1] + df_fc[str(col)+'_1d'].cumsum()
    return df_fc
