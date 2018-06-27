import os
class PullData:
    """pulls the ranking data from a text file and returns it for use in later stages"""
    def __init__(self, sub_no):
        self.sub_no = sub_no
        
    
    def open_data(self):
        #with (os.path.normpath('Ranking/Itzik_'+str(self.sub_no)+'.txt'), 'r') as file:
        f = open('Itzik_1.txt','r')
        data = f.read()
        return(data)
        f.close()
        
        