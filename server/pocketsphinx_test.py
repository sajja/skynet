from pocketsphinx import LiveSpeech
import speech_recognition as sr

speech = LiveSpeech(lm=False, keyphrase='hello', kws_threshold=1e-20)
for phrase in speech:
    print(phrase.segments(detailed=True))
