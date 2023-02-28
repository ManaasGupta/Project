import speech_recognition as sr

def s2t():
# Initialize recognizer
    r = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...") 
        r.adjust_for_ambient_noise(source) 
        print("Say something...")
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio,language='hi-In')
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Oops! Unable to recognize speech.")
    except sr.RequestError as e:
        print("Oops! Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text 

if __name__=='__main__':
    s2t()