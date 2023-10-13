from tkinter import *
from gtts import gTTS
import speech_recognition as sr
import os
from PIL import ImageTk, Image
import webbrowser
mainwindow = Tk()
mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('1366x768')
# mainwindow.resizable(0, 0)
mainwindow.configure(bg='grey')
def say(text1):
    language = 'en'
    speech = gTTS(text=text1, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("start text.mp3")
def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text1 = r.recognize_google(audio, language="en-IN")
            except:
                pass
            return text1
def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry('533x300')
    texttospeechwindow.configure(bg='silver')

    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Times New Roman", 15),
          bg='silver',fg='black').pack()

    text = Text(texttospeechwindow, font=12, height=7, width=30)
    text.place(x=120, y=50)

    speakbutton = Button(texttospeechwindow, text='listen', bg='coral', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=230, y=200)
def Speechtotext():
    secondwin=Tk()
    secondwin.geometry('533x400')
    secondwin.title("Speech to text")
    secondwin.configure(bg="silver")
    lb=Label(secondwin, text='Speech to text', bg='silver', fg='black', font=('bold', 20))
    lb.pack()
    text = Text(secondwin, font=12, height=7, width=30)
    text.place(x=120, y=50)
    bt1=Button(secondwin, text='Speech To Text', bg='red', fg='white', font=('bold', 20),command=lambda: text.insert(END, recordvoice()))
    bt1.place(y=220, x=160)
    bt2=Button(secondwin, text='exit', bg='purple', fg='white', font=('bold', 18), command=exit)
    bt2.place(y=290, x=240)
    secondwin.mainloop()
def web():
    webbrowser.open_new(r"https://www.seedinfotech.com/")
def location():
    webbrowser.open_new(r"https://goo.gl/maps/e5ZisS8zCMCyDvvJ7")
# Creating Menubar
menubar = Menu(mainwindow)
# Adding File Menu and commands
Functions = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Functions', menu = Functions)
Functions.add_command(label ='TextToSpeech', command = TextToSpeech)
Functions.add_command(label ='Speechtotext...', command = Speechtotext)
Functions.add_separator()
Functions.add_command(label ='Exit', command = mainwindow.destroy)
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Help')
help_.add_command(label ='Location', command = location)
help_.add_separator()
help_.add_command(label ='About', command = web)
# display Menu
mainwindow.config(menu = menubar)
Label(mainwindow, text='WELCOME',
      font=('Times New Roman', 40), bg='grey',fg="black").place(x=550, y=20)
Label(mainwindow, text='~ Shortcuts ~',
      font=('Times New Roman', 16), bg='grey',fg='black', wraplength=450).place(x=90, y=170)
texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 13), bg='Purple',fg='white',
                            command=TextToSpeech)
texttospeechbutton.place(x=50, y=270)
speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 13), bg='Purple',fg='white'
                            ,command=Speechtotext)
speechtotextbutton.place(x=50, y=370)
close= Button(mainwindow, text='Close', font=('Times New Roman', 13), bg='Purple',fg='white',
                            command=mainwindow.destroy)
close.place(x=120, y=500)
frame = Frame(mainwindow, width=200, height=100)
frame.place(x=400,y=180)
frame.config(bg='grey')
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("seed-removebg-preview.png"))
# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
fotter=Label(mainwindow,text="Developed By:\nAbhijeet Mudholkar",bg='grey',fg='black',font=20).place(x=630,y=600)
mainwindow.update()
mainwindow.mainloop()
