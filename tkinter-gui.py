#import tkinter module
import tkinter as tk

#root widget
root = tk.Tk()

#creating a label widget
#define and put up on the screen
myLabel = tk.Label(root, text ="Hello World!")
myLabel2 = tk.Label(root, text="Whats going on ")
#Pushing to the screen
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
#main Loop
root.mainloop()
