import datetime
import shutil

now = datetime.datetime.now()

from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Convolution1D, Flatten, Dropout
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.callbacks import TensorBoard
import numpy as np
from embedding import to_embedded_tensor

INPUT_FILENAME = 'labeled_data.csv'
N_TESTDATA = 100
N_EPOCH = 24

x, y, words = to_embedded_tensor(INPUT_FILENAME)
x, y = np.array(x), np.array(y)
x_train = x[N_TESTDATA:]
y_train = y[N_TESTDATA:]
x_test = x[:N_TESTDATA]
y_test = y[:N_TESTDATA]

# Using embedding from Keras
embedding_vecor_length = 300
model = Sequential()
model.add(Embedding(words, embedding_vecor_length, input_length=x_train.shape[1]))

# Convolutional model (3x conv, flatten, 2x dense)
model.add(Convolution1D(64, 3, padding='same'))
model.add(Convolution1D(32, 3, padding='same'))
model.add(Convolution1D(16, 3, padding='same'))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(180, activation='sigmoid'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

# Log to tensorboard
tensorBoardCallback = TensorBoard(log_dir='./logs', write_graph=True)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=N_EPOCH, callbacks=[tensorBoardCallback], batch_size=64)

# Evaluation on the test set
scores = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

model.save('models/' + str(now) + '-yok-detect-model.h5')
shutil.copy2('models/' + str(now) + '-yok-detect-model.h5', "models/latest-yok-detect-model.h5")