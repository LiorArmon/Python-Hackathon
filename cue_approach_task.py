import psychopy.event
import psychopy.core
import psychopy.visual
import psychopy.gui
import psychopy.sound
import os

images = os.listdir("Images")
#open a file the contains DataFrame with all the stimuli and the "play sound" boolean

# subject info window
gui = psychopy.gui.Dlg()
gui.addField("Subject ID:")
gui.addField("Age:")
gui.addField("Gender:")
gui.show()

# saving subject info
subj_id = gui.data[0]
subj_age = gui.data[1]
subj_gender = gui.data[2]
#save as a metadata to the Results DataFrame


# window
win = psychopy.visual.Window(
        units = "pix",
        size = (1000, 1000),
        fullscr=False
)

# fixation cross
fixation = psychopy.visual.ShapeStim(win, 
    vertices=((0, -10), (0, 10), (0,0), (-10,0), (10, 0)),
    lineWidth=3,
    closeShape=False,
    lineColor="white"
) 

#add a loop that runs on a  range that equals to the number of trials set in the settings doc
# image
for image in images: #repeat for each image in the folder
    img = psychopy.visual.ImageStim(
            win=win,
            image=os.path.normpath("Images/"+image), #opens a picture from Images folder
            units="pix",
            size=[400,400])

    
    #draw fixation cross
    fixation.draw()
    win.flip()
    psychopy.core.wait(0.980) #wait 1 sec
    
    # initializing the clock for RT
    clock = psychopy.core.Clock()
    
    #draw image
    img.draw()
    win.flip()
    psychopy.core.wait(0.7)

# need to add a condition - if in the stimulus data frame, boolean is True do this:
    #sound
    s=psychopy.sound.Sound(value="G", secs=0.1) #creates a sound
    #if play:
    3.0..0
    .
    .
    00
    00.0
    s.play() #plays the sound
    keys = psychopy.event.getKeys(keyList = ["b"], timeStamped=clock) #records the RT for a button press
    psychopy.core.wait(0.3)
# should append the results from the keys list to a Results DataFrame with attributes "stimulus, RT"

win.close()