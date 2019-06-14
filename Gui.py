# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:53:23 2019

@author: preetham
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk

root = Tk()
C = Canvas(root, bg="blue", height=300, width=300)
filename = ImageTk.PhotoImage(file = "C:\\Users\\preetham\\Downloads\\arai.jpg")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



class cmf:
    def browsecomf(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Csv Files","*.csv" )])
        #return filename
    def run(self):
        from Ride_comfort import Ride
        Ride.Run(self.filename)

class life:
    def browslife(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Csv Files","*.csv" )])
    def pl(self):
        from Life_cycle import Life
        Life.pl(self.filename)

class dur:
    def browsdur(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Csv Files","*.csv" )])
    def du(self):
        from Durability import dura
        dura.d(self.filename)
        
l=life()
g=cmf()  
d=dur()
browsecom = Button(root,width=20,background='blue',foreground='white', text="Comfortness File", command=g.browsecomf)
browsecom.pack()
runbutton=Button(root,width=15,background='blue',foreground='white',text="Run",command=g.run)
runbutton.pack()

browselif= Button(root, width=20,background='blue',foreground='white', text="Life_cycle File", command=l.browslife)
browselif.pack()
plotpy=Button(root, width=15,background='blue',foreground='white', text="Life_cycle Graph", command=l.pl)
plotpy.pack()

browsedura= Button(root, width=20,background='blue',foreground='white', text="Durablity File", command=d.browsdur)
browsedura.pack()
plotdu=Button(root, width=15,background='blue',foreground='white', text="Durability Graph", command=d.du)
plotdu.pack()


pathlabel = Label(root)
C.pack()
pathlabel.pack()
root.mainloop()

#print(filename)
#pathlabel.config(text=filename)