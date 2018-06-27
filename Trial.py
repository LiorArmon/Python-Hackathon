import os
import psychopy.visual
import psychopy.core
import psychopy.sound

class Trial:
    def __init__(self, stimulus, pre_cue, stim_time, iti, itis, stim_size, stim_position, win, cue, success_count, failure_count):
        self.stimulus = stimulus
        self.pre_cue = pre_cue
        self.stim_time = stim_time
        self.iti = iti
        self.itis = itis
        self.stim_size = stim_size
        self.stim_position = stim_position
        self.cue = cue
        self.success_count = success_count
        self.failure_count = failure_count
        self.success = ()
        self.RT = ()
        
        
    def run_trial(self):
        if self.stimulus.show:
        
            win = self.win
            
            # fixation cross
            fixation = psychopy.visual.ShapeStim(
                win = win, 
                vertices=((0, -10), (0, 10), (0,0), (-10,0), (10, 0)),
                lineWidth=3,
                closeShape=False,
                lineColor="white") 
            
            # image
            img = psychopy.visual.ImageStim(
                win=win,
                image=os.path.normpath("Images/"+self.stimulus.name), #opens a picture from Images folder
                units="pix",
                size=[self.stim_size])
            
            
            #draw stimulus image
            img.draw()
            win.flip()
            clock = psychopy.core.Clock() #start the clock

            
            #Cue section
            if self.stimulus.cued: #if the stimulus is set to be cued
                
                pre_que = self.pre_cue+self.success*0.06-self.failure*0.05
                if pre_que < 0: # so the cue doesn't show before the picture
                    pre_que = 0
                elif pre_que > self.stim_time + self.itis: # so the cue doesn't show too late
                    pre_cue = self.stim_time + self.itis
                
                psychopy.core.wait(pre_cue) #wait until cue
                clock = psychopy.core.Clock() #if the stimulus is cued restart the clock
            
                if self.cue.cue_type == 'sound': #if the cue is set to be a sound
                    self.cue.play() #plays the sound
                elif self.cue.cue_type == 'image': #if the cue is set to be an image
                    self.cue.draw()
            
            else:
                pre_que = 0 #if the stimulus is not cued, just display it for 1 sec
                
            self.RT = psychopy.event.getKeys(timeStamped=clock)[1] #records the RT for a button press
            
            psychopy.core.wait(stim_time-pre_que)
            
        #draw fixation cross - Inter Trial Interval
        fixation.draw()
        win.flip()
        psychopy.core.wait(self.iti) #show cross for the amount of time set in ITI
    
        elif self.stimulus.still: #if stimulus is instructions, it just waits for a space bar hit to continue
            psychopy.event.waitKeys(keyList = ['space'])
        else:
             psychopy.core.wait(0) # if the stimulus is not set to be shown, just skip this trial
            
   
            