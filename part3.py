import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
                    
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description','nsum','rz', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=20, anchor=tk.CENTER)
        self.tree.column('description', width=265, anchor=tk.CENTER)
        self.tree.column('nsum',width=150,anchor=tk.CENTER)
        self.tree.column('rz',width=150,anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('nsum', text='Цена')
        self.tree.heading('rz', text='Количество')
        self.tree.heading('costs', text='Производитель')
        self.tree.heading('total', text='Материал')

        self.tree.pack()

    def records(self, description, nsum, rz, costs, total):
        self.db.insert_data(description, nsum, rz, costs, total)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM meb''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=20)
        label_sel = ttk.Label(self,text='Цена')
        label_sel.place(x=50,y=50)
        label_sum = ttk.Label(self,text='количество')
        label_sum.place(x=50,y=80)
        label_select = tk.Label(self, text='Производитель')
        label_select.place(x=50, y=110)
        label_sum = tk.Label(self, text='Материал')
        label_sum.place(x=50, y=140)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=20)
        
        self.entry_kol = ttk.Entry(self)
        self.entry_kol.place(x=200, y=50)
        
        self.entry_mat = ttk.Entry(self)
        self.entry_mat.place(x=200, y=140)
        
        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=80)

        self.made = ttk.Entry(self)
        self.made.place(x=200, y=110)



        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                  self.entry_kol.get(),
                                                                  self.entry_mat.get(),
                                                                  self.entry_money.get(),
                                                                  self.made.get()))

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('meb.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS meb(id integer primary key, description text, nsum text, rz text, costs text, total real)''')
        self.conn.commit()

    def insert_data(self, description, nsum, rz, costs, total):
        self.c.execute('''INSERT INTO meb(description, nsum, rz, costs, total) VALUES (?, ?, ?, ?, ?)''',
                       (description, nsum, rz, costs, total))
        self.conn.commit()


if __name__ == "__main__":
     root = tk.Tk()
     db = DB()
     app = Main(root)
     app.pack()
     root.title("Household finance")
     root.geometry("840x450+300+200")
     root.resizable(False, False)
     root.mainloop()
