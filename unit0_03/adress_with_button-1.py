# Created by: Francisco Lee
# Created on : 14-sep-2017
# Created for: ICS3U
# Daily assignment-Unit0-03
#This program is the Adress program, but wi a button.

import ui

def show_adress_touch_up_inside(sender):
	#print ('Hello, World!')
	view['name_label'].text = ("Francisco,Lee")
	view['city_label'].text = ("Ottawa")
	view['country_label'].text = ("Canada")

v = ui.load_view()
v.present('sheet')
