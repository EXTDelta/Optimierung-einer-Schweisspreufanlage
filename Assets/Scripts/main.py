#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk

from Package.StartScreen import StartScreen  # imports of other files of the package
from Package.OptionsScreen import OptionsScreen
from Package.ReallySwitch import ReallySwitch
from Package.NewTestScreen_01 import NewTestScreen_01
from Package.NewTestScreen_02 import NewTestScreen_02
from Package.NewTestScreen_03 import NewTestScreen_03
from Package.NewTestScreen_04 import NewTestScreen_04
from Package.JsonFunctions import json_writer

# Shared variables----------------------------------------
from Package.sharedVar import window_geometry, name_of_app, \
    start_window, GetStartupVariables, GetPersonalVariables, GetItemVariables, \
    appearance_mode  # import of shared variables located in the sharedVar file


class App(ctk.CTk):  # main window class, every other window class is called from here
    def __init__(self, title):  # title is given as an attribute from the class call
        # main initialization----------------------------------------
        super().__init__()
        ctk.set_appearance_mode(appearance_mode[0])
        ctk.set_default_color_theme("blue")
        self.title(title)
        self.geometry(f"{window_geometry[0]}x{window_geometry[1]}")
        self.resizable(False, False)

        # windows----------------------------------------
        self.startscreen = StartScreen(self)  # ID = 0      other classes
        self.newtestscreen01 = NewTestScreen_01(self)  # ID = 1.0
        self.newtestscreen02 = NewTestScreen_02(self)  # ID = 1.1
        self.newtestscreen03 = NewTestScreen_03(self)  # ID = 1.2
        self.newtestscreen04 = NewTestScreen_04(self)  # ID = 1.3
        self.optionsscreen = OptionsScreen(self)  # ID = 2

        # top level windows----------------------------------------
        self.reallyswitch = None

        # show start screen initially----------------------------------------
        self.switch_window(start_window)

        # run the app----------------------------------------
        self.mainloop()  # the main App window is run (mainloop)

    def open_top_level_window_really_switch(self, which):  # method for creating or focusing the top level window
        # "which" is an attribute given by the back button which calls this function
        if self.reallyswitch is None or not self.reallyswitch.winfo_exists():  # checking if the window exists
            self.reallyswitch = ReallySwitch(self, which)  # the top level window class from the other file is called
        else:
            self.reallyswitch.focus()  # focus the window if it exists

    def switch_window(self, which):  # method for switching windows with the attribute "which"
        if which == "0":
            self.startscreen.place(x=5, y=5)  # the wanted window is placed and all others are deleted from the window
            self.optionsscreen.place_forget()
            self.newtestscreen01.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
        elif which == "1.0":
            self.newtestscreen01.place(x=5, y=5)
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
        elif which == "1.1":
            self.newtestscreen02.place(x=5, y=5)
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
        elif which == "1.2":
            self.newtestscreen03.place(x=5, y=5)
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen04.place_forget()
        elif which == "1.3":
            self.newtestscreen04.place(x=5, y=5)
            self.newtestscreen03.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
        elif which == "2":
            self.optionsscreen.place(x=5, y=5)
            self.startscreen.place_forget()
            self.newtestscreen01.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()

    # Function for changing appearance mode----------------------------------------
    def appearance_mode_switch(self, mode):  # method for switching the appearance mode to dark/light mode
        ctk.set_appearance_mode(mode)  # the attribute "mode" is given by the menu widget in the OptionsScreen class
        if mode == "light":
            json_writer("startup_var", "appearance_mode", ["light", "dark"], "../Other/")

        elif mode == "dark":
            json_writer("startup_var", "appearance_mode", ["dark", "light"], "../Other/")

    def window_size_switch(self, size):
        print("Neustart für Änderung erforderlich")
        if size == "HD - 1280x720":
            json_writer("startup_var", "window_geometry", [1280, 720], "../Other/")
            json_writer("startup_var", "window_size", ["HD - 1280x720", "FullHD - 1920x1080"], "../Other/")

        elif size == "FullHD - 1920x1080":
            json_writer("startup_var", "window_geometry", [1920, 1080], "../Other/")
            json_writer("startup_var", "window_size", ["FullHD - 1920x1080", "HD - 1280x720"], "../Other/")


if __name__ == "__main__":  # when the file this is in is called main then it is run
    GetStartupVariables()  # run GetStartupVariables from sharedVar
    GetPersonalVariables()  # run GetPersonalVariables from sharedVar
    GetItemVariables()  # run GetItemVariables from sharedVar
    App(name_of_app)  # calls the App class and passes the sharedVar name_of_app as the attribute "title"
