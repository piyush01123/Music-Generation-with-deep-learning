
Code for music generation that I wrote in a 2-day hackathon.
[Presentation](https://github.com/piyush-kgp/Music-Generation-with-AI/blob/master/Music%20generation%20with%20AI.pdf)


Things I completed:
- Lyrics Generation with LSTM on word vectors,
Credits to <https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py>
- Lyrics Generation with char-LSTM, Credits to <https://github.com/dyelax/encore.ai>
- Piano music with seq2seq model, Credits to <https://github.com/Azure/MachineLearning-MusicGeneration>

All 3 have a web-based demo (in flask).


Thing I tried but ran out of time:
- MUSEGAN (<https://github.com/salu133445/musegan>)
- Biaxial RNN (<https://github.com/hexahedria/biaxial-rnn-music-composition>)
- Classical Piano composer <https://github.com/Skuldur/Classical-Piano-Composer>
- Clara: A Neural Net Music Generator at <https://github.com/mcleavey/musical-neural-net>
<br>
I was excited about the last one because I thought the way that Christine Payne (OpenAI) has converted music to vectors is very innovative.
 You can find details at <http://christinemcleavey.com/clara-a-neural-net-music-generator>. But ran out of time.

#### Why Christine's pre-processing is so smart?
In her own words:
One option would be to ask the model to predict yes/no for each of the 88 piano keys, at every musical time step.
<b>(Every other implementation has done exactly this.)</b>
However, since each individual key is silent for the great majority of the time, it would be very difficult for a model to learn to ever risk predicting “yes” for a note. I offer two different possible solutions for this problem. In language models, we often work at either the word-level or character-level. Similarly, for music generation, I offer either chordwise or notewise levels.

She goes on to explain how she constructed these chordwise and notewise vectors.


#### What's next
I want to use Christine's preprocessing technique and try other models with those vectors (GAN is a first thought).
Will post an update with new implementation soon.
