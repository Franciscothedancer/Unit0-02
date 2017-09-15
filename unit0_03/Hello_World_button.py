# Created by: Francisco Lee
# Created on : 14-sep-2017
# Created for: ICS3U
# Daily assignment-Unit0-03
#This program displays Hello World but in GUI and button.

import ui

def hello_world_touch_up_inside(sender):
	#print("Hello,World!")
	view['hello_world_label'].text = ("Hello, World!")


v = ui.load_view()
v.present('sheet')
