import PySimpleGUI as sg
from time import sleep
import os
import sys
script_dir = os.path.dirname( __file__ )
func_dir = os.path.join(script_dir, "Main")
sys.path.append(func_dir)
from Main import Main

class screen:
    def __init__(self):
        """
        GUI Starting configs
        
        """



        sg.theme(new_theme="DarkBlue5")

        layout = [
            [sg.Text("", size=(10, 4), key='-DUMMY-', justification='c')],
            [sg.Button('Iniciar robô', size=(25, 2))],
        ]
        self.window = sg.Window("Robô mesha. technology", layout, size=(400,200), element_justification="center", icon="Data\\logo.ico")

    def run(self):
        """
        Start the program's interface

        """
        while True:
            self.events, self.values = self.window.Read()
            if self.events == sg.WIN_CLOSED:
                break
            else:
                bot = Main.Run()
                break
        self.window.Close()

    def popup(self):
        sg.Popup("Click me whe you are logged in :)", keep_on_top=True)

teste = screen()

teste.run()
