# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:20:07 2021

@author: FALAH FAKHRI

Module: gpt_launcher.py
========================================================================================
This code is used to execute any *xml file using GPT (Graph processing Tool) in python. 
========================================================================================
"""

# imporrt required modules 

import subprocess as sp
import time

def SentinelGraph(gpt_path, graph_path):
    """Returns a results of executing gpt file in python 
    parameters
    ----------
    gpt_path: str
        path directory to the ~\snap\bin\gpt'
    graph_path: str
        the path to the *.xml file
    """
    start_time = time.time()
    gpt_path = gpt_path
    graph_path = graph_path
    
    cmd_pts = [gpt_path,
               graph_path,
               '-PyourParameter1="{}"'.format(graph_path),
               '-PyourParameter2="{}"'.format(graph_path)]
    
    sp.check_call(cmd_pts)
    
    end_time = time.time()
    hours, rem = divmod(end_time-start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    
    if __name__ == '__main__':
        print("Total time is: \n", "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
    






