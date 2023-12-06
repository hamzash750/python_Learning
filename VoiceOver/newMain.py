# Python program to show
# how to convert text to speech
import pyttsx3
  
# Initialize the converter
converter = pyttsx3.init()
voices = converter.getProperty('voices')
converter.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
converter.setProperty('voice', 'english_rp+f3') 
converter.setProperty('voice', voices[1].id)
# Set properties before adding
# Things to say
  
# Sets speed percent 
# Can be more than 100
converter.setProperty('rate', 170)
# Set volume 0-1
converter.setProperty('volume', 1)
  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence
mytext = "Please Like Comment Share And Subscribe For More Video"
  
converter.say("Hello GeeksforGeeks")
converter.say("I'm also a geek")
  
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.save_to_file(mytext,"likeshare.mp3")
converter.runAndWait()
