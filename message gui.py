
from tkinter import *
main = Tk()

main.config(bg='black')
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.pack( ) 
main.mainloop( ) 
