#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Top Level Window Really Switch

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables  # import of shared variables located in the sharedVar file


class ReallySwitch(ctk.CTkToplevel):  # top level window class for checking if you really want to go back
    def __init__(self, parent, which):
        # the attribute "which" is passed on to the widgets and from there to the window switch method in the app class
        super().__init__(parent)
        self.geometry("350x150")
        self.resizable(False, False)
        self.title("!ACHTUNG!")
        self.attributes("-topmost", "true")  # the window is at the top at all times

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=340,
                                          height=20,
                                          corner_radius=5,
                                          text="Wirklich zurück gehen?",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 15))
        self.indicator_bar.place(x=5,
                                 y=5)

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the buttons
                                         width=340,
                                         height=115)
        self.button_frame.place(x=5,
                                y=30)

        # yes button------------------------------------------------------------
        self.yes_button = ctk.CTkButton(master=self.button_frame,
                                        # yes button to continue going back
                                        width=100,
                                        height=50,
                                        corner_radius=10,
                                        text="Ja",
                                        font=("bold", 20),
                                        command=lambda: self.yes_button_function(which))
        # the command call the switch_window method and passes "which" as an argument, then destroys itself
        self.yes_button.place(x=5,
                              y=32.5)

        # no button------------------------------------------------------------
        self.no_button = ctk.CTkButton(master=self.button_frame,
                                       # no button for canceling going back
                                       width=100,
                                       height=50,
                                       corner_radius=10,
                                       text="Nein",
                                       font=("bold", 20),
                                       command=lambda: self.destroy())  # the command destroys the window
        self.no_button.place(x=235,
                             y=32.5)

    def yes_button_function(self, which):
        self.master.switch_window(which)
        self.destroy()
