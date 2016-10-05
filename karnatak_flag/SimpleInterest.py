import tkinter as tk

def compute():
    p = float(entry1.get())
    r = float(entry2.get())
    t = float(entry3.get())

    result = p*r*t/100
    
    label4['text'] = str(result)
    
def clear():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    
root = tk.Tk()

f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)
f5 = tk.Frame(root)


f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()


label1 = tk.Label(f1,text="Principal")
label1.config(font=('ariel',10,'bold'))
label1.pack(side="left")

entry1 = tk.Entry(f1)
entry1.pack(side="right",padx=10,pady=10)

label2 = tk.Label(f2,text="Rate       ")
label2.config(font=('ariel',10,'bold'))
label2.pack(side="left")

entry2 = tk.Entry(f2)
entry2.pack(side="right",padx=10,pady=10)


label3 = tk.Label(f3,text="Period    ")
label3.config(font=('ariel',10,'bold'))
label3.pack(side="left")

entry3 = tk.Entry(f3)
entry3.pack(side="right",padx=10,pady=10)

label4 = tk.Label(f4,text="Result Here    ")
label4.config(font=('ariel',10,'bold'))

label4.pack(side="left")


button1 = tk.Button(f5,text="Compute",command=compute)
button1.config(font=('ariel',10,'bold'))
button1.pack(side="left",padx=10,pady=10)

button2 = tk.Button(f5,text="Clear",command=clear)
button2.config(font=('ariel',10,'bold'))
button2.pack(side="right",padx=10,pady=10)

entry1.focus_set()
root.mainloop()
