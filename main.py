import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock

from saythis.initialize import initialize_platform
from saythis.ttsspeak import ttsSpeak

from kivy.storage.jsonstore import JsonStore

__version__ = '1.0.2'

class OpenHiit(GridLayout):
	mode='stopped'
	countdown=0
	dropdown = DropDown()	

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
		self.store('started')

	def stop(self):
		self.ids.button.text="Start"	
		Clock.unschedule(self.clock_callback)
		self.mode='stopped'

	def store(self,counter):
		warmup=str(self.ids.warmup.text)
		rounds=str(self.ids.rounds.text)
		work=str(self.ids.work.text)
		rest=str(self.ids.rest.text)
		id='('+warmup+') '+rounds+' x '+work+'s <-> '+rest+'s'
		if OpenHiitApp.store.exists(id):
			item=OpenHiitApp.store.get(id);
			if counter in item:
				item[counter]+=1
			else:
				item[counter]=1				
		else:
			item={'warmup':warmup, 'rounds':rounds, 'work':work, 'rest':rest, counter:1}
		OpenHiitApp.store[id]=item
		self.populate_dropdown()

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
			self.store('finished')
			self.stop()

	def populate_dropdown(self):
		self.dropdown.clear_widgets()
		for id in OpenHiitApp.store:
			item=OpenHiitApp.store.get(id)
			if 'finished' in item:
				finished=item['finished']
			else:
				finished=0
			text=id+'  ['+str(finished)+'/'+str(item['started'])+']'
			print(id)
			print(text)
			btn = Button(text=text, size_hint_y=None, height=50)
			btn.data=item

			# for each button, attach a callback that will call the select() method
			# on the dropdown. We'll pass the text of the button as the data of the
			# selection.
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.data))

			# then add the button inside the dropdown
			self.dropdown.add_widget(btn)

		self.ids.mainbutton.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=self.dropdown_select)

	def dropdown_select(self,dropdown,data):
		self.ids.warmup.text=data['warmup']
		self.ids.rounds.text=data['rounds']
		self.ids.work.text=data['work']
		self.ids.rest.text=data['rest']

class OpenHiitApp(App):
	store = JsonStore('history.json')

	def build(self):
		initialize_platform()
		cheese=OpenHiit()
		cheese.populate_dropdown()
		return cheese

if __name__ == '__main__':
	OpenHiitApp().run()
