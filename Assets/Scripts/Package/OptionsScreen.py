#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# OptionenFenster

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import window_geometry, color_SET, text_color_SET, \
    back_arrow_image, appearance_mode, window_size


class OptionsScreen(ctk.CTkFrame):  # class for the OptionsScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")
        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # top bar------------------------------------------------------------
        self.optionsscreen_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                        fg_color=color_SET,
                                                        width=window_geometry[0] - 70,
                                                        height=40,
                                                        corner_radius=10,
                                                        text="Optionen",
                                                        text_color=text_color_SET,
                                                        font=("bold", 20),
                                                        anchor="w")
        self.optionsscreen_indicator_bar.place(x=0,
                                               y=0)

        # button frame------------------------------------------------------------
        self.optionsscreen_button_frame = ctk.CTkFrame(master=self,  # frame for the buttons and the menu
                                                       width=460,
                                                       height=130)
        self.optionsscreen_button_frame.place(x=30,
                                              y=75)

        # back button------------------------------------------------------------
        self.optionsscreen_back_button = ctk.CTkButton(master=self,  # back button
                                                       width=40,
                                                       height=40,
                                                       corner_radius=10,
                                                       text="",
                                                       anchor="ne",
                                                       image=back_arrow_image,
                                                       command=lambda: self.master.switch_window("0"))
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        self.optionsscreen_back_button.place(x=window_geometry[0] - 65,
                                             y=0)

        # light mode / dark mode ------------------------------------------------------------
        # option menu
        self.options_light_dark_menu = ctk.CTkOptionMenu(master=self.optionsscreen_button_frame,
                                                         # menu for light / dark
                                                         width=100,
                                                         height=40,
                                                         font=("bold", 20),
                                                         dropdown_font=("bold", 20),
                                                         corner_radius=5,
                                                         values=appearance_mode,
                                                         command=self.master.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_light_dark_menu.place(x=220,
                                           y=20)
        # label
        self.options_light_dark_label = ctk.CTkLabel(master=self.optionsscreen_button_frame,
                                                     # label to describe the menu above
                                                     fg_color=color_SET,
                                                     width=180,
                                                     height=40,
                                                     corner_radius=5,
                                                     text="Anzeigemodus",
                                                     text_color=text_color_SET,
                                                     font=("bold", 20))
        self.options_light_dark_label.place(x=20,
                                            y=20)

        # Window size ------------------------------------------------------------
        # option menu
        self.options_window_size_menu = ctk.CTkOptionMenu(master=self.optionsscreen_button_frame,
                                                          width=100,
                                                          height=40,
                                                          font=("bold", 20),
                                                          dropdown_font=("bold", 20),
                                                          corner_radius=5,
                                                          values=window_size,
                                                          command=self.master.window_size_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_window_size_menu.place(x=220,
                                            y=70)
        # label
        self.options_window_size_label = ctk.CTkLabel(master=self.optionsscreen_button_frame,
                                                      # label to describe the menu above
                                                      fg_color=color_SET,
                                                      width=180,
                                                      height=40,
                                                      corner_radius=5,
                                                      text="Fenstergröße",
                                                      text_color=text_color_SET,
                                                      font=("bold", 20))
        self.options_window_size_label.place(x=20,
                                             y=70)
