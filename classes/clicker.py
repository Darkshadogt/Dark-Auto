import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from classes.GUI import *
import pyautogui

#Inherits all the properties of the GUI including the inputs from user
class AutoClicker(Interface):
    
    def start_clicking(self):
            #Setting a counter if the user is planning to repeat a certain times
            counter = 0
            seconds = self.total_seconds()
            repeats = int(self.total_click_repeat())
            x_coor = int(self.xcoordinate())
            y_coor = int(self.ycoordinate())
            #If its follow mouse, this runs
            if self.mousewhere() == "0":
                #Making sure the repeats aren't blank
                if self.clickrepeat_type() == "0" and repeats != 0:
                    while counter < repeats:
                        #Stops the execution
                        if self.on == False:
                            return
                        if self.click_type() == "Single":
                            if self.mouse_button() == "Middle":
                                #Pausing by the interval, using this instead of time.sleep() because it can be stopped midprocess
                                self.stop.wait(seconds)
                                pyautogui.middleClick()
                                counter += 1
                            else:
                                self.stop.wait(seconds)
                                pyautogui.click(button=(self.mouse_button().lower()))
                                counter += 1
                        elif self.click_type() == "Double":
                            self.stop.wait(seconds)
                            pyautogui.doubleClick(button=(self.mouse_button().lower()))
                            counter += 1
                    
                    #Resetting the counter to 0
                    counter = 0
                    
                    #Stopping the auto clicker once the number of repeats is reached
                    self.on = False
            
                elif self.clickrepeat_type() == "1":
                    while self.on == True:
                        if self.click_type() == "Single":
                            if self.mouse_button() == "Middle":
                                #Pausing by the interval
                                self.stop.wait(seconds)
                                pyautogui.middleClick()
                            else:
                                self.stop.wait(seconds)
                                pyautogui.click(button=(self.mouse_button().lower()))
                        elif self.click_type() == "Double":
                            self.stop.wait(seconds)
                            pyautogui.doubleClick(button=(self.mouse_button().lower()))
            #If its coordinate, this runs
            elif self.mousewhere() == "1":
                if self.clickrepeat_type() == "0" and repeats != 0:
                    while counter < repeats:
                        if self.on == False:
                            break
                        if self.click_type() == "Single":
                            if self.mouse_button() == "Middle":
                                #Pausing by the interval
                                self.stop.wait(seconds)
                                pyautogui.middleClick(x=x_coor, y=y_coor)
                                counter += 1
                            else:
                                self.stop.wait(seconds)
                                pyautogui.click(button=(self.mouse_button().lower()), x=x_coor, y=y_coor)
                                counter += 1
                        elif self.click_type() == "Double":
                            self.stop.wait(seconds)
                            pyautogui.doubleClick(button=(self.mouse_button().lower()), x=x_coor, y=y_coor)
                            counter += 1
                    
                    #Resetting the counter to 0
                    counter = 0
                    
                    #Stopping the auto clicker once the number of repeats is reached
                    self.on = False
            
                elif self.clickrepeat_type() == "1":
                    while self.on == True:
                        if self.click_type() == "Single":
                            if self.mouse_button() == "Middle":
                                #Pausing by the interval
                                self.stop.wait(seconds)
                                pyautogui.middleClick(x=x_coor, y=y_coor)
                            else:
                                self.stop.wait(seconds)
                                pyautogui.click(button=(self.mouse_button().lower()), x=x_coor, y=y_coor)
                        elif self.click_type() == "Double":
                            self.stop.wait(seconds)
                            pyautogui.doubleClick(button=(self.mouse_button().lower()), x=x_coor, y=y_coor)
