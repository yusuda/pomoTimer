# pomoTimer
A script for training tkinter

## General Information

This script is made for my own training of tkinter / GUI
applications. This application is nothing but a simple timer
application that can countdown from specified time.

## Licences and responsibilities

The author claim nothing about the copyright on the application. You
can edit and redistribute absolutely freely. The original author takes
no charges about troubles on your system or any place triggered by the
original / edited versions.

## Usage

Simply execute on your shell

<code>python /path/to/script/pomotimer.py</code>

and then put the time in hour, minute and second. Each entry can be
omitted if they are zero. You can start countdown by pressing return
key.

On running countdown you can stop it by pressing 'stop' or hitting
return key. Also you can pause it temporarily by pressing 'pause' and
restart by 'resume.'

<table>
<tr>
<th>status</th>
<th>key</th>
<th>behavior</th>
</tr>
<tr>
<td>stop</td>
<td>Return</td>
<td>start</td>
</tr>
<tr>
<td>run</td>
<td>Return</td>
<td>stop</td>
</tr>
<tr>
<td>pause</td>
<td>Return</td>
<td>start from beginning</td>
</tr>
</table>

Note that this script has to be executed on Python 3.x series. Your
system is required to enable the tkinter module other than the minimum
construction.
