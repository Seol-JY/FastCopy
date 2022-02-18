import tkinter as tk
from tkinter import ttk
import clipboard


class main:
    def __init__(self):
        self.select1 = ['CD001002', '웹 프로그래밍']
        self.select2 = ['복사할항목1', '설명1']
        self.select3 = ['복사할항목2', '설명2']
        self.select4 = ['복사할항목3', '설명3']
        self.select5 = ['복사할항목4', '설명4']
        self.select6 = ['복사할항목5', '설명5']
        self.select7 = ['복사할항목6', '설명6']
        self.select8 = ['복사할항목7', '설명7']

        self.UI()

    def func1(self):
        clipboard.copy(self.select1[0])
        self.qst1.config(fg='red')

    def func2(self):
        clipboard.copy(self.select2[0])
        self.qst2.config(fg='red')

    def func3(self):
        clipboard.copy(self.select3[0])
        self.qst3.config(fg='red')

    def func4(self):
        clipboard.copy(self.select4[0])
        self.qst4.config(fg='red')

    def func5(self):
        clipboard.copy(self.select5[0])
        self.qst5.config(fg='red')

    def func6(self):
        clipboard.copy(self.select6[0])
        self.qst6.config(fg='red')

    def func7(self):
        clipboard.copy(self.select7[0])
        self.qst7.config(fg='red')

    def func8(self):
        clipboard.copy(self.select8[0])
        self.qst8.config(fg='red')

    def UI(self):

        window = tk.Tk()
        window.title('FastCopy')
        window.geometry('465x700')
        window.resizable(True, True)

        tit = tk.Label(window, text='              F a s t   C o p y              ',
                       borderwidth=2, relief='groove')
        tit.place(x=30, y=20, width=408, height=45)

        self.btn1 = tk.Button(window, text='Copy!!', command=self.func1)
        self.btn1.place(x=30, y=95, width=70, height=50)
        self.qst1 = tk.Label(
            window, text=self.select1[0], borderwidth=2, relief='groove')
        self.qst1.place(x=107, y=95, width=190, height=50)
        self.tme1 = tk.Label(
            window, text=self.select1[1], borderwidth=2, relief='groove')
        self.tme1.place(x=300, y=95, width=140, height=50)

        self.btn2 = tk.Button(window, text='Copy!!', command=self.func2)
        self.btn2.place(x=30, y=155, width=70, height=50)
        self.qst2 = tk.Label(
            window, text=self.select2[0], borderwidth=2, relief='groove')
        self.qst2.place(x=107, y=155, width=190, height=50)
        self.tme2 = tk.Label(
            window, text=self.select2[1], borderwidth=2, relief='groove')
        self.tme2.place(x=300, y=155, width=140, height=50)

        self.btn3 = tk.Button(window, text='Copy!!', command=self.func3)
        self.btn3.place(x=30, y=215, width=70, height=50)
        self.qst3 = tk.Label(
            window, text=self.select3[0], borderwidth=2, relief='groove')
        self.qst3.place(x=107, y=215, width=190, height=50)
        self.tme3 = tk.Label(
            window, text=self.select3[1], borderwidth=2, relief='groove')
        self.tme3.place(x=300, y=215, width=140, height=50)

        self.btn4 = tk.Button(window, text='Copy!!', command=self.func4)
        self.btn4.place(x=30, y=275, width=70, height=50)
        self.qst4 = tk.Label(
            window, text=self.select4[0], borderwidth=2, relief='groove')
        self.qst4.place(x=107, y=275, width=190, height=50)
        self.tme4 = tk.Label(
            window, text=self.select4[1], borderwidth=2, relief='groove')
        self.tme4.place(x=300, y=275, width=140, height=50)

        self.btn5 = tk.Button(window, text='Copy!!', command=self.func5)
        self.btn5.place(x=30, y=335, width=70, height=50)
        self.qst5 = tk.Label(
            window, text=self.select5[0], borderwidth=2, relief='groove')
        self.qst5.place(x=107, y=335, width=190, height=50)
        self.tme5 = tk.Label(
            window, text=self.select5[1], borderwidth=2, relief='groove')
        self.tme5.place(x=300, y=335, width=140, height=50)

        self.btn6 = tk.Button(window, text='Copy!!', command=self.func6)
        self.btn6.place(x=30, y=395, width=70, height=50)
        self.qst6 = tk.Label(
            window, text=self.select6[0], borderwidth=2, relief='groove')
        self.qst6.place(x=107, y=395, width=190, height=50)
        self.tme6 = tk.Label(
            window, text=self.select6[1], borderwidth=2, relief='groove')
        self.tme6.place(x=300, y=395, width=140, height=50)

        self.btn7 = tk.Button(window, text='Copy!!', command=self.func7)
        self.btn7.place(x=30, y=455, width=70, height=50)
        self.qst7 = tk.Label(
            window, text=self.select7[0], borderwidth=2, relief='groove')
        self.qst7.place(x=107, y=455, width=190, height=50)
        self.tme7 = tk.Label(
            window, text=self.select7[1], borderwidth=2, relief='groove')
        self.tme7.place(x=300, y=455, width=140, height=50)

        self.btn8 = tk.Button(window, text='Copy!!', command=self.func8)
        self.btn8.place(x=30, y=515, width=70, height=50)
        self.qst8 = tk.Label(
            window, text=self.select8[0], borderwidth=2, relief='groove')
        self.qst8.place(x=107, y=515, width=190, height=50)
        self.tme8 = tk.Label(
            window, text=self.select8[1], borderwidth=2, relief='groove')
        self.tme8.place(x=300, y=515, width=140, height=50)

        window.mainloop()

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////


main()
