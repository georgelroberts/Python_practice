"""

G. L. Roberts

September 2017

Uses kivy to remake cora's cancer cell counting app. Previously implemented
in Matlab, now can be exported to android/iOS.
Shows last three values on the screen, continually saves to a Json file, 
and also displays all results when desired.
"""

#TODO: Change output in .kv file. Want to show filepath somewhere,
#		previous three results (in a logical way) and show all results.
#TODO: Export to android using buildozer

import kivy
import numpy as np
import os
kivy.require('1.9.0')

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.storage.dictstore import DictStore
from kivy.storage.jsonstore import JsonStore
import json
from os.path import join

class CalcGridLayout(GridLayout):
	
	completeList=[]
	lastThree=[]
	histDataTemp=[]
	histDataDict={}

	def showLastThreeResults(self):
		if len(self.completeList)>=3:
			self.lastThree=self.completeList[-3:]
		else:
			self.lastThree=self.completeList

		self.lastThreeRes.text=', '.join(str(x) for x in self.lastThree)

	def addToList(self,value):
		self.completeList.append(value)
		self.showLastThreeResults()
		self.saveResultsToFile()
	
	def showAllResults(self):
		self.allResults.text = str(self.histDataDict).replace("{","").replace("}","").replace(",","; ")

	def saveResultsToFile(self):
		# This should work across platforms
		self.histDataTemp=np.histogram(self.completeList,bins=8,range=[1,8])
		self.histDataTemp=np.ndarray.tolist(self.histDataTemp[0])
		self.histDataDict={i:self.histDataTemp[i-1] for i in range(1,9)}

		sdpath = CoraMicroscopeApp.get_running_app().user_data_dir
		storedPath=join(sdpath,'user.json')
		os.remove(storedPath)
		store = JsonStore(storedPath)
		store.put(json.dumps(self.histDataDict,ensure_ascii=False))
		self.fileLocation.text=storedPath

	def deleteLastResult(self):
		del self.completeList[-1]
		self.showLastThreeResults()
		self.saveResultsToFile()
			

class CoraMicroscopeApp(App):

	def build(self):
		return CalcGridLayout()

coraMicroscopeApp = CoraMicroscopeApp()
coraMicroscopeApp.run()
