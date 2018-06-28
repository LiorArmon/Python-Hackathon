import pygame, os, random, numpy as np, glob, psychopy
import psychopy.event
import psychopy.core
import psychopy.visual
import pandas
from psychopy import visual


def probe_organizer(subject_ID='117', main_path='C:\\Users\\naama\\PycharmProjects\\untitled'):
    #Organizes the probe comparisons. Output is the txt file "subject_ID_probe_comparisons.txt" used in the Probe task.
    stim_folder='\\stim' #define stimuli folder

    # import sorted BDM file
    filename = glob.glob(main_path + '\\Output\\' + str(subject_ID) + '_sorted_BDM_mock_data' + '*.txt')
    data = np.genfromtxt(filename[0], dtype=str)

    # fill in the comparisons you want (the numbers indicate value ranking determined the the BDM task
    nobeep = list(data[:, [1]][data[:, 3] == 'Tag.NO_GO'])
    beep = list(data[:, [1]][data[:, 3] == 'Tag.GO'])


    #repeat each item multiple times (as the amount of items), and randomize the order of appearance.
    #This way, the comparisons are random and there may be repetitions. If you want to have only unique comparisons,
    #make the permutation the same for all categories (using indices of one permutation for all the rest)
    beep_perm=np.random.permutation(beep*len(beep))
    nobeep_perm = np.random.permutation(nobeep*len(nobeep))

    #create file to be used in probe, containing all the data needed for comparisons: names of both items and their indices,
    #whether the left one is the go item (determines the side the items will be shown at), and pair type (HV/LV, beep/no beep)
    name_beep=[] #get names of beep items and of no-beep items in each trial
    for i in range(len(beep_perm)):
        name=data[int(beep_perm[i])][0]
        name_beep=np.append(name_beep, name)
    name_nobeep=[]
    for i in range(len(nobeep_perm)):
        name=data[int(nobeep_perm[i])][0]
        name_nobeep=np.append(name_nobeep, name)

    left_go=[] #either 0 or 1, random. determines which item is shown on the left/right in probe
    for i in range(len(beep_perm)):
        left_go=np.append(left_go,random.getrandbits(1))

    comparison_array=np.column_stack((beep_perm, nobeep_perm, left_go, name_beep, name_nobeep))

    np.savetxt(main_path+'\\Output\\'+str(subject_ID)+'_probe_comparisons.txt', comparison_array, fmt='%s', header='Beep Index, No-beep Index, Left Go, Beep Name, No-beep Name')
    return comparison_array



def probe_run(comparison_array, subject_ID,main_path):
    stims_beep = comparison_array[:, 3]
    stims_nobeep = comparison_array[:, 4]
    choice=[]


    win = psychopy.visual.Window(
        units="pix",
        fullscr=True)
    #for i in range(len(stims_beep)):
    for i in range(3):

        fixation = psychopy.visual.ShapeStim(win,
            vertices=((0, -10), (0, 10), (0, 0), (-10, 0), (10, 0)),
                        lineWidth=3,
                        closeShape=False,
                        lineColor="white")

        if comparison_array[i,2]=='0.0': #determines which stimulus is presented on which side, according to "left_go" column in comparison_array
            img1 = psychopy.visual.ImageStim(win=win,
                        image=(main_path+"\\stim\\" + str(stims_beep[i])),  # opens a picture from Images folder
                        units="pix",
                        size=[400, 400],
                        pos=(400, 0.0)
                        )
            img2 = psychopy.visual.ImageStim(
                        win=win,
                        image=(main_path+"\\stim\\" + str(stims_nobeep[i])),  # opens a picture from Images folder
                        units="pix",
                        size=[400, 400],
                        pos=(-400, 0.0)
                        )
        elif comparison_array[i,2]=='1.0':
            img2 = psychopy.visual.ImageStim(
                win=win,
                image=(main_path + "\\stim\\" + str(stims_beep[i])),  # opens a picture from Images folder
                units="pix",
                size=[400, 400],
                pos=(400, 0.0))
            img1 = psychopy.visual.ImageStim(
                win=win,
                image=(main_path + "\\stim\\" + str(stims_nobeep[i])),  # opens a picture from Images folder
                units="pix",
                size=[400, 400],
                pos=(-400, 0.0)
            )

        fixation.draw()
        win.flip()
        psychopy.core.wait(0.980)  # wait 1 sec

        img1.draw()
        img2.draw()
        win.flip()
        resp_key=psychopy.event.waitKeys(keyList=['a','l'])
        choice.append(resp_key)
    win.close()

comparison_array=probe_organizer()
main_path='C:\\Users\\naama\\PycharmProjects\\untitled'
subject_ID="117"

choice=probe_run(comparison_array,subject_ID ,main_path)
comparison_results=pandas.DataFrame(comparison_array)
choice_results=pandas.DataFrame(choice)
comparison_results[5]=choice

go_chosen=[]
for i in range(len(comparison_array)):
    if choice[i]==['a']:
        if comparison_array[i,2]=='1.0':
            go_chosen.append(1)
        elif comparison_array[i,2]=='0.0':
            go_chosen.append(0)
    elif choice[i]==['l']:
        if comparison_array[i,2]=='0.0':
            go_chosen.append(1)
        elif comparison_array[i, 2] == '1.0':
            go_chosen.append(0)
comparison_results['go_chosen']=go_chosen

comparison_results.to_csv(main_path + '\\Output\\' + str(subject_ID) + '_probe_results.csv')