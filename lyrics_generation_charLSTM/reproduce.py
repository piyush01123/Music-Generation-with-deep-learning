import numpy as np
from keras.models import load_model
M = load_model("lyrical_lstm.h5")

def f(x):
    return M.predict(x, verbose=0)[0]

x = np.zeros((1, 40, 49))
print(f(x))
