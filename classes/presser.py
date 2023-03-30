import GUI
import pyautogui

#Inheriting all of GUI's properties
class KeyPresser(GUI.Interface):

    def start_pressing(self):
        #Setting a counter if the user is planning to repeat a certain times
        counter = 0
        seconds = self.total_seconds()
        repeats = int(self.press_repeat())
        #Making sure repeats isn't 0
        if self.keyrepeat_type() == "0" and repeats != 0:
            while counter < repeats:
                #Stops exeuction if user stops the auto clicker
                if self.on == False:
                    return
                if self.key_type() == "Single":
                    self.stop.wait(seconds)
                    pyautogui.press(self.key_button())
                    counter += 1
                elif self.key_type() == "Hold":
                    self.stop.wait(seconds)
                    pyautogui.keyDown(self.key_button())
                    self.stop.wait(seconds)
                    pyautogui.keyUp(self.key_button())
                    counter += 1
            counter = 0
            self.run = False
        elif self.keyrepeat_type() == "1":
            while self.on == True:
                if self.key_type() == "Single":
                    self.stop.wait(seconds)
                    pyautogui.press(self.key_button())
                elif self.key_type() == "Hold":
                    #Keeps holding until user stops it
                    pyautogui.hold(self.key_button())

