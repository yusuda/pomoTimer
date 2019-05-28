#! /usr/bin/env python
# coding: utf-8

import time
import tkinter as tk

# ルート
root = tk.Tk()
root.title('Simple Pomodoro Timer 1.0')
root.geometry('360x200')

# 時:分:秒のエントリ
frame_time = tk.Frame(root)
frame_time.pack()
label_hh = tk.Label(frame_time, text=u'hours')
label_hh.pack(side='left')
entry_hh = tk.Entry(frame_time, width=5)
entry_hh.pack(side='left')
label_mm = tk.Label(frame_time, text=u'minutes')
label_mm.pack(side='left')
entry_mm = tk.Entry(frame_time, width=5)
entry_mm.pack(side='left')
label_ss = tk.Label(frame_time, text=u'seconds')
label_ss.pack(side='left')
entry_ss = tk.Entry(frame_time, width=5)
entry_ss.pack(side='left')

# ボタン
frame_button = tk.Frame(root)
frame_button.pack()
button_start = tk.Button(frame_button, text='start')
button_start.pack(side='left')
button_pause = tk.Button(frame_button, text='pause')
button_pause.pack(side='left')


# やること
# 適当に入れた時間からトータルで時分秒表示にする
# カウントダウン
# 減っていく時間をラベルで表示 -> ラベルの表示の自動更新
