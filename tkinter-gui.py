#import tkinter module
import tkinter as tk


#define function
#function displays text in the root window
def red_apple():
    tk.Label(root,text="Always looks red").pack()
    
def green_apple():
    tk.Label(root,text= "Always looks green").pack()

#root widget window
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#title on root window
root.title("My Program")
#creating a label widget
#define and put up on the screen
#myLabel = tk.Label(root, text ="Hello World!")
#myLabel2 = tk.Label(root, text="Whats going on ")
#myButton = tk.Button(root, text="Click!!")
#Pushing to the screen
#myLabel.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)
#create button
#button for red apple
tk.Button(frame, text="RED APPLE", fg= "red", command= red_apple).pack(side= tk.LEFT)
#redButton.bind("<Button-1>",red_apple)
#button for green apples
tk.Button(frame, text="Green Apple", fg="green", command = green_apple).pack(side=tk.LEFT)

#main Loop
root.mainloop()
