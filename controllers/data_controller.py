import os
import logging
import pandas as pd
from data import DATA_BASE_DIR

logging.basicConfig(format='%(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class DataController(object):
    def __init__(self):
        self.data_filename = os.path.join(DATA_BASE_DIR, 'data.csv')
        LOGGER.info('Data file: ' + self.data_filename.split('/')[-1] + ' is loaded')

    def get_dataframes(self):
        df = pd.read_csv(self.data_filename, parse_dates=['Time'])
        df.index = df.Time
        df = df.drop(['Time'], axis=1)
        df_differenced = df.diff().dropna()
        return df, df_differenced
