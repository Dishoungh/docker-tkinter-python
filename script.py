from tkinter import *

def run():
    name = name_storage.get();
    print(name);

screen = Tk();
screen.title("Docker Python GUI")
screen.geometry("600x600");

welcome_text = Label(text = "Welcome to the first Docker graphics container", fg = "red", bg = "yellow");
welcome_text.pack();

click_me = Button(text = "Click Me", fg = "red", bg = "yellow", command = run);
click_me.place(x = 10, y = 20);

name_storage = StringVar();
nameVar = Entry(textvariable = name_storage);
nameVar.pack();
screen.mainloop();
