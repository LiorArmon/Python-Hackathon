import psychopy.core
import psychopy.event
import psychopy.visual
import pandas as pd
import numpy as np
import psychopy.gui
import psychopy.sound
from SBDM_Data import SBDM_Data
from Block import Block
from psychopy_utilities import create_psychopy_window
from Cue import Cue

class Game:
    def __init__(self, params, data_frame, no_of_blocks, break_interval):
        self.data_frame = data_frame
        self.no_of_blocks = no_of_blocks
        self.break_interval = break_interval
        self.win = create_psychopy_window()
        self.params = params
        self.textmsg = self.params['break_text']
        self.sbdm = SBDM_Data(self.data_frame)
        self.stim_list = self.sbdm.create_stim_list()
        self.cue = Cue(self.win, self.params)

    def run_game(self):
        
        list_of_results = []  # will contain DataFrames
        for block_idx in range(self.no_of_blocks):
            block = Block(self.stim_list, self.data_frame, self.params, self.win, self.cue)
            block.run_block()
            list_of_results.append(block.get_result())
            if np.mod(block_idx, self.break_interval) == 0:
                # load the break instructions message
                message = psychopy.visual.TextStim(self.win, #todo use utils
                                                   text=self.textmsg)  # opens a break instructions picture from Images folder

                # draw the break instructions image
                message.draw()
                self.win.flip()
                
                psychopy.event.waitKeys(keyList=['space'])
                
            print("End block")
        
        self.results_df = pd.concat(list_of_results)
        
       
        
    def get_final_results(self):
        return self.results_df
    