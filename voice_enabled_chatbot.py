import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
from pygame import mixer
import pyaudio
pa = pyaudio.PyAudio()
chosen_device_index = -1
for x in xrange(0,pa.get_device_count()):
    info = pa.get_device_info_by_index(x)
    #print pa.get_device_info_by_index(x)
    if info["name"] == "pulse":
        chosen_device_index = info["index"]
        #print "Chosen index: ", chosen_device_index
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input_device_index=chosen_device_index, input=True, output=False)
stream.start_stream()
def run():
	engine=pyttsx3.init()
	voices=engine.getProperty('voices')
	engine.setProperty('voice',voices[1].id)
	volume=engine.getProperty('volume')
	engine.setProperty('volume',10.0)
	rate=engine.getProperty('rate')
	engine.setProperty('rate',rate-100)
	greetings=['hello','hi there','hey','hi']
	howdy=['how are you?','how you doin?']
	answers=['i am fine','i am good','okay']
	creator=['Who made you?','Who created you?']
	cmd_jokes=['Tell me a joke','Make me laugh']
	youtube=['Open Youtube','Want to watch a video']
	binge_watch=['I wanna binge watch','Open Amazon prime']
	cmd_web=['Open Google','Connect to the web']
	jokes=['Why is advanced math to be taken easy?......because it is as easy as pi','Why did the scarecrow get an award?....He was outstanding in his field'
	,'What do you give a sick lemon?......lemon-aid']
	bye=['bye','Bye....talk to you later','Happy to have helped you']
	talk_color=['Which is your favourite color?','What color do you like?']
	color=['Pink','Red','Lavender','Blue','Yellow']
	add_tasks=['Hey Bhau add some tasks to my tasklist','Add something to my tasklist','add to tasks']
	show_tasks=['Hey Bhau show me my tasks for today','Show me my work for today']
	engine.say("Hello....how may I help you?")
	engine.runAndWait()
	while (True):
		inst=raw_input()
		r=sr.Recognizer()
		with sr.Microphone() as source:
			print("SAY SOMETHING")
			r.adjust_for_ambient_noise(source,duration=1)
			audio=r.listen(source)
			print("TIME OVER")
			try:
				print('You said: '+inst)
			except sr.UnknownValueError:
				print('Could not get your message.....Please try again')
				engine.say('Could not get you.....Rerun the code to try again')
				engine.runAndWait()
		print(inst)
		if (inst in greetings):
			r_greet=random.choice(greetings)
			print(r_greet)
			engine.say(r_greet)
			engine.runAndWait()
		elif inst in howdy:
			r_ans=random.choice(answers)
			r_q=random.choice(howdy)
			print(r_ans+r_q)
			engine.say(r_ans+r_q)
			engine.runAndWait()
		elif inst in creator:
			print('I was made by Vaibhavi')
			engine.say('I was created by Vaibhavi')
			engine.runAndWait()
		elif inst in cmd_jokes:
			r_jokes=random.choice(jokes)
			print(r_jokes)
			engine.say(r_jokes)
			engine.runAndWait()
		elif inst=='I want to pass my time':
			r_converse=random.choice(talk_color)
			print(r_converse)
			engine.say(r_converse)
			engine.runAndWait()
			if inst in talk_color:
				r_cont=random.choice(color)
				print(r_cont)
				engine.say(r_cont)
				engine.runAndWait()
		elif inst in cmd_web:
			webbrowser.open("https://www.google.com/")
			engine.runAndWait()
		elif inst in youtube:
			webbrowser.open("https://www.youtube.com/")
			engine.say("Here, I have opened Youtube")
			print("Here, I have opened Youtube")
			engine.runAndWait()
		elif inst in binge_watch:
			webbrowser.open("https://www.primevideo.com/")
			engine.say("Here,I have opened Amazon Prime Video...Login and enjoy your binge")
			print("Here,I have opened Amazon Prime Video...Login and enjoy your binge")
			engine.runAndWait()
		elif inst=='Hey bhau wish Jahanvi a Happy Birthday':
			engine.say('sure')
			engine.say('Wish you a very Happy Birthday Jahanvi.....How about a birthday song?')
			webbrowser.open("https://www.youtube.com/watch?v=bV2GklFBaT8")
			engine.runAndWait()
		else:
			engine.say("Please wait")
			print("Please Wait")
			engine.say(wikipedia.summary(inst))
			print(wikipedia.summary(inst))
			engine.runAndWait()
