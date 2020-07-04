# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:06:52 2020

@author: VIDYA
"""

#import pandas as pd

#f = pd.read_csv("C:/Users/VIDYA/Documents/ecg/data_arrhythmia.csv")
#f.to_csv("C:/Users/VIDYA/Documents/ecg/data_arrhythmia1.csv", sep=",")

import csv
with open(r"C:/Users/VIDYA/Documents/ecg/11.txt") as in_file, open(r"C:/Users/VIDYA/Documents/ecg/data_arrhythmia1.csv", 'w') as out_file:
    semicolonin = csv.reader(in_file, delimiter=';')
    commaout = csv.writer(out_file, delimiter=',')
    for row in semicolonin:
        commaout.writerow(row)
    
    
    in_file.close()
    out_file.close()
    
  #remove unwanted rows 
#with open(r"C:/Users/VIDYA/Documents/ecg/11.txt") as in_file, open(r"C:/Users/VIDYA/Documents/ecg/data_arrhythmia1.csv", 'w') as out_file:
#    non_blank = (line for line in in_file if line.strip())
#    out_file.writelines(non_blank)