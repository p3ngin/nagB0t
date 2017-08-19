#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import time
import sys
import os

'''
Program to initialize GUI on time delay to validate various things have been done. Currently is built for 1 parameter (exercise).
Goal is to have 3+ different parameters in different pop-up windows to validate various things are being done and run in the background
until all parameters are completed. Time delay on hiding windows and showing again will eventually be increased to multiple hours.

*Will run on startup and run in background throughout day.
'''

class subModule():
	def __init__(self, paramText, show_interval=3, hide_interval=6):
		# Constructs class parameters and builds GUI
		self.hide_int = hide_interval  # In seconds
		self.show_int = show_interval  # In seconds
		self.paramText = paramText
		self.parameterCount = 0

		self.root = Tk()

		# Default creation variables for GUI
		self.root.title("***Alert***")
		self.root.minsize(width=300, height=150)
		self.label = Label(self.root, text=paramText)
		self.label.pack()

		# Creates Buttons on GUI and calls commands for when Yes and No buttons are pressed.
		# If 'Yes' button is pressed, excel file to input exercises is opened via openExcel method
		self.buttonYes = Button(self.root, text ="Yes", command=self.openExcel)
		self.buttonYes.pack()

		# If 'No' button is pressed, increment method called which will then hide window and show again after time
		# **This is temporary as the incremental method will eventually be used for validation of various parameters before Program can exit
		self.buttonNo = Button(self.root, text ="No", command=self.increment)
		self.buttonNo.pack()

	def increment(self):
		# Increment count variable if Yes was selected
		# Counter was introduced for testing and eventually will become separate windows with various questions i.e. Exercised today? Chores done? etc.
		self.parameterCount = (self.parameterCount + 1)
		print("Count = ", self.parameterCount)
		self.hide()

	def hide(self):
		self.root.withdraw()  # Hide the window
		self.root.after(1000 * self.hide_int, self.show) # Schedule self.show() in hide_int seconds

	def show(self):
		# Check the count to see if all parameters have been met, hide/show to ask again
		if (self.parameterCount < 3):
			self.root.deiconify() # Show the window
		else:
			self.quitApp()

	def start(self):
		# Intialize the GUI loop
		self.root.mainloop()

	def openExcel(self):
		# open excel file to input daily exercise (don't want to automate writing to this as it'll be difficult with inputting different types of exercise) and call program to quit
		exFile_dir = os.getcwd()
		os.startfile((exFile_dir + '\\excelFiles\\dailyWorkouts.xlsx'))
		self.quitApp()

	def quitApp(self):
		# Exit application
		print("Exiting program.")
		raise SystemExit


if __name__ == "__main__":
	exercise = subModule("Have you exercised yet?")
	exercise.start()