#!/usr/bin/env python
# coding: utf-8


import os
import shutil
import numpy as np
import pandas as pd




"""You may not need the code in this file. This file contains the code which I used to create my train/test data 
from the data provided by Zindi and other data I was able to generate."""




PATH1 = 'C:\\Users\\Divine Comprehensive\\books\\Audio\\GIZ\\nlp_keywords'
PATH2 = 'C:\\Users\\Divine Comprehensive\\books\\Audio\\GIZ\\AdditionalUtterances'
DST = 'C:\\Users\\Divine Comprehensive\\books\\Audio\\GIZ\\audio_files'





train = pd.read_csv('Train.csv')





def create_data(folder, path):
    fn = []
    labels = []
    for i in os.listdir(path=path):
        for j in os.listdir(path=path+'\\'+i):
            fn.append(f'audio_files/{j}')
            labels.append(i)
    return fn, labels
                            
# create filename and label lists
a, b = create_data('nlp_keywords', PATH1)
c, d = create_data('AdditionalUtterances', PATH2)

# in a dataframe
nlp_keywords = pd.DataFrame({'fn': a, 'label': b})
AdditionalUtterances = pd.DataFrame({'fn': c, 'label': d})


df = pd.concat([train, nlp_keywords, AdditionalUtterances], axis=0)
df.to_csv('df.csv', index=False)


def move_files(PATH, dst):
    for i in os.listdir(path=PATH):
        for j in os.listdir(path=PATH+'\\'+i+'\\'):
            file = PATH+'\\'+i+'\\'+j
            shutil.move(file, dst)
    return


move_files(PATH1, DST)
move_files(PATH2, DST)






