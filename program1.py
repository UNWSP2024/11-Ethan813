import tkinter

class saying_gui:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.title('bears beets battlestar galactica')
        self.Label = tkinter.Label(self.window, text = 'bears beets battlestar galactica')
        self.Label.pack()
        tkinter.mainloop()
#ethan collins 4/7/2025 bears and beets
if __name__ == '__main__':
    Saying_GUI = saying_gui()