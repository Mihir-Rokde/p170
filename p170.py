from tkinter import*
root=Tk()
root.title("Grade Calculator")
root.geometry("600x600")
pg3l=Label(root)
pg5l=Label(root)
pg10l=Label(root)
class grade3():
    def __init__(self,language_arts,maths):
        self.language_arts=language_arts
        self.maths=maths
    def percentage(self):
        tm=self.language_arts+self.maths
        tmw100=tm*100
        g3p=tmw100/200
        pg3l["text"]=g3p
class grade5():
    def __init__(self,language_arts,maths,ss):
        self.language_arts=language_arts
        self.maths=maths
        self.ss=ss
    def percentage(self):
        tm=self.language_arts+self.maths+self.ss
        tmw100=tm*100
        g5p=tmw100/300
        pg5l["text"]=g5p
class grade10():
    def __init__(self,language_arts,maths,ss,fl):
        self.language_arts=language_arts
        self.maths=maths
        self.ss=ss
        self.fl=fl
    def percentage(self):
        tm=self.language_arts+self.maths+self.ss+self.fl
        tmw100=tm*100
        g10p=tmw100/400
        pg10l["text"]=g10p
og3=grade3(40,50)
g3b=Button(root,text="grade 3",command=og3.percentage)
g3b.pack(padx=20,pady=20)
pg3l.pack(padx=20,pady=20)

og5=grade5(40,50,80)
g5b=Button(root,text="grade 5",command=og5.percentage)
g5b.pack(padx=20,pady=20)
pg5l.pack(padx=20,pady=20)

og10=grade10(40,50,80,70)
g10b=Button(root,text="grade 10",command=og10.percentage)
g10b.pack(padx=20,pady=20)
pg10l.pack(padx=20,pady=20)

root.mainloop()