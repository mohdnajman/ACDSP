# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: handle_logging.py
Description: 3.	Write a program in Python to handle logging

Date Created:       Thu, 11 July 2023, 19:56:00
Date last update:   Thu, 11 July 2023

@author: evoma
"""

import os
import logging

logging.basicConfig(filename = 'C:\\Users\\evoma\\anaconda\\Scripts\\handle_logging_log.txt', level=logging.debug,filemode='w')

def findgrade():
    exam_marks = int(input('Enter the marks you scored: (0-100)'))
    
    gvgrade = ''
    
    if exam_marks >= 0 and exam_marks <= 49:
        logging.debug('exam_marks >= 0 and exam_marks <= 49:')
        gvgrade = 'FAIL'
        return gvgrade
    elif exam_marks >= 50 and exam_marks <= 64:
        logging.debug('exam_marks >= 50 and exam_marks <= 64:')
        gvgrade = 'PASS'        
        return gvgrade
    elif exam_marks >= 65 and exam_marks <= 74:
        logging.debug('exam_marks >= 65 and exam_marks <= 74:')
        gvgrade = 'CREDIT'
        return gvgrade
    elif exam_marks >= 75 and exam_marks <= 79:
        logging.debug('exam_marks >= 75 and exam_marks <= 79:')
        gvgrade = 'A'
        return gvgrade
    elif exam_marks >= 80:
        logging.debug('exam_marks >= 80:')
        gvgrade = 'A+'
        return gvgrade
    else:
        logging.debug('Enter a valid number')
        gvgrade = ''
        print('Enter a valid number')
        return gvgrade
    
print('Your grade is', findgrade())