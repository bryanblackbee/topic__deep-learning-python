import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.backend import clear_session
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Flatten, Dense, SimpleRNN, LSTM, GRU)

def ingest():
    # Read from CSV, keep only values
    df = pd.read_csv('jena_climate_2009_2016.csv')
    df = df.iloc[:,1:]
    df_values = df.values
    # Normalisation
    df_mean = df_values[:200000].mean(axis=0)
    df_std = df_values[:200000].std(axis=0)
    df_values-=df_mean
    df_values/=df_std
    return df_values

# Generator
def generator(data, lookback=0, delay=0, min_index=0, 
  max_index=None, shuffle=False,
  batch_size=128, step=6):
    if max_index == None:
        max_index = len(data) - delay - 1
    i = min_index + lookback
    
    while 1:
        if shuffle:
            rows = np.random.randint(
            min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback
            rows = np.arange(i, min(i + batch_size, max_index))
            i+= len(rows)
        
        samples = np.zeros((len(rows),
                           lookback // step,
                           data.shape[-1]))
        targets = np.zeros((len(rows,)))
        for j, row in enumerate(rows):
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]
            targets[j] = data[rows[j] + delay][1]
        yield samples, targets

df_values = ingest()

LOOKBACK, STEP, DELAY, BATCH_SIZE = 1440, 6, 144, 128
train_min_i, train_max_i = 0, 200000
val_min_i, val_max_i = 200001, 300000
test_min_i, test_max_i = 300001, None
val_steps = (val_max_i - val_min_i - LOOKBACK)
test_steps = (len(df_values) - test_min_i - LOOKBACK)
train_gen = generator(df_values, 
                      lookback=LOOKBACK, delay=DELAY, 
                      min_index=train_min_i, max_index=train_max_i, 
                      batch_size=BATCH_SIZE, step=STEP,shuffle=True)
val_gen = generator(df_values, 
                    lookback=LOOKBACK, delay=DELAY, 
                    min_index=val_min_i, max_index=val_max_i, 
                    batch_size=BATCH_SIZE, step=STEP,shuffle=False)
test_gen = generator(df_values, 
                     lookback=LOOKBACK, delay=DELAY, 
                     min_index=test_min_i, max_index=test_max_i, 
                     batch_size=BATCH_SIZE, step=STEP,shuffle=False)        

# Instantiate Model
###################
clear_session()
model4 = Sequential()
model4.add(GRU(32, dropout=0.1, recurrent_dropout=0.5, 
               input_shape=(None, df_values.shape[-1])))
model4.add(GRU(64, dropout=0.1, recurrent_dropout=0.5, 
               activation='relu'))
model4.add(Dense(1))
model4.compile(optimizer=RMSprop(), loss='mae',)
print(model4.summary())

# Train
#######
history4 = model4.fit(train_gen, 
  steps_per_epoch=500, 
  epochs=40, 
  validation_data=val_gen, 
  validation_steps=val_steps)
metrics_df = pd.DataFrame(history4.history)
metrics_df.to_csv('history4.csv', index=False)

# Save
######
model4.save('weather__v4__stacked_rnn_with_dropout.h5')
