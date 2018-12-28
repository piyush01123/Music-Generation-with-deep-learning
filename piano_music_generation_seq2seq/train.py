
from __future__ import print_function
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import *
from keras.layers.normalization import *
from keras.callbacks import EarlyStopping, History, TensorBoard
from keras.layers import TimeDistributed
from keras.models import model_from_json
import time
from midi_io import get_data, createSeqNetInputs
from config import cfg
import sys
import os

DATA_DIR = 'data/'

#Global parameters
time_per_time_slice = cfg.CONST.TIME_PER_TIME_SLICE #0.02 #200ms #time-unit for each column in the piano roll
highest_note = cfg.CONST.HIGHEST_NOTE #81 # A_6
lowest_note = cfg.CONST.LOWEST_NOTE  #33 # A_2
input_dim = cfg.CONST.INPUT_DIM #highest_note - lowest_note + 1
output_dim = cfg.CONST.OUTPUT_DIM #highest_note - lowest_note + 1
MICROSECONDS_PER_MINUTE = cfg.CONST.MICROSECONDS_PER_MINUTE #60000000

#Model parameters
num_units = cfg.MODEL_PARAMS.NUM_UNITS #64
x_seq_length = cfg.MODEL_PARAMS.X_SEQ_LENGTH #50
y_seq_length = cfg.MODEL_PARAMS.Y_SEQ_LENGTH  #50
loss_function = cfg.MODEL_PARAMS.LOSS_FUNCTION #'categorical_crossentropy'
optimizer = cfg.MODEL_PARAMS.OPTIMIZER #Adam() #lr=0.0001
batch_size = cfg.MODEL_PARAMS.BATCH_SIZE #64
num_epochs = cfg.MODEL_PARAMS.NUM_EPOCHS #100


def createSeq2Seq():
	#seq2seq model

	#encoder
	model = Sequential()
	model.add(LSTM(input_dim = input_dim, output_dim = num_units, activation= 'tanh', return_sequences = True ))
	model.add(BatchNormalization())
	model.add(Dropout(0.3))
	model.add(LSTM(num_units, activation= 'tanh'))

	#decoder
	model.add(RepeatVector(y_seq_length))
	num_layers= 2
	for _ in range(num_layers):
		model.add(LSTM(num_units, activation= 'tanh', return_sequences = True))
		model.add(BatchNormalization())
		model.add(Dropout(0.3))

	model.add(TimeDistributed(Dense(output_dim, activation= 'softmax')))
	return model

tensorboard = TensorBoard(log_dir = "logs/{}".format(time.time()))

#Prepare data
dataset_folder = DATA_DIR
pianoroll_data = get_data(dataset_folder)
input_data, target_data = createSeqNetInputs(pianoroll_data, x_seq_length, y_seq_length)
input_data = input_data.astype(np.bool)
target_data = target_data.astype(np.bool)

#Model
model = createSeq2Seq()
print(model.summary())
model.compile(loss=loss_function, optimizer = optimizer)
earlystop = EarlyStopping(monitor='loss', patience= 10, min_delta = 0.01 , verbose=0, mode= 'auto')
history = History()
hist = model.fit(input_data, target_data, batch_size =  batch_size, nb_epoch=num_epochs,
callbacks=[ earlystop, history, tensorboard])
print("History:", hist.history )

model_file = 'SEQ2SEQ_architecture.json'
model_path = '%s/%s' %(cfg.DATA.MODEL_DIR, model_file)
open(model_path, 'w').write(model.to_json())

weights_file = 'SEQ2SEQ_weights.h5'
weights_path = '%s/%s' %(cfg.DATA.MODEL_DIR, weights_file)
model.save_weights(weights_path)

model_file = 'SEQ2SEQ_full_model.h5'
model_path = '%s/%s' %(cfg.DATA.MODEL_DIR, model_file)
model.save(model_path)
