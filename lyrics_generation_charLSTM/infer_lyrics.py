from keras.models import load_model
import helper
import numpy as np
import sys
SEQUENCE_LENGTH = 40
SEQUENCE_STEP = 3
PATH_TO_CORPUS = "pink_floyd_lyrics.txt"
EPOCHS = 20
DIVERSITY = 1.0
text = helper.read_corpus(PATH_TO_CORPUS)
chars = helper.extract_characters(text)
sequences, next_chars = helper.create_sequences(text, SEQUENCE_LENGTH, SEQUENCE_STEP)
char_to_index, indices_char = helper.get_chars_index_dicts(chars)

model = load_model("lyrical_lstm.h5")

def preprocess(input_text):
    input_text = input_text.lower()
    if len(input_text)<40:
        input_text+=" "*(40-len(input_text))
    if len(input_text)>40:
        input_text = input_text[:40]
    return input_text

def infer(input_text):
    input_text = preprocess(input_text)
    print('input_text***********', input_text)
    generated = ''
    generated += input_text
    for i in range(400):
        x = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
        for t, char in enumerate(input_text):
            x[0, t, char_to_index[char]] = 1.

        predictions = model.predict(x, verbose=0)[0]
        next_index = helper.sample(predictions, DIVERSITY)
        next_char = indices_char[next_index]

        generated += next_char
        input_text = input_text[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()
    return generated
