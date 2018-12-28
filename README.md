
Code for music generation that I wrote in a 2-day hackathon.
[Presentation](https://github.com/piyush-kgp/Music-Generation-with-AI/blob/master/Music%20generation%20with%20AI.pdf)


Things I completed:
- Lyrics Generation in Pink Floyd style using LSTM on word vectors,
Credits to <https://github.com/dyelax/encore.ai>
- Piano music generation in Mozart's style with seq2seq model, Credits to <https://github.com/Azure/MachineLearning-MusicGeneration>

Also was able to get lyrics generation with char-LSTM to work, inspired from <https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py>
But ditched it for demo because it is trained on characters and so will only learn conditional occurrence of characters (It will generate meaningless words.)

All 3 have a web-based demo (in flask). I scraped Mozart's symphonies and Pink Floyd's lyrics from websites <http://www.midiworld.com> and <https://www.allthelyrics.com> respectively.


Things I tried but ran out of time:
- MUSEGAN (<https://github.com/salu133445/musegan>)
- Biaxial RNN (<https://github.com/hexahedria/biaxial-rnn-music-composition>)
- Classical Piano composer <https://github.com/Skuldur/Classical-Piano-Composer>
- Clara: A Neural Net Music Generator at <https://github.com/mcleavey/musical-neural-net>
I was excited about the last one because I thought the way that Christine Payne (OpenAI) has converted music to vectors is very innovative.
 You can find her blog about it [here](http://christinemcleavey.com/clara-a-neural-net-music-generator)
 But ran out of time.

#### Why Christine's pre-processing is so smart?
In her own words:
One option would be to ask the model to predict yes/no for each of the 88 piano keys, at every musical time step.
<b>(Every other model on Github has done exactly this for pre-processing)</b>
However, since each individual key is silent for the great majority of the time, it would be very difficult for a model to learn to ever risk predicting “yes” for a note. I offer two different possible solutions for this problem. In language models, we often work at either the word-level or character-level. Similarly, for music generation, I offer either chordwise or notewise levels.

She goes on to explain how she constructed these chordwise and notewise vectors.


#### What's next
I want to use Christine's preprocessing technique and try other models with those chord and note vectors (GAN is a first thought).
Will post an update with new implementation soon.
