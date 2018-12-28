from midi_io import midiToPianoroll, createSeqTestNetInputs, seqNetOutToPianoroll, pianorollToMidi
from keras.models import model_from_json
from config import cfg
import time
import random
import glob
import numpy as np
DATA_DIR = 'data/'

model = model_from_json(open(cfg.DATA.MODEL_PATH).read())
model.load_weights(cfg.DATA.WEIGHTS_PATH)
model.compile(loss= cfg.MODEL_PARAMS.LOSS_FUNCTION , optimizer=cfg.MODEL_PARAMS.OPTIMIZER)
print(model.summary())

def generate_double(fn, gn):
    test_piano_roll = midiToPianoroll(fn)
    test_data = [test_piano_roll]
    test_input = createSeqTestNetInputs(test_data, cfg.MODEL_PARAMS.X_SEQ_LENGTH)
    test_data = test_input[0]
    net_output = model.predict(test_data)
    net_roll = seqNetOutToPianoroll(net_output)
    total_roll = np.concatenate((test_piano_roll, net_roll))
    pianorollToMidi(net_roll, gn)


def test():
    midi_files  = glob.glob(DATA_DIR +'/*.mid')
    file_idx = random.randint(0,len(midi_files) - 1)
    # midi_file = midi_files[file_idx]
    midi_file = 'uploads/mozk175b_trimmed.mid'
    print('Generating from %s' %midi_file)
    test_piano_roll = midiToPianoroll(midi_file)
    test_data = [test_piano_roll]
    test_input = createSeqTestNetInputs(test_data, cfg.MODEL_PARAMS.X_SEQ_LENGTH)
    test_data = test_input[0]

    generated_file = 'AI_generated_%s.mid' %(time.strftime("%Y_%m_%d_%H_%M_%s"))
    generated_path = '%s/%s' %(cfg.DATA.GENERATED_DIR, generated_file)

    net_output = model.predict(test_data)
    print("net_output:", np.array(net_output.shape))
    net_roll = seqNetOutToPianoroll(net_output)
    print("net_roll:", net_roll.shape)
    pianorollToMidi(net_roll, generated_path)

def test_identity_fn():
    # verify the identity function
    midi_file = 'uploads/mozk175b_trimmed.mid'
    test_piano_roll = midiToPianoroll(midi_file)
    generated_path = '%s/%s' %(cfg.DATA.GENERATED_DIR, 'same.mid')
    pianorollToMidi(test_piano_roll, generated_path)

if __name__=='__main__':
    test()
    test_identity_fn()
