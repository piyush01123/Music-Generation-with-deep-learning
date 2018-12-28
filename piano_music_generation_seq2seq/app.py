import flask
import random
import generate_music as zen
from config import cfg
from keras.models import model_from_json
from midi_io import midiToPianoroll, createSeqTestNetInputs, seqNetOutToPianoroll, pianorollToMidi
import numpy as np
import time

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['midi', 'mid'])

model = model_from_json(open(cfg.DATA.MODEL_PATH).read())
model.load_weights(cfg.DATA.WEIGHTS_PATH)
model.compile(loss= cfg.MODEL_PARAMS.LOSS_FUNCTION , optimizer=cfg.MODEL_PARAMS.OPTIMIZER)
X = np.random.randn(10, 50, 49)
print(model.predict(X)[0])

app = flask.Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def webpage():
    return flask.render_template('index.html')

@app.route('/generate', methods = ['POST'])
def generate():
    file = flask.request.files['midifile']
    if file.filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        print(model.summary())
        fn = 'uploads/input_file_%s.mid' %(time.strftime("%Y_%m_%d_%H_%M_%s"))
        file.save(fn)
        gn = 'static/AI_generated_%s.mid' %(time.strftime("%Y_%m_%d_%H_%M_%s"))
        # zen.generate_double(fn, gn)
        test_piano_roll = midiToPianoroll(fn)
        test_data = [test_piano_roll]
        test_input = createSeqTestNetInputs(test_data, cfg.MODEL_PARAMS.X_SEQ_LENGTH)
        test_data = test_input[0]
        net_output = model.predict(test_data)
        net_roll = seqNetOutToPianoroll(net_output)
        total_roll = np.concatenate((test_piano_roll, net_roll))
        pianorollToMidi(net_roll, gn)

        return flask.jsonify({'generated': gn})
    else:
        return "You have uploaded invalid file"

@app.route('/test', methods=['GET'])
def test():
    return flask.jsonify({'ping': 'ping_data'})

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run('0.0.0.0', 8000, debug = True)
