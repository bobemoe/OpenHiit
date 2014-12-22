import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

from saythis.initialize import initialize_platform
from saythis.ttsspeak import ttsSpeak

__version__ = '1.0.0'

class SettingsScreen(GridLayout):

	def __init__(self, **kwargs):
		super(SettingsScreen, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='Warmup:'))
		self.warmup = TextInput(multiline=False,text="10")
		self.add_widget(self.warmup)
		self.add_widget(Label(text='Rounds:'))
		self.rounds = TextInput(multiline=False,text="5")
		self.add_widget(self.rounds)
		self.add_widget(Label(text='Work:'))
		self.work = TextInput(multiline=False,text="20")
		self.add_widget(self.work)
		self.add_widget(Label(text='Rest:'))
		self.rest = TextInput(multiline=False,text="10")
		self.add_widget(self.rest)
		self.start=Button(text='Start');
		self.add_widget(self.start)
		self.start.bind(on_press=self.start_callback)
		self.stop=Button(text='Stop');
		self.add_widget(self.stop)
		self.stop.bind(on_press=self.stop_callback)		

	def start_callback(instance, value):
		print('My button <%s> state is <%s>' % (instance, value))
		MyApp.hiit=Hiit(int(MyApp.root.warmup.text), int(MyApp.root.rounds.text), int(MyApp.root.work.text), int(MyApp.root.rest.text));

	def stop_callback(instance, value):
		print('My button <%s> state is <%s>' % (instance, value))
		MyApp.hiit.stop();

class MyApp(App):

	root=0

	def build(self):
		initialize_platform()
		MyApp.root=SettingsScreen()
		return MyApp.root

class Hiit():
	def __init__(self, warmup, rounds, work, rest):
		self.warmup=warmup
		self.rounds=rounds
		self.work=work
		self.rest=rest
		self.mode='warmup'
		self.countdown=warmup
		self.clock=Clock.schedule_interval(self.clock_callback, 1)
		ttsSpeak(self.mode)

	def clock_callback(self,dt):
		self.countdown-=1
		if(self.countdown==0):
			if(self.mode=='warmup'):
				self.mode='work'
				self.countdown=self.work
			elif(self.mode=='work'):
				self.mode='rest'
				self.countdown=self.rest
				self.rounds-=1
				if self.rounds==0:
					self.mode='finished'
			elif(self.mode=='rest'):
				self.mode='work'
				self.countdown=self.work
			ttsSpeak(self.mode)
		if(self.mode!='finished'):
			if(self.countdown<=3):
				ttsSpeak(str(self.countdown))
		else:
			self.stop()

	def stop(self):
		Clock.unschedule(self.clock_callback)

if __name__ == '__main__':
	MyApp().run()