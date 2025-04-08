import os
import tkinter as tk

root = tk.Tk()
root.title = "Conexiones a SAP"

mainframe = tk.Frame(root)
mainframe.pack()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def myClick1():
    SID1 = os.system('start sapshcut.exe -system="DEH" -client="100" -user="VDMACIASP" -pw="Sysproc2024..."')
    SID1.pack()
def myClick2():
    SID2 = os.system('start NWBC.exe -system="DEH" -client="110" -user="VDMACIASP" -pw="Sysproc.2025"')
    SID2.pack()
def myClick3():
    SID3 = os.system('start sapshcut.exe -system="TEH" -client="400" -user="MAEZEQUIELP" -pw="NoRmEn07."')
    SID3.pack()
def myClick4():
    SID3 = os.system('start sapshcut.exe -system="150" -client="150" -user="ABAP2_EXT" -pw="Consultor2024"')
    SID3.pack()
def myClick5():
    SID3 = os.system('start sapshcut.exe -system="MEQ" -client="300" -user="VMASIAS_EXT" -pw="300...MEDS"')
    SID3.pack()


Frame1 = tk.Frame(mainframe, height=5, width=5, border=2, relief="sunken")
Frame1.pack()
Label1 = tk.Label(Frame1, text="Conexiones ACHS")
Label1.pack()
button1 = tk.Button(Frame1, width=10, text="ACHS DEV", command=myClick1)
button1.pack()
button2 = tk.Button(Frame1, width=10, text="ACHS 110", command=myClick2)
button2.pack()
button3 = tk.Button(Frame1, width=10, text="ACHS QAs", command=myClick3)
button3.pack()

Linea1 = tk.Label(mainframe, text="")
Linea1.pack()

Frame2 = tk.Frame(mainframe, height=5, width=5, border=2, relief="sunken")
Frame2.pack()
Label2 = tk.Label(Frame2, text="Conexiones MEDS")
Label2.pack()
button4 = tk.Button(Frame2, width=10, text="MEDs DEV", command=myClick4)
button4.pack()
button5 = tk.Button(Frame2, width=10, text="MEDs QAs", command=myClick5)
button5.pack()

Linea2 = tk.Label(mainframe, text="")
Linea2.pack()
root.mainloop()