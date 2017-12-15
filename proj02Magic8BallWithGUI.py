#!/usr/bin/env python3
# proj02Magic8BallWithGUI.py - r/BeginnerProjects #2 BONUS
# https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/

import time, random
import tkinter as tk

responses = ["Type in a question and click Ask", 
	"Hmm... thinking...",
	"Nah.",
	"Get out of here.",
	"Could be, who knows man.",
	"Yes",
	"Technically your odds aren't zero, but realistically...",
	"Maybe.",
	"You're wasting everyone's time, ask me a real question.",
	"Totally",
	"I'm optimistic",
	"The future is cloudy"]
	
def mainevent():

	def Ask(): # TODO: Currenty thinking is never applied, it sleeps and then changes to random response
		#instructions.delete(0, tk.END)   # Clear previous output
		#instructions.insert(0, "Thinking...") # Insert response
		#time.sleep(3)
		instructions.delete(0, tk.END)
		instructions.insert(0, responses[random.randint(2, len(responses)-1)])
		
	def Clear():
		entryQuestion.delete(0, tk.END)
		
	def PlayAgain():
		instructions.delete(0, tk.END)
		instructions.insert(0, "Type in a question below and then click Ask")
		entryQuestion.delete(0, tk.END)
	
	root = tk.Tk()	
	root.title("Magic 8 Ball")
	root.geometry("500x250")
	
	frame = tk.Frame(root)
	frame.pack()
	
	instructions = tk.Entry(root, width=100, justify=tk.CENTER)
	instructions.insert(tk.END, "Type in a question below and then click Ask")
	instructions.pack()
	
	entryQuestion = tk.Entry(root)
	entryQuestion.pack()
	
	buttonAsk = tk.Button(root, text="Ask", command=Ask)
	buttonAsk.pack()
	
	buttonClear = tk.Button(root, text="Clear", command=Clear)
	buttonClear.pack()
	
	buttonPlayAgain = tk.Button(root, text="Play Again", command=PlayAgain)
	buttonPlayAgain.pack()
	
	buttonQuit = tk.Button(root, text="Quit", command=root.destroy)
	buttonQuit.pack()
	
	root.mainloop()

mainevent()
