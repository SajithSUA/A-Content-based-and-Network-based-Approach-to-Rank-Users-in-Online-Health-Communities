from tkinter import *
from tkinter import messagebox


window = Tk()
window.configure(background="#9980FA")
window.title("Stack Overflow User Expertise Detector")
window.geometry('350x400')
lbl = Label(window, text="Predict Expertise", wraplength=300, background="#0652DD")
lbl.pack(fill=BOTH, expand=1)
#btn2 = Button(window, text="Get Features", command=get_features, background="#1289A7")
#btn2.pack(fill=BOTH, padx=40, pady=20)
#btn1 = Button(window, text="Train", command=train, background="#1289A7")
#btn1.pack(fill=BOTH, padx=40, pady=20)

lb2 = Label(window, text="Enter Sample number from 20", wraplength=300, background="#0652DD")
lb2.pack(fill=BOTH, padx=80, pady=0)
entry = Entry(window,bg='white')
entry.pack(fill=BOTH, padx=150, pady=20)
btn = Button(window, text="Predict Technical Level", background="#1289A7")
btn.pack(fill=BOTH, padx=40, pady=20)
window.mainloop()