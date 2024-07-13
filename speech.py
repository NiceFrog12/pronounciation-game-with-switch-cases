import speech_recognition as sr
r = sr.Recognizer()
def speech():
    with sr.Microphone() as source:
        print("Listening... (You have 3.5 seconds)")
        try:
            audio = r.listen(source, timeout=3)
            endoutput = r.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout occurred, no speech detected within 3 seconds.")
            return ""
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        return endoutput
    
