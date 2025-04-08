import tkinter
import tkinter.messagebox

class NameAddress:
    def __init__(self):
        self.window = tkinter.Tk()

        self.button = tkinter.Button(self.window, text='show data', command=self.reveal)

        self.button.pack()

        tkinter.mainloop()

    def reveal(self):
        tkinter.messagebox.showinfo('data','Micheal Scott, 1725 Slough Avenue, Scranton, Pennsylvania')
if __name__ == '__main__':
    nameaddress = NameAddress()
#ethan collins 4/8/2025 i didn't want to put my actual address so dunder mifflin it is