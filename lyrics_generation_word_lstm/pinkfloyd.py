with open('pink_floyd_lyrics.txt') as f:
    txt = f.read()

songs = txt.split('\n\n\n')

for i, song in enumerate(songs):
    open('data/PinkFloyd/song_%s.txt' %i , 'w').write(song)
