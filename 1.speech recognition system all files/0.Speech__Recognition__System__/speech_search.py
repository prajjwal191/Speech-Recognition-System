from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Speech Recognition System")
root.state("zoomed")
root.geometry("600x400")
# root.resizable(False,False)
root.configure(bg="#ADD8E6")

engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():

        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 200)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 100)
            setvoice()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():

        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 200)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 120)
            setvoice()

def backend():

                import speech_recognition as sr
                import pyttsx3
                import webbrowser as wb

                r1 = sr.Recognizer()
                r2 = sr.Recognizer()
                r3 = sr.Recognizer()

                def SpeakText(command):

                    engine = pyttsx3.init()
                    engine.say(command)
                    engine.runAndWait()

                with sr.Microphone() as source:
                    r3.adjust_for_ambient_noise(source, duration=0.2)
                    print('speak now')
                    SpeakText("say search now")
                    audio = r3.listen(source)

                    if 'search now' in r2.recognize_google(audio):
                        r2 = sr.Recognizer()

                        url = 'http://www.google.com/search?q='
                        with sr.Microphone():
                            print('search your query')
                            SpeakText("search your query")
                            audio = r2.listen(source)

                            try:
                                get = r2.recognize_google(audio)
                                MyText = r2.recognize_google(audio)
                                MyText = MyText.lower()
                                print("you searched " + MyText)

                                SpeakText("you searched " + MyText)

                                wb.get().open_new(url + get)
                            except sr.UnknownValueError:
                                print('error')
                            except sr.RequestError as e:
                                print('failed'.format(e))


image_icon = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\speak.png.png")
root.iconphoto(False, image_icon)

top_frame = Frame(root, bg="red", width=1700, height=100)
top_frame.place(x=0, y=0)

logo = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\speakerlogo.png.png")
Label(top_frame, image=logo,bg="red").place(x=8, y=4)
Label(top_frame, text="SPEECH RECOGNITION SYSTEM", font="arial 20 bold",bg="red",fg="white").place(x=520, y=30)

text_area = Text(root, font="Robote 15", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=300, width=400, height=150)

Label(root,text="Type here",font="arial 15 bold",bg="white",fg="#FF4500").place(x=155,y=265)
Label(root, text="VOICE", font="arial 15 bold", bg="white", fg="red").place(x=580, y=290)
Label(root, text="SPEED", font="arial 15 bold", bg="white", fg="red").place(x=760, y=290)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=330)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=330)
speed_combobox.set('Normal')

imageicon = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\speak.png.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=380)

imageicon2 = PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\download.png.png")
save = Button(root, text="SAVE", compound=LEFT, image=imageicon2, width=130, bg="#39c790", font="arial 14 bold",command=download)
save.place(x=730, y=380)

imageicon3=PhotoImage(file="C:\\Users\\prajjwal shukla\\Desktop\\project images\\search1.png")
search = Button(root,text="SPEAK AND SEARCH",compound=LEFT,image=imageicon3,width=400,bg="#FFF8DC",font="arial 14 bold",command=backend)
search.place(x=1000,y=350)


f = ("Times bold", 18)


def translate():
    root.destroy()
    import Translator



Button(
    root,
    bg="#000080",
    fg="white",
    text="Language Translator",
    font=f,
    command= translate,
    padx=20,
    pady=10,
).place(x=600,y=680)


root.mainloop()