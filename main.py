import tkinter
from tkinter import *
from tkinter import ttk
import text
import time


def start_countdown():
    showingtext()
    type_text.focus_set()
    global countdown_time
    if time_cb.get() == '1min':
        countdown_time = 5
    if time_cb.get() == '5min':
        countdown_time = 60 * 5
    if time_cb.get() == '10min':
        countdown_time = 60 * 10
    countdown(countdown_time)


def countdown(count):
    if count >= 0:
        mins, secs = divmod(count, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        countdown_label.config(text=time_format)
        countdown_label.after(1000, countdown, count - 1)
    else:
        countdown_label.config(text="Times up!")
        check_result()


def check_result():
    global type_t
    type_t = type_text.get('1.0', tkinter.END)
    type_t_list = type_t.split(' ')
    type_t_list[len(type_t_list) - 1] = type_t_list[len(type_t_list) - 1].replace('\n', '')
    org_t_list = org_t.split(' ')
    result_list = [i2 for i1, i2 in zip(org_t_list, type_t_list) if i1 == i2]
    print(f'Correct words: {len(result_list)}/{len(org_t_list)}')


def showingtext():
    global org_t
    if difficulty_cb.get() == 'Easy':
        org_text.insert(tkinter.END, text.easy)
    if difficulty_cb.get() == 'Medium':
        org_text.insert(tkinter.END, text.medium)
    if difficulty_cb.get() == 'Hard':
        org_text.insert(tkinter.END, text.hard)
    org_t = org_text.get('1.0', tkinter.END)
    org_text.config(state=tkinter.DISABLED)


root = Tk()

countdown_time = 0
org_t = ''
type_t = ''
canvas = Canvas(master=root)
canvas.pack()

option_frame = Frame(canvas)
option_frame.pack()

difficulty_label = Label(text='Select difficulty: ', master=option_frame)
difficulty_label.grid(column=0, row=0)

difficulty_value = ['Easy', 'Medium', 'Hard']
difficulty_cb = ttk.Combobox(option_frame, values=difficulty_value, state='readonly')
difficulty_cb.grid(column=1, row=0)

time_label = Label(master=option_frame, text='Time: ')
time_label.grid(column=2, row=0)

time_value = ['1min', '5min', '10min']
time_cb = ttk.Combobox(option_frame, values=time_value, state='readonly')
time_cb.grid(column=3, row=0)

butt = Button(master=canvas, text='show text', command=start_countdown)
butt.pack()

typing_frame = Frame(canvas)
typing_frame.pack()

countdown_label = Label(typing_frame, text='', font=('Arial', 30, 'bold'))
countdown_label.pack()

org_text = Text(typing_frame)
org_text.pack(side='left')

type_text = Text(typing_frame)
type_text.pack(side='right')

root.mainloop()
