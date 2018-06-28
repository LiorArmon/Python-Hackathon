import psychopy.core
import psychopy.event
import psychopy.visual
import pandas as pd
import numpy as np
import psychopy.gui
import psychopy.sound
import os

def create_psychopy_window():
    win = psychopy.visual.Window(
        units = "pix",
        size = (200, 200), 
        fullscr=False) #todo change to True
    return win

def create_fixation_cross(win):
    fixation = psychopy.visual.ShapeStim(
        win=win,
        vertices=((0, -10), (0, 10), (0, 0), (-10, 0), (10, 0)),
        lineWidth=3,
        closeShape=False,
        lineColor="white")
    return fixation

def create_psychopy_image(win, params, stimulus):
    img = psychopy.visual.ImageStim(
        win=win,
        image=os.path.normpath("Images/" + stimulus.name),  # opens a picture from Images folder
        units="pix",
        size=params["stim_size"],
        pos=params["stim_position"])
    return img

def create_psychopy_sound():
    s = psychopy.sound.Sound(params[cue_sound_value], secs=params[time])  # creates a sound
    return s