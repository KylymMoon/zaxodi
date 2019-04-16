from tkinter import *
from tkinter import messagebox
import pickle
import tkinter as tk
from tkinter import ttk
import sqlite3


root = Tk()
root.geometry("220x150")
root.title("Войти в систему!")
 
a = "1"
b = "1"

conn = sqlite3.connect("meb.db")
c=conn.cursor()
c.execute(
     '''CREATE TABLE  IF NOT EXISTS meb(id integer primary key, name text, _sum real, rz real , fr text , os text)''')
conn.commit()

def _registr():
     
     _rego = Tk()
     _rego.geometry("1000x500")
     _rego.title("Рабочее место!")

     _topframe = Frame(_rego,bg="#d7d8e0",bd=3)
     
     tree=ttk.Treeview(_rego,columns=("id","name","_sum","rz","os","fr"),height=20,show="headings")
     tree.column("id",width=5,anchor=tk.CENTER)
     tree.column("name",width=165,anchor=tk.CENTER)
     tree.column("_sum",width=150,anchor=tk.CENTER)
     tree.column("rz",width=150,anchor=tk.CENTER)
     tree.column("os",width=220,anchor=tk.CENTER)
     tree.column("fr",width=110,anchor=tk.CENTER)


     tree.heading("id", text="N")
     tree.heading("name", text="Наименование")
     tree.heading("_sum", text="цена")
     tree.heading("rz", text="количество")
     tree.heading("os", text="производитель")
     tree.heading("fr", text="материал")
     
     btn_open_dob = Button(_topframe,text="Добавить",command=lambda:open_dob(),bd=1)
     
     _topframe.pack(side=TOP,fill=tk.X)
     btn_open_dob.pack(side=tk.TOP,anchor="w")
     tree.pack(fill=tk.X)


     _rego.resizable(False,False)
     
def records(name,_sum,rz,fr):
          db.insert_data(name,_sum,rz,fr)
          view_records()
          
def view_records():
          db.c.execute('''SELECT * FROM meb''')
          [tree.delete(i) for i in tree.get_children()]
          [tree.insert('', 'end', values=row) for row in db.c.fetchall()]
          
def open_dob():
     _dob_av = Tk()
     _dob_av.geometry("350x250")
     _dob_av.title("Добавить")
     


     label_desk1 = ttk.Label(_dob_av,text="Наименование")
     label_desk1.place(x=30,y=30)
     label_sel = ttk.Label(_dob_av,text="цена розничная")
     label_sel.place(x=30,y=60)
     label_sum = ttk.Label(_dob_av,text="количество")
     label_sum.place(x=30,y=90)
     label_sum1 = ttk.Label(_dob_av,text="производитель")
     label_sum1.place(x=30,y=120)
     label_sum2 = ttk.Label(_dob_av,text="материал")
     label_sum2.place(x=30,y=150)

     
     endesk = ttk.Entry(_dob_av)
     endesk.place(x=180,y=30)
     enros = ttk.Entry(_dob_av)
     enros.place(x=180,y=60)
     enost = ttk.Entry(_dob_av)
     enost.place(x=180,y=90)
     enmon = ttk.Entry(_dob_av)
     enmon.place(x=180,y=150)
     combox = ttk.Combobox(_dob_av, values=["Италья", "Кыргызстан","Россия"])
     combox.current(0)
     combox.place(x=180,y=120)

     btn_can = ttk.Button(_dob_av,text="Закрыть")
     btn_dob = ttk.Button(_dob_av,text="Добавить",command=lambda:open_dob())
     
     btn_can.place(x=170,y=200)
     btn_dob.place(x=245,y=200)
     btn_dob.bind("<Button-1>",lambda event:ins_data(endesk.get(), enros.get(), enmon.get(), enost.get()))
                  
     _dob_av.resizable(False,False)
#ewqeqe

 
def ins_data(name,_sum,rz,fr):
     c.execute('''INSERT INTO meb(name,suma,rz,fr) VALUES (?, ?, ?, ?)''',(name,_sum,rz,fr))
     conn.commit()
     conn.close()
          
               
def login():
     text_enter_login = Label(root,text="Ведите логин")
     enter_login = Entry()
     text_enter_pass = Label(root,text="Ведите пароль")
     enter_pass = Entry(show="*")
     button_enter = Button(root,text="ВОЙТИ!", command=lambda: log_pass())

     
     text_enter_login.pack()
     enter_login.pack(expand=1)
     text_enter_pass.pack()
     enter_pass.pack(expand=1)
     button_enter.pack(expand=1)


     def log_pass():
               if enter_pass.get() and enter_login.get() == a and b:
                    _registr()
                    return
               else:
                    messagebox.showerror("ошибка","неверный пароль")
                    
root.resizable(False,False)
root.grab_set()
root.focus_set()

login()
root.mainloop()











