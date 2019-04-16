from tkinter import *
from datetime import datetime

root =Tk()
root.title("спунлае")

temp = 0
after_id = ''
#использование библиотеки дататайм 
def tick():
     global temp, after_id
     after_id = root.after(1000, tick)#1000 это скорость тика
     f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")#минута и секунда
     start.configure(text=str(f_temp))
     temp += 1
#функция старт  :)  
def start_sw():
     btn1.grid_forget()
     btn2.grid(row=1, columnspan=2, sticky="ew")
     tick()
#функция стоп)))))       
def stop_sw():
     btn2.grid_forget()
     btn3.grid(row=1,column=0,sticky="ew")
     btn4.grid(row=1,column=1,sticky="ew")
     root.after_cancel(after_id)
#функция продолжить)    
def continue_sw():
     btn3.grid_forget()
     btn4.grid_forget()
     btn2.grid(row=1, columnspan=2,sticky="ew")
     tick()
#функция сброс)      
def reset_sw():
     global temp
     temp = 0
     start.configure(text="00:00")
     btn3.grid_forget()
     btn4.grid_forget()
     btn1.grid(row=1, columnspan=2,sticky="ew")
     

#создание 00 00 шрифт убунту размер100
start = Label(root, width=5 , font=("Ubuntu",100),text="00:00")
start.grid(row=0, columnspan=2)
#создание кнопок и ссылки на функции
btn1= Button(root, text="старт", font=("Ubuntu",30), command=start_sw)
btn2= Button(root, text="стоп", font=("Ubuntu",30), command=stop_sw)
btn3= Button(root, text="продолжить", font=("Ubuntu",30), command=continue_sw)
btn4= Button(root, text="сброс", font=("Ubuntu",30), command=reset_sw)
#отображение кнопки
btn1.grid(row=1, columnspan=2,sticky="ew")
root.mainloop()
#программу разработали Илон Маск и Бийбосунов Кылыбек







