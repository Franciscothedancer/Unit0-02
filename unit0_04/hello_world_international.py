# Created by: Francisco Lee
# Created on : 15-sep-2017
# Created for: ICS3U
# Daily assignment-Unit0-04
# This program displays Hello World but in GUI and multiple languages.

import ui

def english_touch_up_imside(sender):
	# displays the English version
	view['hello_world_label'].text=('Hello,World!')
	
		
def french_touch_up_inside(sender):	
 # displays the French version
 view['hello_world_label'].text=('Bonjour le monde!')
		
def spanish_touch_up_inside(sender):
 # displays the Spanish version
 view['hello_world_label'].text=('iHola Mundo!')
			
# note that now the app runs full screen
		
		
view = ui.load_view()
view.present('sheet')
