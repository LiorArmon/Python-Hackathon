import psychopy.event
import psychopy.core
import psychopy.visual



# window
win = psychopy.visual.Window(
        size=[400, 400],
        units="pix",
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