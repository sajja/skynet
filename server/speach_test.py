import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone(device_index=14)

try:
    print("A moment of silence, please...")
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    # r.energy_threshold = 200
    # r.dynamic_energy_threshold = False
    names = sr.Microphone.list_microphone_names()
    print(names)
    
    while True:
        print("Say something!")
        with m as source: 
            r.adjust_for_ambient_noise(source,duration=0.5)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            # audio = r.listen(source, phrase_time_limit=5 )
            audio = r.listen(source, phrase_time_limit=5 )
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio,show_all=True)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
