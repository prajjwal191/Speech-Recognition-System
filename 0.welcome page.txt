from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Speech Recognition System")
root.state("zoomed")
root.geometry("600x400")
top_frame = Frame(root, bg="#2F3C7E", width=1700, height=500)
top_frame.place(x=0, y=0)

top_frame1 = Frame(root, bg="#FBEAEB", width=1700, height=500)
top_frame1.place(x=0, y=400)

var = StringVar()
label = Label(root, textvariable =var,font="arial 24 bold", fg= "yellow",bg="#2F3C7E",bd = 5,padx=10,pady=5,justify ="left",relief="groove")
var.set("Speech\nRecognition\nSystem")
label.place(x=20,y=40)


text1= """Welcome to Speech recognition system!\n
This technology allows devices to take spoken audio,interpret it and generate\n text from it, and then this text is processed furthermore in order to search it in browser,\nwhich helps users to search their query even without typing it."""
t1=Label(root,text=text1,bg="#2F3C7E",fg="#F0F8FF",font="Roboto 14",pady=5)
t1.place(x=450,y=60)


image1=Image.open("C:\\Users\\prajjwal shukla\\Desktop\\project images\\speechrecognition.png")
image=  ImageTk.PhotoImage(image1)
t2=Label(root,image=image,borderwidth="5",relief="solid")
t2.place(x=350,y=261)



def SPEECH():
    root.destroy()
    import speech_search




f = ("Times bold", 16)
Button(
    root,
    bg="#000080",
    fg="white",
    text="Enter Into Speech Recognition System",
    font=f,
    pady=10,
    padx=50,
    command= SPEECH
).place(x=560,y=690)

root.mainloop()