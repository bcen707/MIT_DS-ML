#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:46:38 2022

@author: billy
"""


bootstrap_loandf= []

def test_gen_random_set(dataframe, size):
    for i in range(2):
        sample= np.random.choice(dataframe, size)
        bootstrap_loandf.append(sample)
        
        
# Test Code

# test_gen_random_set(hmeq['LOAN'], 0)
# test_gen_random_set(hmeq['LOAN'], 5)
# test_gen_random_set(hmeq['LOAN'], -1)