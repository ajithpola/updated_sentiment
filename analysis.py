#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Mar 12, 2018 05:36:24 PM
import sys

import bow_graph_neg
import bow_graph_pos

try:
    from Tkinter import *
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

#import _support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = analysis (root)
 #   _support.init(root, top)
    root.mainloop()

w = None
def create_analysis(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = analysis (w)
  #  _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

def pos():
    bow_graph_pos.graph()
def neg():
    bow_graph_neg.graph()

class analysis:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font14 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
        font16 = "-family Algerian -size 24 -weight normal -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("673x543+650+150")
        top.title("New Toplevel 1")
        top.configure(background="#704ee7")



        self.Message1 = Message(top)
        self.Message1.place(relx=-0.01, rely=0.0, relheight=0.28, relwidth=1.02)
        self.Message1.configure(background="#5aaee0")
        self.Message1.configure(font=font16)
        self.Message1.configure(foreground="#e60f34")
        self.Message1.configure(highlightbackground="#bff2ec")
        self.Message1.configure(highlightcolor="#33c454")
        self.Message1.configure(text='''ANALYSIS''')
        self.Message1.configure(width=686)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.33, rely=0.44, height=63, width=216)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(disabledforeground="#000000")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#000000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''POSITIVE''')
        self.Button1.configure(width=216)
        self.Button1.configure(command=pos)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.33, rely=0.72, height=63, width=216)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#000000")
        self.Button2.configure(highlightcolor="#ffffff")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''NEGATIVE''')
        self.Button2.configure(width=216)
        self.Button2.configure(command=neg)






if __name__ == '__main__':
    vp_start_gui()


