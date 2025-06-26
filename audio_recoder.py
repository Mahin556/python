import sounddevice as sd
import wavio as wv
import scipy as sy

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values of duration and sample frequency
recording=sd.rec(int(duration * freq), samplerate=freq, channels=1)
# Record audio for the given number of seconds
sd.wait()

wv.write("recording1.wav", recording, freq, sampwidth=2)


