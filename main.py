import psychopy.event
import psychopy.core
import psychopy.visual
import psychopy.gui
import psychopy.sound
import os
import BDM
import sort_by_BDM
from Game import Game
import yaml 



with open("params.yml", 'r') as stream:
   try:
      params=(yaml.load(stream))
   except yaml.YAMLError as exc:
       print(exc)
   
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

cur_folder = os.getcwd()

tx_file = BDM.main(subj_id)

# tx_file = r"C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Output\11_BDM1.txt"
keys = os.path.join(cur_folder, "Only_6_snacks_ladder_key.xlsx")

A = sort_by_BDM.Sort_By_BDM(tx_file, keys)
df = A.create_full_df()
print(df)
game=Game(params, df, 1, 1) #todo no_block, interval from params
print("RUN GAME")
game.run_game()
print("Bye")
game.win.close()
res_df = game.get_final_results()
res_df.to_csv("res_df") #todo take from params

