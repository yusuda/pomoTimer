#! /usr/bin/env python
# coding: utf-8

import time
import tkinter as tk
from tkinter import messagebox

# ルート
root = tk.Tk()
root.title('Simple Pomodoro Timer 1.0')
root.geometry('400x200')

# 時刻情報の処理
def start_timer():
    try:
        hh = int(entry_hh.get())
        mm = int(entry_mm.get())
        ss = int(entry_ss.get())
    except ValueError:
        messagebox.showerror(u'Error', u'invalid values: hour, minute and second must be integers.')
    else:
        time_total = hh * 3600 + mm * 60 + ss
        # while time_total > 0:
        #     time.sleep(1)
        #     time_total = time_total - 1
        #     time_rem_hh = '{0:02d}'.format(time_total // 3600)
        #     time_rem_mm = '{0:02d}'.format(time_total % 3600 // 60)
        #     time_rem_ss = '{0:02d}'.format(time_total % 60)
        #     var.set('{}:{}:{}'.format(time_rem_hh, time_rem_mm, time_rem_ss))
        time_str.set(str(time_total))

def pause_timer():
    return "hoge"


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
button_start = tk.Button(frame_button, text='start', command=start_timer)
button_start.pack(side='left')
button_pause = tk.Button(frame_button, text='pause', command=pause_timer)
button_pause.pack(side='left')

# 時間の取得
time_str = tk.StringVar()
if time_str.get() != '':
    time_int = int(time_str.get())
var = tk.StringVar()

# 時間の表示
frame_ind = tk.Frame(root)
frame_ind.pack()
label_ind = tk.Label(frame_ind, textvariable=var, font=('Helvetica', 100, 'bold'))
label_ind.pack()

# カウントダウン
try:
    while time_int > 0:
        time.sleep(1)
        time_int = time_int - 1
        time_rem_hh = str(time_int) // 3600
        time_rem_mm = str(time_int) % 3600 // 60
        time_rem_ss = str(time_int) % 60
        var.set('{}:{}:{}'.format(time_rem_hh, time_rem_mm, time_rem_ss))
except NameError:
    pass

# やること
# 適当に入れた時間からトータルで時分秒表示にする -> ok
# カウントダウン
# 減っていく時間をラベルで表示 -> ラベルの表示の自動更新
# ポーズボタン

root.mainloop()
