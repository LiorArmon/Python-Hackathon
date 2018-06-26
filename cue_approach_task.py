import psychopy.event
import psychopy.core
import psychopy.visual

win = psychopy.visual.Window(
        size=[400, 400],
        units="pix",
        fullscr=True
)

img = psychopy.visual.ImageStim(
        win=win,
        image="Images\snickers.jpg",
        units="pix",
        size=[400,400])

img.draw()

win.flip()

psychopy.event.waitKeys()

win.close()