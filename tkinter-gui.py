#import tkinter module
import tkinter as tk


#define function
def red_apple():
    print('Always looks red')
def green_apple():
    print('Always looks green')

#root widget
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
#creating a label widget
#define and put up on the screen
#myLabel = tk.Label(root, text ="Hello World!")
#myLabel2 = tk.Label(root, text="Whats going on ")
#myButton = tk.Button(root, text="Click!!")
#Pushing to the screen
#myLabel.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)
#create button
redButton = tk.Button(frame, text="RED APPLE", fg= "red", command= red_apple)
redButton.pack(side= tk.LEFT)
greenButton = tk.Button(frame, text="Green Apple", fg="green", command = green_apple)
greenButton.pack(side= tk.LEFT)
#main Loop
root.mainloop()
