from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='What is your favorite ice cream flavor?')
        self.helloLabel.pack()
        # self.quitButton = Button(self, text='quit', command=self.quit)
        # self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # self.alertButton = Button(self, text='Hello', command=self.hello)
        # self.alertButton.pack()
        self.btOK = Button(self, text='OK', fg='red', command=self.hello)
        self.btCancel = Button(self, text='cancel', bg='yellow', command=self.processCancel)
        self.btOK.pack()
        self.btCancel.pack()

    def processOk(self):
        print('OK button is clicked.')

    def processCancel(self):
        print('cancel button is clicked.')

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'your favorite ice cream is %s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()
