
import runner_copy as rc
load_path = "../save/models/lyricmodel/PinkFloyd.ckpt-70000"
artist_name = "PinkFloyd"
test = True

def infer(prime_text):
    prime_text = prime_text.lower()
    lyricmodel = rc.LyricGenRunner(load_path, artist_name, test, prime_text)
    result = lyricmodel.test(prime_text)
    return result

if __name__ == '__main__':
    prime_text = "Hey you would you help me to carry the stone"
    prime_text = prime_text.lower()
    # prime_text = None
    lyricmodel = rc.LyricGenRunner(load_path, artist_name, test, prime_text)
    result = lyricmodel.test(prime_text)
    print('*'*20, "result = %s "%result, '*'*20)
