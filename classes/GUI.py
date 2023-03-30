import tkinter as tk
import pyautogui
import threading
import pynput
import customtkinter as ctk
import tkinter.messagebox as mtk
class Interface:
    def __init__(self):
        self.window = ctk.CTk()
        #Checks whether the auto is running or not
        self.on = False
        #Text variable for hour interval
        self.hour = ctk.StringVar()
        self.hour.trace("w", self.hours)
        #Text variable for minute interval
        self.min = ctk.StringVar()
        self.min.trace("w", self.minutes)
        #Text variable for second interval
        self.sec = ctk.StringVar()
        self.sec.trace("w", self.seconds)
        #Text variable for millisecond interval
        self.milli = ctk.StringVar()
        self.milli.trace("w", self.milliseconds)
        #Text variable for click_position, either follow mouse or coordinate
        self.position = ctk.StringVar()
        self.position.trace("w", self.mousewhere)
        #Text variable for x coordinate
        self.x_coordinate = ctk.StringVar()
        self.x_coordinate.trace("w", self.xcoordinate)
        #Text variable for y coordinate
        self.y_coordinate = ctk.StringVar()
        self.y_coordinate.trace("w", self.ycoordinate)
        #Variable to check the mouse type
        self.mousetype = ctk.StringVar()
        self.mousetype.trace("w", self.mouse_button)
        #Variable to check the click type
        self.clicktype = ctk.StringVar()
        self.clicktype.trace("w", self.click_type)
        #Variable to check if it repeats a certain time or infinite for auto clicker
        self.click_repeat_type = ctk.StringVar()
        self.click_repeat_type.trace("w", self.clickrepeat_type)
        #Variable to check the number of repeats for auto clicker
        self.click_repeats = ctk.StringVar()
        self.click_repeats.trace("w", self.total_click_repeat)
        #Variable for the key the user wants to press
        self.keybutton = ctk.StringVar()
        self.keybutton.trace("w", self.key_button)
        #Variable to check the key type either single or hold
        self.keytype = ctk.StringVar()
        self.keytype.trace("w", self.key_type)
        #Variable to check if it repeats a certain time or infinite for key presser
        self.key_repeat_type = ctk.StringVar()
        self.key_repeat_type.trace("w", self.keyrepeat_type)
        #Variable to check the number of repeats for key presser
        self.key_repeats = ctk.StringVar()
        self.key_repeats.trace("w", self.press_repeat)
        #Variable to check the button that is the auto clicker hotkey
        self.clickerhotkey = ctk.StringVar()
        self.clickerhotkey.trace("w", self.clickhotkey)
        #Varaible to check the button that is the key presser hotkey
        self.presserhotkey = ctk.StringVar()
        self.presserhotkey.trace("w", self.key_hotkey)
        #Variable to check the kind of auto user is using, either auto clicker, or key presser
        self.autokind = ctk.StringVar()
        self.autokind.trace("w", self.type_of_auto)
        self.stop = threading.Event()
        #Types of keys
        self.keys = [' ', '!', '"', '#', '$', '%', '&', "'", '(',
            ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
            'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
            'browserback', 'browserfavorites', 'browserforward', 'browserhome',
            'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
            'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
            'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
            'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
            'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
            'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
            'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
            'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
            'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
            'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
            'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
            'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
            'command', 'option', 'optionleft', 'optionright']
        
    #GUI Settings
    def window_settings(self):
        self.window.title("Dark Auto")
        self.window.geometry("555x370")
        self.window.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.interval()
        self.click_position()
        self.click_setting()
        self.key_setting()
        self.hotkey()
        self.auto_type()

    #Main command
    def main(self):
        self.window_settings()
        self.window.mainloop()
    
    #Listener for auto clicker
    def listen_clicker(self):
        listener = pynput.keyboard.Listener(on_press=self.click_listener)
        listener.start()
    
    #Listener for key presser
    def listen_presser(self):
        listener = pynput.keyboard.Listener(on_press=self.key_listener)
        listener.start()
    
    #Intervals between each click or press
    def interval(self):
        check_time = self.window.register(self.check_time_interval)
        interval_frame = ctk.CTkFrame(self.window, height=70, width=515+30, border_width=2)
        interval_frame.place(x=5, y=5)
        
        hourinterval = ctk.CTkEntry(interval_frame, width=45, textvariable=self.hour, validate="key", validatecommand=(check_time, "%P"), text_color="white")
        hourinterval.place(x=60+15, y=22) 
        hourinterval_label = ctk.CTkLabel(interval_frame, text="Hours: ", text_color="white")
        hourinterval_label.place(x=10+10, y=20) 
        
        mininterval = ctk.CTkEntry(interval_frame, width=45, textvariable=self.min, validate="key", validatecommand=(check_time, "%P"), text_color="white")
        mininterval.place(x=175+15, y=22) 
        mininterval_label = ctk.CTkLabel(interval_frame, text="Minutes: ", text_color="white")
        mininterval_label.place(x=115+15, y=20) 
        
        secinterval = ctk.CTkEntry(interval_frame, width=45, textvariable=self.sec, validate="key", validatecommand=(check_time, "%P"), text_color="white")
        secinterval.place(x=295+15, y=22) 
        secinterval_label = ctk.CTkLabel(interval_frame, text="Seconds: ", text_color="white")
        secinterval_label.place(x=165+65+15, y=20) 

        milli_interval = ctk.CTkEntry(interval_frame, width=45, textvariable=self.milli, validate="key", validatecommand=(check_time, "%P"), text_color="white")
        milli_interval.place(x=440+15, y=22)
        milli_interval_label = ctk.CTkLabel(interval_frame, text= "Milliseconds:", text_color="white")
        milli_interval_label.place(x=290+60+15, y=20)

    #Used to check entry boxes for the intervals
    def check_time_interval(self, time):
        if len(time) == 0:
            return(True)
        if len(time) < 5:
            try:
                if int(time) >= 0:
                    return(True)
            except:
                return(False)
        else:
            return(False)

    #Coordinate settings, either follow mouse or at a certain coordinate
    def click_position(self):
        check_coor = self.window.register(self.check_input)

        position_frame = ctk.CTkFrame(self.window,height=85, width=195, border_width=2)
        position_frame.place(x=5, y=95-15)

        none_button = ctk.CTkRadioButton(self.window, text="Follow Mouse", variable=self.position, value=0, text_color="white")
        none_button.place(x=15, y=112-15)

        coordinate_button = ctk.CTkRadioButton(self.window,variable=self.position, value=1, text="", width=5)
        coordinate_button.place(x=15, y=133)

        #Pick is used for the user to choose where the mouse to click if they don't know the coordinates
        pick = ctk.CTkButton(self.window, text="Pick" ,command=self.bind_locate, width=10, text_color="white")
        pick.place(x=140, y=110-15)

        x_coordinate_label = ctk.CTkLabel(self.window, text= "X:", text_color="white")
        x_coordinate_label.place(x=50-5, y=143-15)

        y_coordinate_label = ctk.CTkLabel(self.window, text="Y:", text_color="white")
        y_coordinate_label.place(x=120, y=143-15)

        x_coordinate = ctk.CTkEntry(self.window, width=50, textvariable=self.x_coordinate, validate="key", validatecommand=(check_coor, "%P"), text_color="white")
        x_coordinate.place(x=70-5, y=145-15)

        y_coordinate = ctk.CTkEntry(self.window, width=50, textvariable=self.y_coordinate, validate="key", validatecommand=(check_coor, "%P"), text_color="white")
        y_coordinate.place(x=140, y=145-15)
        
    #Used to check the entry for the coordinates
    def check_input(self, input):
        if len(input) == 0:
            return(True)
        if len(input) < 5:
            try:
                if int(input) >= 0:
                    return(True)
            except:
                return(False)
        else:
            return(False)
    
    #Settings for auto clicker
    def click_setting(self):
        check_repeat = self.window.register(self.check_input)
        buttonlist = ["Left", "Middle", "Right"]
        typelist = ["Single", "Double"]
        
        setting_frame = ctk.CTkFrame(self.window, height=85, width=325+20, border_width=2)
        setting_frame.place(x=205, y=95-15)
        
        button_word = ctk.CTkLabel(self.window, text="Mouse Button:", width=3, corner_radius=3, text_color="white")
        button_word.place(x=210, y=111-17)
        
        #Setting the default to left clicks
        self.mousetype.set(buttonlist[0])
        
        mouse_button = ctk.CTkOptionMenu(self.window, variable=self.mousetype, values=buttonlist, width=80, text_color="white")
        mouse_button.place(x=303, y=112-17)
       
        click_word = ctk.CTkLabel(self.window, text="Click Type:", text_color="white")
        click_word.place(x=385, y=111-17)
        
        #Setting the clicktype default to single
        self.clicktype.set(typelist[0])
        
        click_type = ctk.CTkOptionMenu(self.window, variable=self.clicktype, values=typelist, width=90, text_color="white")
        click_type.place(x=455, y=112-17)

        repeat_word = ctk.CTkRadioButton(self.window, text="Repeat", variable=self.click_repeat_type, value=0, text_color="white")
        repeat_word.place(x=213, y=145-13)

        repeat_times = ctk.CTkEntry(self.window, width=50, textvariable=self.click_repeats, validate="key", validatecommand=(check_repeat,  "%P"), text_color="white")
        repeat_times.place(x=290, y=145-15)
        
        times_word = ctk.CTkLabel(self.window, text="times", text_color="white")
        times_word.place(x=345, y=143-14)
        
        infinite = ctk.CTkRadioButton(self.window, text="Infinite until Stopped", variable=self.click_repeat_type, value=1, text_color="white")
        infinite.place(x=385, y=145-13)
    
    #Settings for the key presser
    def key_setting(self):
        check_repeat = self.window.register(self.check_input)
        type_frame = ctk.CTkFrame(self.window, height=85, width=360+10, border_width=2)
        type_frame.place(x=5, y=190-20)

        key_button_label = ctk.CTkLabel(self.window, text="Key:", text_color="white")
        key_button_label.place(x=15, y=210-30)
        
        key_button = ctk.CTkOptionMenu(self.window, variable=self.keybutton, values=self.keys, width=150, text_color="white")
        key_button.place(x=45, y=209-27)

        #Setting it to the first key on pyautogui.keyboard_keys list
        self.keybutton.set(self.keys[0])
        
        key_type_label = ctk.CTkLabel(self.window, text="Presser Type:", text_color="white")
        key_type_label.place(x=200, y=210-30)
        
        #Setting the press type default to single
        self.keytype.set("Single")
        

        repeat_word = ctk.CTkRadioButton(self.window, text="Repeat", variable=self.key_repeat_type, value=0, text_color="white")
        repeat_word.place(x=15, y=240-20)
        
        repeat_times = ctk.CTkEntry(self.window, width=50, textvariable=self.key_repeats, validate="key", validatecommand=(check_repeat,  "%P"), text_color="white")
        repeat_times.place(x=90, y=238-20)

        times_word = ctk.CTkLabel(self.window, text="times", text_color="white")
        times_word.place(x=145, y=240-23)
        
        infinite = ctk.CTkRadioButton(self.window, text="Infinite until Stopped", variable=self.key_repeat_type, value=1, text_color="white")
        infinite.place(x=170+25, y=240-19)
        
        key_type = ctk.CTkOptionMenu(self.window, variable=self.keytype, values=["Single", "Hold"], width=4, text_color="white")
        key_type.place(x=290, y=209-27)
    
    #Settings for hotkey
    def hotkey(self):
        hotkey_frame = ctk.CTkFrame(self.window, height=85, width=150+20, border_width=2)
        hotkey_frame.place(x=380, y=170)

        click_label = ctk.CTkLabel(self.window, text="Clicker Hotkey:", text_color="white")
        click_label.place(x=330+65,y=210-30)
        
        click_hotkey = ctk.CTkButton(self.window, textvariable=self.clickerhotkey, command=self.set_clicker_hotkey, width=40, text_color="white")
        click_hotkey.place(x = 420+80, y=209-27)

        key_label = ctk.CTkLabel(self.window, text="Presser Hotkey:", text_color="white")
        key_label.place(x=330+65, y=240-22)
        
        press_hotkey = ctk.CTkButton(self.window, textvariable=self.presserhotkey, command=self.set_presser_hotkey, width=40, text_color="white")
        press_hotkey.place(x=420+80, y=240-20)


    #Settings for the type of auto user is using
    def auto_type(self):
        type_frame = ctk.CTkFrame(self.window, height=45, width=514+30, border_width=2)
        type_frame.place(x=5, y=275-15)

        clicker_type = ctk.CTkRadioButton(self.window, text="Auto Clicker", variable=self.autokind, value=0, text_color="white")
        clicker_type.place(x=120, y=290-15)
        
        key_type = ctk.CTkRadioButton(self.window, text="Key Presser", variable=self.autokind, value=1, text_color="white")
        key_type.place(x=330, y=290-15)

        #Start button for either the auto clicker or key presser
        start_button = ctk.CTkButton(self.window, text="Start", width=540/2, height=50, command=self.turn_on, text_color="white")
        start_button.place(x=5, y=330-15)
        
        #Stop button for either the auto clicker or key presser
        stop_button = ctk.CTkButton(self.window, text="Stop", width=540/2, height=50, command=self.turn_off, text_color="white")
        stop_button.place(x=280, y=330-15)
    
    #Turning auto on
    def turn_on(self):
        self.stop.clear()
        self.on = True
        #Importing the files here, doesn't cause a circular import error
        import os
        import sys

        file_dir = os.path.dirname(__file__)
        sys.path.append(file_dir)
        
        import clicker
        import presser
        
        #Thread for the auto clicker
        autoclicker = threading.Thread(target=clicker.AutoClicker.start_clicking, args=(self,))
        keypresser = threading.Thread(target=presser.KeyPresser.start_pressing, args=(self, ))
        
        if self.type_of_auto() == "":
            mtk.showerror('Error', "Please select a type of Auto")
            self.on = False
        elif self.type_of_auto() == "0":
            if self.mousewhere() == "" or self.clickrepeat_type() == "":
                mtk.showerror("Error", "Please select an Option")
                self.on = False
        elif self.type_of_auto() == "1":
            if self.mousewhere() == "" or self.keyrepeat_type() == "":
                mtk.showerror("Error", "Please select an Option")
                self.on = False
            
        #Resetting the thread
        new_autoclicker = 0
        new_keypresser = 0
        if self.type_of_auto() == "0" and self.on == True:
            try:
                autoclicker.start()
            except RuntimeError:
                #A new thread so the RunTimeError: threads can only be started once wouldn't be caused
                new_autoclicker = threading.Thread(target=clicker.AutoClicker.start_clicking, args=(self,))
                new_autoclicker.start()
        elif self.type_of_auto() == "1":
            try:
                keypresser.start()
            #Can't run same thread more than once 
            except RuntimeError:
                new_keypresser = threading.Thread(target=presser.KeyPresser.start_pressing, args=(self,))
                new_keypresser.start()
        
    #Turning the auto off
    def turn_off(self):
        self.on = False
        
        #Stops the auto from running
        self.stop.set()
    
    #For the user to pick the coordinate location
    def bind_locate(self):
        global pick_popup
        
        #Popup window
        pick_popup = tk.Toplevel(self.window)
        
        width, height = pyautogui.size()
        pick_popup.geometry(f"{width}x{height}")
        pick_popup.resizable(False, False)
        pick_popup.attributes("-alpha", 0.5)
        pick_popup.bind("<Button-1>", self.pick_location)
        #Hides the window
        self.window.withdraw()
    
    #Setting the hotkey for auto clicker
    def set_clicker_hotkey(self):
        global hotkey1
        hotkey1 = self.window.bind("<Key>", self.clicker_hotkey)

    def clicker_hotkey(self, event):
        key = event.char
        self.clickerhotkey.set(key)
        #Removes the bind so the function won't be called after keys pressed by user
        self.window.unbind("<Key>", hotkey1)
        
        #Running the listener on a separate thread
        listener = threading.Thread(target=self.listen_clicker)
        listener.start()
    
    #Setting the hotkey for key presser
    def set_presser_hotkey(self):
        global hotkey2
        hotkey2 = self.window.bind("<Key>", self.presser_hotkey)
    
    def presser_hotkey(self, event):
        key = event.char
        self.presserhotkey.set(key)
        self.window.unbind("<Key>", hotkey2)
        
        #Running the listener on a separate thread
        listener = threading.Thread(target=self.listen_presser)
        listener.start()
    
    #User choose the coordinate location
    def pick_location(self, event):
        self.x_coordinate.set(event.x)
        self.y_coordinate.set(event.y)
        
        #Destroys the popup window after user choosing a point
        pick_popup.destroy()

        #Shows the window again after popup window is destroyed
        self.window.deiconify()

    #Listener for auto clicker
    def click_listener(self, event):
        #Checking if the key matches the hotkey for auto clicker
        if event.char == self.clickhotkey():
            if self.on == False:
                self.turn_on()
            elif self.on == True:
                self.turn_off()

        
    #Listener for key presser
    def key_listener(self, event):
        #Checking if the key matches the hotkey for key presser
        if event.char == self.key_hotkey():
            if self.on == False:
                self.turn_on()
            else:
                self.turn_off()

    
    #Returns the hour interval
    def hours(self, *args):
        if self.hour.get() == "":
            return("0")
        else:
            return(self.hour.get())
    
    #Returns the millisecond interval
    def milliseconds(self, *args):
        if self.milli.get() == "":
            return("0")
        else:
            return(self.milli.get())
    
    #Returns the second interval
    def seconds(self, *args):
        if self.sec.get() == "":
            return("0")
        else:
            return(self.sec.get())
    
    #Returns the minute interval
    def minutes(self, *args):
        if self.min.get() == "":
            return("0")
        else:
            return(self.min.get())

    #Calculates the total interval converted into seconds
    def total_seconds(self):
            total_second = 0
            milli = self.milliseconds()
            sec = self.seconds()
            min = self.minutes()
            hour = self.hours()
            if milli != "0":
                total_second += int(milli) / 1000
            if sec != "0":
                total_second += int(sec)
            if min != "0":
                total_second += (int(min) * 60)
            if hour != "0":
                total_second += (int(hour) * 3600)
            return(total_second)

    #Returns the total number of clicker repeat times
    def total_click_repeat(self, *args):
        if self.click_repeats.get() == "":
            return("0")
        else:
            return(self.click_repeats.get())
    
    #Returns the total number of presser repeat times
    def press_repeat(self, *args):
        if self.key_repeats.get() == "":
            return("0")
        else:
            return(self.key_repeats.get())
    
    #Returns the x coordinate of the user picked location
    def xcoordinate(self, *args):
        if self.x_coordinate.get() == "":
            return("0")
        else:
            return(self.x_coordinate.get())
    
    #Returns the y coordinate of the user picked location
    def ycoordinate(self, *args):
        if self.y_coordinate.get() == "":
            return("0")
        else:
            return(self.y_coordinate.get())
    
    #Returns the key type
    def key_type(self, *args):
        return(self.keytype.get())

    #Returns the key to be pressed by the key presser
    def key_button(self, *args):
        return(self.keybutton.get())
    
    #Returns the hotkey of the auto clicker
    def clickhotkey(self, *args):
        return(self.clickerhotkey.get())

    #Returns the hotkey of the key presser
    def key_hotkey(self, *args):
        return(self.presserhotkey.get())

    #Returns the mouse type
    def mouse_button(self, *args):
        return(self.mousetype.get()) 

    #Returns the click type
    def click_type(self, *args):
        return(self.clicktype.get()) 
    
    #Returns whether follow mouse or coordinate point
    def mousewhere(self, *args):
        return(self.position.get())

    #Returns key repeat type
    def keyrepeat_type(self, *args):
        return(self.key_repeat_type.get())

    #Returns click repeat type
    def clickrepeat_type(self, *args):
        return(self.click_repeat_type.get())
    
    #Returns whether if auto is running
    def on_state(self):
        return(self.on)
    
    #Returns the type of auto
    def type_of_auto(self, *args):
        return(self.autokind.get())