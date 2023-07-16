import speech_recognition as sr
import pyttsx3 as t2s
import openai

#initialise speech to text
listner = sr.Recognizer()

#initialize text to speech
engine = t2s.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

openai.api_key = "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"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        print("Microphone issue")
    
    return command

def runOpenAI(text): 
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "assistant", "content": text}])
    returnedOutput = completion.choices[0].message.content
    print(returnedOutput)
    return returnedOutput

#RunInteractiveGPT
talk(runOpenAI(takeCommand()))
