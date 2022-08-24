#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:46:38 2022

@author: billy
"""


bootstrap_loandf= []

for i in range(2): 
    x= np.random.choice(hmeq['LOAN'], 5)
    bootstrap_loandf.append(x)