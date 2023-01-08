from tkinter import *
from tkinter import ttk
import googletrans
import pyttsx3
from googletrans import Translator

root = Tk()
root.title("Language Translator")
root.state("zoomed")
root.geometry("600x400")
root.configure(bg="#008080")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)



def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    engine = pyttsx3.init()
    engine.say(trans_text)
    engine.setProperty('rate',80)
    engine.runAndWait()

    text2.delete(1.0, END)
    text2.insert(END, trans_text)





top_frame = Frame(root, bg="#FFEB3B", width=1700, height=100)
top_frame.place(x=0, y=0)

logo = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\speakerlogo.png.png")
Label(top_frame, image=logo,bg="#FFEB3B").place(x=8, y=4)
Label(top_frame, text="LANGUAGE TRANSLATOR", font="arial 20 bold",bg="#F44336",fg="white").place(x=550, y=30)

image_icon = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\project images\\speak.png.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\project images\\arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=650, y=280)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=210, y=215)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 20 bold", bg="#EEEEEE",fg="black", width=18, bd=5, relief=GROOVE)
label1.place(x=167, y=255)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=1000, y=215)
combo2.set("SPANISH")

label2 = Label(root, text="ENGLISH", font="segoe 20 bold", bg="#EEEEEE", width=18, bd=5, relief=GROOVE)
label2.place(x=967, y=255)

f = Frame(root, bg="black", bd=5)
f.place(x=100, y=308, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=900, y=308, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="TRANSLATE", font="Roboto 15 bold", activebackground="white", cursor="hand2",
                   bd=1, width=10, height=2, bg="orange", fg="white", command=translate_now)
translate.place(x=665, y=450)

label_change()

def welcome1():
    root.destroy()
    import Welcome

f = ("Times bold", 16)
Button(
    root,
    bg="#000080",
    fg="white",
    text="Homepage",
    font=f,
    pady=10,
    padx=50,
    command= welcome1
).place(x=600,y=690)




root.mainloop()

