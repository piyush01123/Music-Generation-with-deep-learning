import flask
import os
# import infer_lyrics as lyric
import numpy as np
from keras.models import load_model, model_from_json
import five_words as five
M = load_model("lyrical_lstm.h5")


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




# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("lyrical_lstm_weights.h5")
loaded_model.load_weights("new_weights.h5")
print("Loaded model from disk")
x = np.zeros((1, 40, 49))
print(loaded_model.predict(x, verbose=0)[0])

def preprocess(input_text):
    input_text = input_text.lower()
    if len(input_text)<40:
        input_text+=" "*(40-len(input_text))
    if len(input_text)>40:
        input_text = input_text[:40]
    return input_text


app = flask.Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def webpage():
    return flask.render_template('index.html')


@app.route('/five', methods=['GET'])
def webpage_five():
    return flask.render_template('index_two.html')



@app.route('/lyrics', methods = ['POST'])
def search():

    print('$'*10)
    import numpy as np
    from keras.models import load_model
    x = np.zeros((1, 40, 49))
    # M = load_model("lyrical_lstm.h5")
    # M._make_predict_function()
    # print(M.predict(x, verbose=0)[0])
    # print(predictor(x))
    print(loaded_model.predict(x, verbose=0)[0])
    print('^'*10)

    content = flask.request.get_json(silent = True)
    input_text = content['search_text']
    print('input_text***********', input_text)
    # generated = lyric.infer(input_text)
    input_text = preprocess(input_text)
    print('input_text***********', input_text)
    generated = ''
    generated += input_text
    for i in range(400):
        x = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
        for t, char in enumerate(input_text):
            x[0, t, char_to_index[char]] = 1.

        predictions = loaded_model.predict(x, verbose=0)[0]
        next_index = helper.sample(predictions, DIVERSITY)
        next_char = indices_char[next_index]

        generated += next_char
        input_text = input_text[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()

    return flask.jsonify({'generated': generated})


@app.route('/lyricsfive', methods = ['POST'])
def searchfive():

    print('$'*10)
    import numpy as np
    from keras.models import load_model
    x = np.zeros((1, 40, 49))
    # M = load_model("lyrical_lstm.h5")
    # M._make_predict_function()
    # print(M.predict(x, verbose=0)[0])
    # print(predictor(x))
    print(loaded_model.predict(x, verbose=0)[0])
    print('^'*10)

    content = flask.request.get_json(silent = True)
    input_text = content['search_text']
    print(input_text, '#'*10)
    input_text = ' '.join(five.get_sentences(input_text))
    print('@'*10, input_text, '@'*10)
    return flask.jsonify({'generated': input_text})
    # generated = lyric.infer(input_text)
    input_text = preprocess(input_text)
    generated = ''
    generated += input_text
    for i in range(400):
        x = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
        for t, char in enumerate(input_text):
            x[0, t, char_to_index[char]] = 1.

        predictions = loaded_model.predict(x, verbose=0)[0]
        next_index = helper.sample(predictions, DIVERSITY)
        next_char = indices_char[next_index]

        generated += next_char
        input_text = input_text[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()

    return flask.jsonify({'generated': generated})


@app.route('/test', methods=['GET'])
def test():
    return flask.jsonify({'ping': 'ping_data'})

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run('0.0.0.0', 8001, debug = True)
