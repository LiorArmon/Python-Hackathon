import psychopy.core
import psychopy.event
import psychopy.visual
import pandas as pd
import numpy as np
import psychopy.gui
import psychopy.sound
import os
import yaml
import json
from pathlib import Path
import random
from Trial import Trial

class Block:
    def __init__(self, stim_list, df, params, win, cue):
        self.df = df
        print(self.df.columns)
        print(self.df["StimName"])
        self.win = win
        self.stim_list = stim_list
        self.success_count = 0
        self.failure_count = 0
        self.params = params
        self.cue = cue

    def run_block(self):
        random.shuffle(self.stim_list)
        self.trials = []

        for stim in self.stim_list:
            curr_trial = Trial(stim, self.params, self.win, self.success_count, self.failure_count, self.cue)
            curr_trial.run_trial()
            self.trials.append(curr_trial)
    
    def get_result(self):        
        #todo take outto a seperate function:
        trials_data = pd.DataFrame(data=None, index=None, columns=['trial', 'RT', 'success', 'key'])

        for trial in self.trials:
            if trial.stimulus.show:
                trial_data = trial.get_trial_data()
                if trial_data[2] == 1:
                    self.success_count += 1
                else:
                    self.failure_count += 1
                trials_data.append = (
                {'trial': trial_data[0], 'RT': trial_data[1], 'success': trial_data[2], 'key': trial_data[3]})
        
        return trials_data