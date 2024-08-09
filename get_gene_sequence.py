"""
Author: FeiLiu <FeiLiuEM@outlook.com>
Date: 2024-08-09 16:21:00
LastEditors: FeiLiu <FeiLiuEM@outlook.com>
LastEditTime: 2024-08-09 16:49:16
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
"""

import sys


def merge_args_to_list(args):

    return args[1:]  # 去掉程序本身的名称，只保留传入的参数


# load dict from file
import pickle

with open("hg19.pkl", "rb") as tf:
    chr_dcit_hg19 = pickle.load(tf)

with open("hg38.pkl", "rb") as tf:
    chr_dcit_hg38 = pickle.load(tf)


def get_chr_data(chr_type, chr_name, begin, end):
    if chr_type == "hg19":
        chr_data = chr_dcit_hg19
    elif chr_type == "hg38":
        chr_data = chr_dcit_hg38
    chr_string = chr_data[chr_name]
    return chr_string[begin:end]


if __name__ == "__main__":
    args = sys.argv
    result_list = merge_args_to_list(args)
    # print(result_list)
    sequence = get_chr_data(
        result_list[0], result_list[1], int(result_list[2]), int(result_list[3])
    )
    print(sequence)

