import psychopy.event
import psychopy.core
import psychopy.visual
import psychopy.gui
import psychopy.sound
import os
import BDM
import sort_by_BDM

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

cur_folder = r"C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon"

tx_file = BDM.main(subj_id)

# tx_file = r"C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Output\11_BDM1.txt"
keys = r"C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Only_6_snacks_ladder_key.xlsx"

A = sort_by_BDM.Sort_By_BDM(tx_file, keys)
df = A.create_full_df()
print(df)


# load parameters

# os.system('C:\\Users\wolfi\Documents\PythonCourse\Final_project\CAT\BDM.py')


# images = os.listdir("Images")
#open a file the contains DataFrame with all the stimuli and the "play sound" boolean





# window
# win = psychopy.visual.Window(
#         units = "pix",
#         fullscr=True
# )
