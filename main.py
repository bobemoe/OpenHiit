import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

from saythis.initialize import initialize_platform
from saythis.ttsspeak import ttsSpeak

__version__ = '1.0.1'

class OpenHiit(GridLayout):
	mode='stopped'
	countdown=0

	def toggle(self):
		if self.mode=='stopped' or self.mode=='finished':
			self.start()
		else:
			self.stop()

	def start(self):
		self.ids.button.text="Stop"
		self.mode='start'
		self.countdown=0
		self.clock=Clock.schedule_interval(self.clock_callback, 1)

	def stop(self):
		self.ids.button.text="Start"	
		Clock.unschedule(self.clock_callback)
		self.mode='stopped'

	def clock_callback(self,dt):
		self.countdown-=1
		if(self.countdown<=0):
			if self.mode=='start':
				self.mode='warmup'
				self.countdown=int(self.ids.warmup.text)
				self.rounds=int(self.ids.rounds.text)				
			elif self.mode=='warmup':
				self.mode='work'
				self.countdown=int(self.ids.work.text)
			elif(self.mode=='work'):
				self.mode='rest'
				self.countdown=int(self.ids.rest.text)
				self.rounds-=1
				if self.rounds==0:
					self.mode='finished'
			elif(self.mode=='rest'):
				self.mode='work'
				self.countdown=int(self.ids.work.text)
			ttsSpeak(self.mode)
		if(self.mode!='finished'):
			if(self.countdown<=3):
				ttsSpeak(str(self.countdown))
		else:
			self.stop()

class OpenHiitApp(App):
	def build(self):
		initialize_platform()
		return OpenHiit()

if __name__ == '__main__':
	OpenHiitApp().run()
