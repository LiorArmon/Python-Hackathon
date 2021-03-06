import psychopy.core
import psychopy.event
import psychopy.visual
import psychopy.gui
import psychopy.sound
import os
import numpy as np

class Trial:
    def __init__(self, stimulus, params, win, success_count, failure_count, cue):
        self.stimulus = stimulus
        self.params = params
        self.pre_cue = self.params.get('pre_cue')
        self.stim_time = self.params['stim_time']
        self.iti = self.params['iti']
        self.success_window = self.params['success_window'] # this is time after pic disappears that still defines as success
        self.stim_size = self.params['stim_size']
        self.stim_position = tuple(self.params['stim Position'])
        self.cue = cue
        self.success_count = success_count
        self.failure_count = failure_count
        self.win = win


    def run_trial(self):

        win = self.win
        # fixation cross
        fixation = psychopy.visual.ShapeStim(
            win=win,
            vertices=((0, -10), (0, 10), (0, 0), (-10, 0), (10, 0)),
            lineWidth=3,
            closeShape=False,
            lineColor="white")

        if self.stimulus.show:
            # image
            img = psychopy.visual.ImageStim(
                win=win,
                image=os.path.normpath("Images/" + self.stimulus.name),  # opens a picture from Images folder
                units="pix",
                size=[self.stim_size],
                pos=self.stim_position
            )

            # draw stimulus image
            img.draw()
            win.flip()
            clock = psychopy.core.Clock()  # start the clock
            # Cue section
            if self.stimulus.cued:  # if the stimulus is set to be cued

                pre_cue = self.pre_cue + (self.success_count * 0.016) - (self.failure_count * 0.05)
                if pre_cue < 0:  # so the cue doesn't show before the picture
                    pre_cue = 0
                elif pre_cue > self.stim_time + self.success_window:  # so the cue doesn't show too late
                    pre_cue = self.stim_time + self.success_window

                psychopy.core.wait(pre_cue)  # wait until cue
                
                #todo use enum
                if self.cue.cue_type == 'sound':  # if the cue is set to be a sound
                    self.cue.play()  # plays the sound
                elif self.cue.cue_type == 'image':  # if the cue is set to be an image
                    self.cue.draw()  # display the cue

            else:
                pre_cue = 0  # if the stimulus is not cued, just display it for 1 sec

            clock.reset()  # if the stimulus is cued restart the clock when the cue appears
            rt_pressed_keys = psychopy.event.getKeys(timeStamped = clock)
            if rt_pressed_keys:
                print(rt_pressed_keys)
                self.RT = rt_pressed_keys[0][1]  # records the RT for a button press
                self.pressed_key = rt_pressed_keys[0][0]  # record which key was  pressed
            else:
                self.RT = np.nan
                self.pressed_key = np.nan
                self.success = 0    
                
            psychopy.core.wait(
                self.stim_time - pre_cue)  # wait for the remaining time after the cue until the stimulus disappears

            # draw fixation cross - Inter Trial Interval
            fixation.draw()
            win.flip()
            psychopy.core.wait(self.iti)  # show cross for the amount of time set in ITI
            
            if self.RT != np.nan:            
                if (self.RT < (self.stim_time - pre_cue) + self.success_window) and (self.pressed_key == self.params['key_to_press']):
                    self.success = 1
                else:
                    self.success = 0

        elif self.stimulus.still:  # if stimulus is instructions, it just waits for a space bar hit to continue
            psychopy.event.waitKeys(keyList=['space'])

            # draw fixation cross - Inter Trial Interval
            fixation.draw()
            win.flip()
            psychopy.core.wait(self.iti)  # show cross for the amount of time set in ITI

        else:
            psychopy.core.wait(0)  # if the stimulus is not set to be shown, just skip this trial
                
    def get_trial_data(self):
        return self.stimulus.name, self.RT, self.success, self.pressed_key