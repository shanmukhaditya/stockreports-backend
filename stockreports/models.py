from django.db import models
import yfinance as yf
from datetime import datetime
import time
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import SimpleRNN
# from keras.layers import Dropout


# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=120)
    ticker = models.CharField(max_length=120)
    dashboardId = models.IntegerField(default=1)
    dashboardName = models.CharField(max_length=120, default='main')

    def _str_(self):
        return self.name
    
    def suggest(self):
        return True
    
    def get_openPrice(self):
        ticker = yf.Ticker(self.ticker)
        data = ticker.history(period='1d')
        # Return the open price if available, otherwise return None
        return round(data['Open'].iloc[0], 2) if not data.empty else None
    def get_closePrice(self):
        ticker = yf.Ticker(self.ticker)
        data = ticker.history(period='1d')
        # Return the open price if available, otherwise return None
        return round(data['Close'].iloc[0], 2) if not data.empty else None
        X_input = df.iloc[-time_step:].Open.values               # getting last 50 rows and converting to array
        X_input = scaler.fit_transform(X_input.reshape(-1,1))      # converting to 2D array and scaling
        X_input = np.reshape(X_input, (1,50,1))                    # reshaping : converting to 3D array
        print("Shape of X_input :", X_input.shape)
        LSTM_prediction = scaler.inverse_transform(model_lstm.predict(X_input))
        return LSTM_prediction[0,0] if LSTM_prediction else str(round(float(self.get_openPrice()) + 2, 2))

number = 1233
companies = {
    'AAPL':'Apple',
    'GOOGL':'Alphabet Inc.',
    'META':'Meta Platforms Inc.',
    'BIDU':'Baidu Inc.',
    'SPOT':'Spotify',
    'DASH':'DoorDash',
    'PINS':'Pinterest Inc.',
    'SNAP':'Snap Inc.',
    'TME':'Tencent Music Entertainment',
    'Z':'Zillow Group Inc.',
    'TWLO':'Twilio Inc.',
    'MTCH':'Match Group Inc.',
    'YELP':'Yelp Inc.'
}

