#!/usr/bin/env python

"""Contains an example of midi input, and a separate example of midi output.

By default it runs the output example.
python midi.py --output
python midi.py --input

"""

#this program changes the lighttrix wifi balls with the serato midi controller

import sys
import os

import pygame
import pygame.midi
from pygame.locals import *

from socket import *
import struct

import time

import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()


udp_header = struct.pack("!bIBH", 66, 0, 0, 0)
s = socket(AF_INET, SOCK_DGRAM)



# def print_device_info():
# 	pygame.midi.init()
# 	_print_device_info()
# 	pygame.midi.quit()

# def _print_device_info():
# 	print('print device info')
# 	for i in range( pygame.midi.get_count() ):
# 		r = pygame.midi.get_device_info(i)
# 		(interf, name, input, output, opened) = r

# 		in_out = ""
# 		if input:
# 			in_out = "(input)"
# 		if output:
# 			in_out = "(output)"

# 		print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
# 			   (i, interf, name, opened, in_out))

# #brightness_last_changed = 0
# cur_brightness = 0
# def change_brightness(value):
# 	#global brightness_last_changed
# 	global cur_brightness
# 	#brightness_last_changed = time.time()
# 	cur_brightness = int(value/16)
# 	print('send brightness', cur_brightness)
# 	data = struct.pack("!BB", 0x10, cur_brightness)
# 	for ball_num in active_balls:
# 		s.sendto(udp_header+data, ('192.168.43.'+ball_num, 41412));

# #color_last_changed = 0

# cur_color =	{
#   "red": 0,
#   "green": 0,
#   "blue": 0
# }
# def change_color(color, value):
# 	print('change color', color, value)
# 	#global color_last_changed
# 	global cur_color
# 	#color_last_changed = time.time()
# 	cur_color[color] = value
# 	data = struct.pack("!BBBB", 0x0a, cur_color['red']*2, cur_color['green']*2, cur_color['blue']*2)
# 	for ball_num in active_balls:
# 		print('ball_num',ball_num)
# 		s.sendto(udp_header+data, ('192.168.43.'+ball_num, 41412));



# active_balls = ['23','81']		
# def input_main(device_id = None):
# 	global active_balls
# 	pygame.init()
# 	pygame.fastevent.init()
# 	event_get = pygame.fastevent.get
# 	event_post = pygame.fastevent.post

# 	pygame.midi.init()

# 	_print_device_info()


# 	if device_id is None:
# 		input_id = pygame.midi.get_default_input_id()
# 	else:
# 		input_id = device_id

# 	print ("using input_id :%s:" % input_id)
# 	i = pygame.midi.Input( input_id )

# 	pygame.display.set_mode((1,1))



# 	going = True
# 	while going:
# 		events = event_get()
# 		for e in events:
# 			if e.type in [QUIT]:
# 				going = False
# 			if e.type in [KEYDOWN]:
# 				going = False
# 			if e.type in [pygame.midi.MIDIIN]:
# 				if e.data1 == 7:
# 					change_color('red', e.data2)
# 				if e.data1 == 11:
# 					change_color('green', e.data2)
# 				if e.data1 == 15:
# 					change_color('blue', e.data2)
# 				if e.data1 == 19:
# 					change_brightness(e.data2)
# 				if e.data1 == 27:
# 					print('active_balls 35')
# 					active_balls = ['35']
# 				if e.data1 == 30:
# 					print('active_balls 85')
# 					active_balls =  ['85']
# 				if e.data1 == 32:
# 					print('active_balls 240')
# 					active_balls =  ['240']
# 				if e.data1 == 34:
# 					active_balls = ['35','85','240']
# 				else:
# 					print ("event data",e)
# 			#if e.

# 		if i.poll():
# 			midi_events = i.read(10)
# 			# convert them into pygame events.
# 			midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

# 			for m_e in midi_evs:
# 				event_post( m_e )

# 		# send_color()
# 		# send_brightness()

# 	del i
# 	pygame.midi.quit()



# try:
# 	device_id = int( sys.argv[-1] )
# except:
# 	device_id = None
# print_device_info()
# input_main(device_id)

