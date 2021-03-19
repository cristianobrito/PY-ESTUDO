#from hospital import Hopistal, Medico
import tkinter

from hospital import Hospital
from medico import Medico
from tkinter import *
hosp = Hospital(nome='', tipo='',especialidade='', avaliacao='')
app = Tk(screenName='principal')

app.geometry('200x100+200+100')
bt_inserir = Button(app, text='Inserir', command=hosp.inserir)
bt_inserir.pack(side='right')
bt_mostrar = Button(app, text='Mostrar', command= hosp.mostrar)
bt_mostrar.pack(side='left')
app.mainloop()





