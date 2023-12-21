from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0
 #Питання №1
    if v1.get() == 1 and v2.get() == 0 and v3.get() == 1 and v4.get() == 1:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 1 and v4.get() == 0:
        mark += 1
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 1:
        mark += 1
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 0.25
#Питання № 2
    if v5.get() == 2:
        mark += 2
#Питання № 3
    if v7.get() == 1:
        mark += 2
#Питання № 4
    if entry.get() == 'Передача':
        mark += 2
#Питання 5
    if cb.get() == '<a href="url">посилання</a>':
        mark +=2
#Питання 6
    if scale.get() == 1991:
        mark += 2
    if mark > 6:
        lbl5["fg"] = "green"
    else:
        lbl5["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))

tk = Tk()



tk.title("Тест з інформатики")
font_title = ("Montserrat", 11, "bold")
font_q = ("Montserrat", 10, "italic")

window = tk
window.config(bg='#E6E6FA',
              cursor="heart",
              highlightcolor='#9370DB',
              highlightthickness=1)

#Питання №1
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl2 = Label(tk, text="Які з наведених нижче є прикладами програмного забезпечення?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Microsoft Word", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Відеокарта", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Google Chrome", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Python", variable=v4, onvalue=1, offvalue=0)
#Питання №2
lbl3 = Label(tk, text="Питання №2", font=font_title)
lbl4 = Label(tk, text="Виберіть тип змінних, який вказує на числа з плаваючою комою.", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Integer", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Float", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Claus", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="String", variable=v5, value=4)
#Питання №3
lbl6 = Label(tk, text="Питання №3", font=font_title)
lbl7 = Label(tk, text="Виберіть всі твердження, які є правдивими для реляційної бази даних.", font=font_q)
v7 = IntVar()
rbt5 = Radiobutton(tk, text="Дані організовані у вигляді таблиць.", variable=v7, value=1)
rbt6 = Radiobutton(tk, text="Може містити лише текстову інформацію.", variable=v7, value=2)
rbt7 = Radiobutton(tk, text="Використовується для створення графічних зображень.", variable=v7, value=3)
#Питання №4
lbl8 = Label(tk, text="Питання №4", font=font_title)
lbl9 = Label(tk, text="Вкажіть термін, що описує процес передачі даних між комп'ютерами через Інтернет.", font=font_q)
entry = Entry(tk, width = 30, font = "ubuntu 14",  bd=5,)
#Питання №5
lbl10 = Label(tk, text="Питання №5", font=font_title)
lbl11 = Label(tk, text="Оберіть HTML-тег для створення посилання на іншу веб-сторінку.", font=font_q)
text_variante=('<a href="url">посилання</a>' ,
               '<d href="url">посилання</d>',
               '<div href="url">посилання</div>',
               'floagt = href =посилання')

cb=Combobox(tk, values=text_variante)
#Питання №6
lbl12 = Label(tk, text="Питання №6", font=font_title)
lbl13= Label(tk, text="Якого року було створено мову праграмування Python?", font=font_q)
scale = Scale(tk, orient=HORIZONTAL, length=300, from_=1990, to = 2000, tickinterval=5,
               resolution=1)

btn = Button(tk, text="Відповісти", command=btn_click, font=font_q)
v6 = StringVar()
lbl5 = Label(tk, text='', textvariable=v6, font=font_title)

lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()
lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()
lbl6.pack()
lbl7.pack()
rbt5.pack()
rbt6.pack()
rbt7.pack()
lbl8.pack()
lbl9.pack()
entry.pack()
lbl10.pack()
lbl11.pack()
cb.pack()
lbl12.pack()
lbl13.pack()
scale.pack()
btn.pack()
lbl5.pack()
tk.mainloop()

