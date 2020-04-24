from tkinter import *
from tkinter import ttk
import random
from Algorithms import *

root = Tk()
root.title('Algorithm Visualizer')
root.maxsize(1000, 600)
root['bg'] = '#44ebb6'

algo = StringVar()
data = []

def getData(data,colorarray):
    canvas.delete("all")
    cwidth = 680
    cheight = 580
    datawidth = cwidth / (len(data) + 1)
    diffspace = 10
    space = 10
    ndata = [i / max(data) for i in data]
    for i, height in enumerate(ndata):
        x0 = i * datawidth + diffspace+space
        y0 = cheight - height * 540
        x1 = (i + 1) * datawidth + diffspace
        y1 = cheight

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])
        canvas.create_text((x0+2), y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def select():
    global data
    data.clear()
    canvas.delete("all")

    minval = int(minn.get())
    maxval = int(maxx.get())
    sizeval = int(sizelength.get())

    for i in range(sizeval):
        data.append(random.randrange(minval, maxval+1))
    getData(data,['red' for x in range(len(data))])

def startalgo():
    global data
    if algo.get()=="Bubble sort":
        bubblesort(data, getData, speedscale.get())
    elif algo.get()=="Selection sort":
        selectionsort(data, getData, speedscale.get())
    elif algo.get()=="Insertion sort":
        Insertionsort(data, getData, speedscale.get())
    elif algo.get()=="Quick sort":
        quickSort(data,0,len(data)-1,getData,speedscale.get())
    elif algo.get()=="Merge sort":
        mergeSort(data,len(data),data,getData,speedscale.get())


#frame
ui_frame = Frame(root, width = 150, height = 580, bg='grey')
ui_frame.grid(row=0, column=0, padx=5, pady=10)

canvas = Canvas(root, width=680, height=580, bg='white')
canvas.grid(row=0, column=1, padx=5, pady=10)

#ui
Label(ui_frame, text="ALGO: ", bg='grey', fg='white').grid(row=0, column=0, padx=5, pady=10, sticky=W)
Menu=ttk.Combobox(ui_frame, textvariable=algo, values=['Selection sort', 'Bubble sort', 'Quick sort', 'Merge sort', 'Insertion sort'])
Menu.grid(row=0, column=1, padx=5, pady=10)
Menu.current(0)

Button(ui_frame, text="Select Algo", command=select).grid(row=2, column=0, padx=0, pady=0)

sizelength = Scale(ui_frame, from_=3, to=30, length=150, resolution=1, orient=HORIZONTAL, label="Select size")
sizelength.grid(row=3, column=1, padx=5, pady=10)

minn = Scale(ui_frame, from_=0, to=10, length=150, resolution=1, orient=HORIZONTAL, label="Select minimum")
minn.grid(row=4, column=1, padx=5, pady=10)

maxx = Scale(ui_frame, from_=10, to=100, length=150, resolution=1, orient=HORIZONTAL, label="Select maximum")
maxx.grid(row=5, column=1, padx=5, pady=10)

speedscale = Scale(ui_frame, from_=0.1, to=1.6, length=150, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select speed")
speedscale.grid(row=7, column=1, padx=5, pady=10)

Button(ui_frame, text="RUN", command=startalgo).grid(row=9, column=0, padx=5, pady=10)

root.mainloop()