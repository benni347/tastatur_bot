'''Creating the GUI'''

# Misc imports
import time
import random as rnd
import json
import webbrowser
#import keyboard
from functools import partial
import base

# Tk import
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dict with min. & max. number of exercises in each "Lerneinheit" (LE)
exercises_range = {
  4: (3, 7),
  5: (0, 7),
  6: (0, 7),
  7: (0, 8),
  8: (0, 8),
  9: (0, 8),
  10: (0, 8),
  11: (0, 7),
  12: (0, 8),
  13: (0, 8),
  14: (0, 8),
  15: (1, 4),
  16: (1, 3),
  17: (1, 2)
}

def record_wait_period(period_to_wait):
  '''store the wait_period in the global variable'''
  global wait_period
  wait_period = float(period_to_wait)

def openweb(url, new=1):
  webbrowser.open(url, new=new)

def exercise(le, uebung):
  '''Helper function run by Tk.button, which executes the proper function.'''
  # "le" = "Lerneinheit"
  import exercises.exercise
  exercises.exercise.run(le, uebung)

def drawWindow():
  window = tk.Tk()

  window.title("Exercises")
  window.geometry('950x500')

  tab_parent = ttk.Notebook(window)

  # "Exercises" tabs
  tab_list = [] # List with all the tabs for the exercises
  # Create tabs
  for tn in range(14):
    # Empty tabs
    tab_list.append(ttk.Frame(tab_parent))

  tab_list_settings = [
    ttk.Frame(tab_parent)
  ]

  title = 4
  for tab in tab_list:
    tab_parent.add(tab, text="%s" % title)
    title = title+1

  # "Settings" tab
  titleSettings = "Settings"
  for tab in tab_list_settings:
    tab_parent.add(tab, text="Settings")

  mail = tk.Label(tab_list_settings[0], text="E-Mail")
  password = tk.Label(tab_list_settings[0], text="Password")
  username_tx = tk.Entry(tab_list_settings[0])
  password_tx = tk.Entry(tab_list_settings[0], show="#")
  time_scale = tk.Scale(tab_list_settings[0], from_=0.1, to=1.0,
    resolution=0.01, length=600, orient=tk.HORIZONTAL, command=record_wait_period
  )
  submit = tk.Button(tab_list_settings[0], text="Speichern",
    command=lambda: base.store_settings(
      username_tx.get(), password_tx.get(), time_scale.get())
  )

  username_tx.insert(0, base.USERNAME)
  password_tx.insert(0, base.PASSWORD)
  time_scale.set(base.WAIT_PERIOD)

  # === WIDGETS FOR TABS
  # "exercises": Dict containing for every "Lerneinheit":
  # - "exercises": Dict with partial() function for every "Übung"
  # - "buttons": List with buttons for every "Übung"
  exercises = {}
  btn_list = []
  # "le" = "Lerneinheit"
  for le in exercises_range.keys():
    tab = tab_list[le-4] # current tab
    exercises[le] = {
      "exercises": {},
      "buttons": []
    }
    for uebung in range(exercises_range[le][0], exercises_range[le][1]+1):
      exercises[le]["exercises"][uebung] = partial(exercise, le, uebung)
      exercises[le]["buttons"].append(
        tk.Button(tab, text="%s-%s" % (le, uebung), command=exercises[le]["exercises"][uebung])
      )
    btn_list.append(exercises[le]["buttons"])

  # === ADD WIDGETS TO GRID ON TABS
  row = 0
  col = -1

  # Add buttons to tabs, so that they are actually visible
  for btns in btn_list:
    for btn in btns:
      if (row%8) == 0: col = col + 1
      row = (row%8) + 1
      btn.grid(row=row, column=col, padx=15, pady=15)
    row=0

  # Widgets on Settings tab
  mail.grid(row=0, column=0)
  password.grid(row=1, column=0)
  username_tx.grid(row=0, column=1)
  password_tx.grid(row=1, column=1)
  time_scale.grid(row=3, column=0)
  submit.grid(row=4, column=0)

  tab_parent.pack(expand=1, fill='both')

  window.mainloop()
