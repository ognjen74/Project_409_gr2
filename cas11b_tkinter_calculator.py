import tkinter as tk
import tkinter.ttk as ttk

def saberi():
    rezultatV.set(float(prviV.get())+float(drugiV.get()))
def oduzmi():
    rezultatV.set(float(prviV.get())-float(drugiV.get()))
def pomnozi():
    rezultatV.set(float(prviV.get())*float(drugiV.get()))
root=tk.Tk()

def podeli():
    rezultatV.set(float(prviV.get())/float(drugiV.get()))
prviV=tk.StringVar()
drugiV=tk.StringVar()
rezultatV=tk.StringVar()
prvibroj=ttk.Entry(root, textvariable=prviV)
drugibroj=ttk.Entry(root, textvariable=drugiV)
rezultat=ttk.Entry(root, textvariable=rezultatV)
labelaPrvi=ttk.Label(root,text="Prvi broj" )
labelaDrugi=ttk.Label(root,text="Drugi broj" )
labelaRezultat=ttk.Label(root,text="Rezultat")
plusButton=ttk.Button(root, text="+", command=saberi)
minusButton=ttk.Button(root, text="-", command=oduzmi)
putaButton=ttk.Button(root, text="*", command=pomnozi)
podeljenoButton=ttk.Button(root, text="/", command=podeli)

prvibroj.grid(row=0, column=4)
drugibroj.grid(row=1, column=4)
rezultat.grid(row=4, column=4)
labelaPrvi.grid(row=0, column=0)
labelaDrugi.grid(row=1, column=0)
labelaRezultat.grid(row=3, column=4)
plusButton.grid(row=3, column=0)
minusButton.grid(row=4, column=0)
putaButton.grid(row=3, column=1)
podeljenoButton.grid(row=4, column=1)

root.mainloop()
