import pyttsx3

#   Credit to https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13
#   For explaining how to install other voices/languages

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# To check which voices are available:

# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()

engine.setProperty('voice', voices.id)
engine.say('Hello world')
engine.runAndWait()