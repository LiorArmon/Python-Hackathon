import psychopy.event
import psychopy.core
import psychopy.visual
import psychopy.gui

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


# window
win = psychopy.visual.Window(
        units = "pix",
        fullscr=True
)

# fixation cross
fixation = psychopy.visual.ShapeStim(win, 
    vertices=((0, -10), (0, 10), (0,0), (-10,0), (10, 0)),
    lineWidth=3,
    closeShape=False,
    lineColor="white"
) 

# image
img = psychopy.visual.ImageStim(
        win=win,
        image="Images\snickers.jpg",
        units="pix",
        size=[400,400])

#draw fixation cross
fixation.draw()
win.flip()
psychopy.core.wait(0.980) #wait 1 sec

#draw image
img.draw()
win.flip()
psychopy.event.waitKeys() #wait for user to press a button

win.close()