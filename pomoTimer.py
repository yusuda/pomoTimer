#! /usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import messagebox
import pygame

# バグ
# カウントダウン中にstopを押すと一瞬最初の数字が出る
# 終了後にresumeを押すと一時停止した位置から再生する

# SEの読み込み
pygame.init()
pygame.mixer.init()
se1 = pygame.mixer.Sound('./se1.wav')

# ルート
root = tk.Tk()
root.title('Simple Pomodoro Timer 1.0')
root.geometry('360x200')

# カウントダウンの処理
def start_timer():
    global status
    if status == 'run':
        status = 'stop'
    else:
        status = 'run'
        var_start.set('stop')
    # button_start.state(['disabled'])

    try:
        hh = int(entry_hh.get())
        mm = int(entry_mm.get())
        ss = int(entry_ss.get())
    except ValueError:
        messagebox.showerror('error', 'values invalid: enter integers.')
    else:
        time_total = hh * 3600 + mm * 60 + ss
        set_time(time_total)


def set_time(time_total):
    hh_new = '{0:02d}'.format(time_total // 3600)
    mm_new = '{0:02d}'.format(time_total % 3600 // 60)
    ss_new = '{0:02d}'.format(time_total % 60)
    timer.set('{}:{}:{}'.format(hh_new, mm_new, ss_new))
    time_total = time_total - 1
    global status
    if time_total > -1 and status == 'run':
        frame_ind.after(1000, set_time, time_total)
    elif status == 'pause':
        global current_time
        current_time = time_total
    elif status == 'stop':
        var_start.set('start')
    else:
        se1.play()
        timer.set('00:00:00')
        var_start.set('start')
        status = 'stop'
        messagebox.showinfo('info', 'time is up')


def pause_timer():
    # if var_pause.get() == 'pause':
    #     var_pause.set('resume')
    # elif var_pause.get() == 'resume':
    #     var_pause.set('pause')

    global status
    if status == 'run':
        status = 'pause'
        var_pause.set('resume')
    elif status == 'pause':
        status = 'run'
        var_pause.set('pause')
        set_time(current_time)
    elif status == 'stop':
        pass


# 時:分:秒のエントリ
frame_time = tk.Frame(root)
frame_time.pack()
label_hh = tk.Label(frame_time, text=u'hours')
label_hh.pack(side='left')
entry_hh = tk.Entry(frame_time, width=5)
entry_hh.insert(tk.END, 0)
entry_hh.pack(side='left')
label_mm = tk.Label(frame_time, text=u'minutes')
label_mm.pack(side='left')
entry_mm = tk.Entry(frame_time, width=5)
entry_mm.insert(tk.END, 0)
entry_mm.pack(side='left')
label_ss = tk.Label(frame_time, text=u'seconds')
label_ss.pack(side='left')
entry_ss = tk.Entry(frame_time, width=5)
entry_ss.insert(tk.END, 0)
entry_ss.pack(side='left')

# ボタン
frame_button = tk.Frame(root)
frame_button.pack()
var_start = tk.StringVar()
var_start.set('start')
var_pause = tk.StringVar()
var_pause.set('pause')
button_start = tk.Button(frame_button, textvariable=var_start, command=start_timer)
button_start.pack(side='left')
button_pause = tk.Button(frame_button, textvariable=var_pause, command=pause_timer)
button_pause.pack(side='left')
root.bind('<Return>', lambda x: start_timer())

# 時間の表示
status = 'stop'
frame_ind = tk.Frame(root)
frame_ind.pack()
timer = tk.StringVar()
label_ind = tk.Label(frame_ind, textvariable=timer, font=('Helvetica', 80, 'bold'))
label_ind.pack()

root.mainloop()
