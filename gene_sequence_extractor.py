"""
Author: FeiLiu <FeiLiuEM@outlook.com>
Date: 2024-08-09 16:21:00
LastEditors: FeiLiu <FeiLiuEM@outlook.com>
LastEditTime: 2024-08-09 16:24:52
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
"""

import os
from tqdm import tqdm, trange
from main.getFilePathList import getFilePathList


filepath_hg19 = "hg19"
filepath_hg38 = "hg38"

# get the file list of hg19 and hg38
target_file_hg19 = getFilePathList(filepath_hg19, "fa")
target_file_hg38 = getFilePathList(filepath_hg38, "fa")

# read all the files and get the dict of hg19
chr_dcit_hg19 = dict()
for i in tqdm(target_file_hg19):

    list_temp = []
    with open(i, "r") as f:
        for line in f:
            list_temp.append(line.strip())

    list_temp1 = list_temp[1:]
    chr_string = ""
    chr_string = "".join(list_temp1)

    chr_name = i.split("/")[-1].split(".")[0]
    chr_dcit_hg19[chr_name] = chr_string

# read all the files and get the dict of hg38
chr_dcit_hg38 = dict()
for i in tqdm(target_file_hg38):

    list_temp = []
    with open(i, "r") as f:
        for line in f:
            list_temp.append(line.strip())

    list_temp1 = list_temp[1:]
    chr_string = ""
    chr_string = "".join(list_temp1)

    chr_name = i.split("/")[-1].split(".")[0]
    chr_dcit_hg38[chr_name] = chr_string


# save dict to file
import pickle

with open("hg19.pkl", "wb") as tf:
    pickle.dump(chr_dcit_hg19, tf)

with open("hg38.pkl", "wb") as tf:
    pickle.dump(chr_dcit_hg38, tf)
