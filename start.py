import sys

import sentiment
import nbc

from tkinter import filedialog
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

except ImportError:
    import tkinter.ttk as ttk

#import home.py.tcl_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    #home.py.tcl_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    #home.py.tcl_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

def bow():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if (root.filename != ""):
        sentiment.func(root.filename)

def nb():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if (root.filename != ""):
        nbc.func(root.filename)

'''def svms():
    svm.create_svm(root)
'''
class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Segoe UI} -size 23 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("New Toplevel 1")
        top.configure(background="#bbeff7")
        top.configure(highlightbackground="#00ff00")
        top.configure(highlightcolor="#00ff00")



        self.SENTIMENT_ANALYSIS = Message(top)
        self.SENTIMENT_ANALYSIS.place(relx=0.02, rely=0.04, relheight=0.22
                , relwidth=0.96)
        self.SENTIMENT_ANALYSIS.configure(background="#2e720a")
        self.SENTIMENT_ANALYSIS.configure(font=font11)
        self.SENTIMENT_ANALYSIS.configure(foreground="#000000")
        self.SENTIMENT_ANALYSIS.configure(highlightbackground="#d9d9d9")
        self.SENTIMENT_ANALYSIS.configure(highlightcolor="black")
        self.SENTIMENT_ANALYSIS.configure(text='''SENTIMENT ANALYSIS''')
        self.SENTIMENT_ANALYSIS.configure(width=576)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.37, rely=0.36, height=53, width=156)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Bag of words''')
        self.Button1.configure(command=bow)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.1, rely=0.71, height=43, width=136)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Naive Bayes''')
        self.Button2.configure(command=nb)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.53, rely=0.71, height=53, width=196)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#0000ff")
        self.Button3.configure(highlightbackground="#00ff40")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Support vector machine''')
#        self.Button3.configure(command=svms)

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()


