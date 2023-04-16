import tkinter as tk
import ttkbootstrap as ttk
from classes.game import Game

window = ttk.Window("PySwarmSim")
window.geometry("600x400")

game = Game(window, 500, 1)

meat_frame = ttk.Frame(window)
meat_label = ttk.Label(meat_frame, text="Meat:")
meat_int_label = ttk.Label(meat_frame, textvariable=game.meat_var)

meat_frame.pack()
meat_label.pack(side="left")
meat_int_label.pack(side="left")

# for creature in game.upgradables:
#     creature_frame = ttk.Frame(window)
#     name_label = ttk.Label(creature_frame, text=creature.name)
#     level_label = ttk.Label(creature_frame, text="Level:")
#     level_int_label = ttk.Label(creature_frame, textvariable=creature.level_var)

window.mainloop()
