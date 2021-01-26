#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on januari 26, 2021, at 14:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

#how many trials must be completed to end a trial block successfully?
Trial_repeats = 4 

#How long is it possible for a participant to respond per trial?
pres_duration = 2.4 

#Do you want to enable facial feedbacK? It shows a smiley that  represents you overall performance? 
#It corresponds with specific intervals between perfect and bad. 
#Choose 0 to disable facial feedback and 1 to enable facial feedback
enable_facial_feedback = 0

#If the change_pres_duration = 0, then each block has the same reaction time
#If the change_pres_duration = 1, then each block has a different reaction time. 
#If the change_pres_duration eaquals to 1, it means that it will go faster and faster per block
change_pres_duration = 1 

#What score is the participant beginning with?
face_score = 1

#The values that are important to make the face change

# If the face_score is above the perfect criterion, the happiest ( :D ) face is shown
# If the face_score is between the perfect and the good criterion, the happy ( :) ) face is shown
# If the face_score is between the good and okay criterion, the neutral ( :| ) face is shown
# If the face_score is between the okay and bad criterion, the sad ( :( ) face is shown
# If the face_score is below the bad criterion, the angry ( >:( ) face is shown

perfect = 3
good = 0
okay = -3
bad = -5



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'PASAT_EN'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\remco\\OneDrive\\Documenten\\Master- ACP\\Stage CMH\\Stage- Nov2020-Jan2021\\PASAT_final_ED_Pyscripts\\PASAT\\PASAT_EN.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction_screen"
Instruction_screenClock = core.Clock()
Click_to_continue = event.Mouse(win=win)
x, y = [None, None]
Click_to_continue.mouseClock = core.Clock()
Instruction_text = visual.TextStim(win=win, name='Instruction_text',
    text="You are about to start an experiment in which your working memory, information processing, and coping will be tested. \nIn short, the main goal is to add up the last two digits that were mentioned by the computer. \n\nFor example: \nFirstly, you hear number 2. This implies that you have to press the box with number 2 in it. \nNext, you'll hear number 4. This implies that you have to add up these two digits, namely 4 and 2. \nThus, you'll press the box with number 6. \n\nIf you hear number 8 afterward, you'll add up number 4 (the last digit) and number 8 (the current digit), \nwhich means that you have to press box number 12. \n\nIf you don't remember it anymore, take a quick break and start with the upcoming number. \n\nKlick with your mouse to start the experiment",
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Determine_stim_presentation_time"
Determine_stim_presentation_timeClock = core.Clock()
round_number = 0
time_zero = core.monotonicClock.getTime()

# Initialize components for Routine "Trial_screen"
Trial_screenClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
last_stim= 0
block_1 = visual.Rect(
    win=win, name='block_1',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_1 = visual.TextStim(win=win, name='text_1',
    text='1',
    font='Arial',
    pos=(0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
sound_1 = sound.Sound('1.wav', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)
block_2 = visual.Rect(
    win=win, name='block_2',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
text_2 = visual.TextStim(win=win, name='text_2',
    text='2',
    font='Arial',
    pos=(0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1)
block_3 = visual.Rect(
    win=win, name='block_3',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='3',
    font='Arial',
    pos=(0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
sound_3 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1)
block_4 = visual.Rect(
    win=win, name='block_4',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
text_4 = visual.TextStim(win=win, name='text_4',
    text='4',
    font='Arial',
    pos=(0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
sound_4 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1)
block_5 = visual.Rect(
    win=win, name='block_5',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text='5',
    font='Arial',
    pos=(0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
sound_5 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1)
block_6 = visual.Rect(
    win=win, name='block_6',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='6',
    font='Arial',
    pos=(0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
sound_6 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1)
block_7 = visual.Rect(
    win=win, name='block_7',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-23.0, interpolate=True)
text_7 = visual.TextStim(win=win, name='text_7',
    text='7',
    font='Arial',
    pos=(0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
sound_7 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1)
block_8 = visual.Rect(
    win=win, name='block_8',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='8',
    font='Arial',
    pos=(0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
sound_8 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1)
block_9 = visual.Rect(
    win=win, name='block_9',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-29.0, interpolate=True)
text_9 = visual.TextStim(win=win, name='text_9',
    text='9',
    font='Arial',
    pos=(0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
sound_9 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1)
block_10 = visual.Rect(
    win=win, name='block_10',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-32.0, interpolate=True)
text_10 = visual.TextStim(win=win, name='text_10',
    text='10',
    font='Arial',
    pos=(-0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
block_11 = visual.Rect(
    win=win, name='block_11',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-34.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='11',
    font='Arial',
    pos=(-0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
block_12 = visual.Rect(
    win=win, name='block_12',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-36.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='12',
    font='Arial',
    pos=(-0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-37.0);
block_13 = visual.Rect(
    win=win, name='block_13',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-38.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='13',
    font='Arial',
    pos=(-0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-39.0);
block_14 = visual.Rect(
    win=win, name='block_14',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-40.0, interpolate=True)
text_14 = visual.TextStim(win=win, name='text_14',
    text='14',
    font='Arial',
    pos=(-0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-41.0);
block_15 = visual.Rect(
    win=win, name='block_15',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-42.0, interpolate=True)
text_15 = visual.TextStim(win=win, name='text_15',
    text='15',
    font='Arial',
    pos=(-0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-43.0);
block_16 = visual.Rect(
    win=win, name='block_16',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-44.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='16',
    font='Arial',
    pos=(-0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-45.0);
block_17 = visual.Rect(
    win=win, name='block_17',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-46.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='17',
    font='Arial',
    pos=(-0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-47.0);
block_18 = visual.Rect(
    win=win, name='block_18',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-48.0, interpolate=True)
text_18 = visual.TextStim(win=win, name='text_18',
    text='18',
    font='Arial',
    pos=(-0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-49.0);

# Initialize components for Routine "Feedback_screen"
Feedback_screenClock = core.Clock()
ansColor = ''

Feedback_image = visual.ImageStim(
    win=win,
    name='Feedback_image', 
    image='sin', mask=None,
    ori=0, pos=(0,-0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
FB_Text_block0 = visual.TextStim(win=win, name='FB_Text_block0',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
FB_text_block1234 = visual.TextStim(win=win, name='FB_text_block1234',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
B_1_FB = visual.Rect(
    win=win, name='B_1_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
T_1_FB = visual.TextStim(win=win, name='T_1_FB',
    text='1',
    font='Arial',
    pos=(0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
B_2_FB = visual.Rect(
    win=win, name='B_2_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
T_2_FB = visual.TextStim(win=win, name='T_2_FB',
    text='2',
    font='Arial',
    pos=(0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
B_3_FB = visual.Rect(
    win=win, name='B_3_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
T_3_FB = visual.TextStim(win=win, name='T_3_FB',
    text='3',
    font='Arial',
    pos=(0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
B_4_FB = visual.Rect(
    win=win, name='B_4_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
T_4_FB = visual.TextStim(win=win, name='T_4_FB',
    text='4',
    font='Arial',
    pos=(0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
B_5_FB = visual.Rect(
    win=win, name='B_5_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
T_5_FB = visual.TextStim(win=win, name='T_5_FB',
    text='5',
    font='Arial',
    pos=(0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
B_6_FB = visual.Rect(
    win=win, name='B_6_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
T_6_FB = visual.TextStim(win=win, name='T_6_FB',
    text='6',
    font='Arial',
    pos=(0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
B_7_FB = visual.Rect(
    win=win, name='B_7_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
T_7_FB = visual.TextStim(win=win, name='T_7_FB',
    text='7',
    font='Arial',
    pos=(0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
B_8_FB = visual.Rect(
    win=win, name='B_8_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
T_8_FB = visual.TextStim(win=win, name='T_8_FB',
    text='8',
    font='Arial',
    pos=(0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
B_9_FB = visual.Rect(
    win=win, name='B_9_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-21.0, interpolate=True)
T_9_FB = visual.TextStim(win=win, name='T_9_FB',
    text='9',
    font='Arial',
    pos=(0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
B_10_FB = visual.Rect(
    win=win, name='B_10_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-23.0, interpolate=True)
T_10_FB = visual.TextStim(win=win, name='T_10_FB',
    text='10',
    font='Arial',
    pos=(-0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
B_11_FB = visual.Rect(
    win=win, name='B_11_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-25.0, interpolate=True)
T_11_FB = visual.TextStim(win=win, name='T_11_FB',
    text='11',
    font='Arial',
    pos=(-0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
B_12_FB = visual.Rect(
    win=win, name='B_12_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-27.0, interpolate=True)
T_12_FB = visual.TextStim(win=win, name='T_12_FB',
    text='12',
    font='Arial',
    pos=(-0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-28.0);
B_13_FB = visual.Rect(
    win=win, name='B_13_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-29.0, interpolate=True)
T_13_FB = visual.TextStim(win=win, name='T_13_FB',
    text='13',
    font='Arial',
    pos=(-0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
B_14_FB = visual.Rect(
    win=win, name='B_14_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-31.0, interpolate=True)
T_14_FB = visual.TextStim(win=win, name='T_14_FB',
    text='14',
    font='Arial',
    pos=(-0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
B_15_FB = visual.Rect(
    win=win, name='B_15_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-33.0, interpolate=True)
T_15_FB = visual.TextStim(win=win, name='T_15_FB',
    text='15',
    font='Arial',
    pos=(-0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
B_16_FB = visual.Rect(
    win=win, name='B_16_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-35.0, interpolate=True)
T_16_FB = visual.TextStim(win=win, name='T_16_FB',
    text='16',
    font='Arial',
    pos=(-0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-36.0);
B_17_FB = visual.Rect(
    win=win, name='B_17_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-37.0, interpolate=True)
T_17_FB = visual.TextStim(win=win, name='T_17_FB',
    text='17',
    font='Arial',
    pos=(-0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-38.0);
B_18_FB = visual.Rect(
    win=win, name='B_18_FB',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-39.0, interpolate=True)
T_18_FB = visual.TextStim(win=win, name='T_18_FB',
    text='18',
    font='Arial',
    pos=(-0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-40.0);

# Initialize components for Routine "Rest_screen"
Rest_screenClock = core.Clock()
Rest_text = visual.TextStim(win=win, name='Rest_text',
    text='This trial block has ended. \nKlick to continue with the next trial block.',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Rest_click = event.Mouse(win=win)
x, y = [None, None]
Rest_click.mouseClock = core.Clock()

# Initialize components for Routine "Final_screen"
Final_screenClock = core.Clock()
Thanks = visual.TextStim(win=win, name='Thanks',
    text='Thanks for participating!\nPress spacebar to end the experiment.',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_exp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction_screen"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the Click_to_continue
gotValidClick = False  # until a click is received
# keep track of which components have finished
Instruction_screenComponents = [Click_to_continue, Instruction_text]
for thisComponent in Instruction_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction_screen"-------
while continueRoutine:
    # get current time
    t = Instruction_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Click_to_continue* updates
    if Click_to_continue.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Click_to_continue.frameNStart = frameN  # exact frame index
        Click_to_continue.tStart = t  # local t and not account for scr refresh
        Click_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Click_to_continue, 'tStartRefresh')  # time at next scr refresh
        Click_to_continue.status = STARTED
        Click_to_continue.mouseClock.reset()
        prevButtonState = Click_to_continue.getPressed()  # if button is down already this ISN'T a new click
    if Click_to_continue.status == STARTED:  # only update if started and not finished!
        buttons = Click_to_continue.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *Instruction_text* updates
    if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_text.frameNStart = frameN  # exact frame index
        Instruction_text.tStart = t  # local t and not account for scr refresh
        Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
        Instruction_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_screen"-------
for thisComponent in Instruction_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Instruction_text.started', Instruction_text.tStartRefresh)
thisExp.addData('Instruction_text.stopped', Instruction_text.tStopRefresh)
# the Routine "Instruction_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block_Loop = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block_Loop')
thisExp.addLoop(Block_Loop)  # add the loop to the experiment
thisBlock_Loop = Block_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_Loop.rgb)
if thisBlock_Loop != None:
    for paramName in thisBlock_Loop:
        exec('{} = thisBlock_Loop[paramName]'.format(paramName))

for thisBlock_Loop in Block_Loop:
    currentLoop = Block_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_Loop.rgb)
    if thisBlock_Loop != None:
        for paramName in thisBlock_Loop:
            exec('{} = thisBlock_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Determine_stim_presentation_time"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Determine_stim_presentation_timeComponents = []
    for thisComponent in Determine_stim_presentation_timeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Determine_stim_presentation_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Determine_stim_presentation_time"-------
    while continueRoutine:
        # get current time
        t = Determine_stim_presentation_timeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Determine_stim_presentation_timeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Determine_stim_presentation_timeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Determine_stim_presentation_time"-------
    for thisComponent in Determine_stim_presentation_timeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    round_number += 1
    last_stim = 0
    thisExp.addData('round_number', round_number)
    # the Routine "Determine_stim_presentation_time" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trial_loop = data.TrialHandler(nReps=Trial_repeats, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Trial_loop')
    thisExp.addLoop(Trial_loop)  # add the loop to the experiment
    thisTrial_loop = Trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    for thisTrial_loop in Trial_loop:
        currentLoop = Trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
        if thisTrial_loop != None:
            for paramName in thisTrial_loop:
                exec('{} = thisTrial_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Trial_screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Do not change presentation duration of stimulus
        if change_pres_duration == 0:
            change_pres_duration = pres_duration
        #change Presentation duration of stimulus
        elif change_pres_duration == 1:
            if Block_Loop.thisRepN == 0:
                change_pres_duration = pres_duration #This is a practice block, so it equals to block number 1
            elif Block_Loop.thisRepN == 1:
                change_pres_duration = pres_duration #This is the presentation duration of block number 1
            elif Block_Loop.thisRepN == 2:
                change_pres_duration = pres_duration - 0.4 #This is the presentation duration of block number 2
            elif Block_Loop.thisRepN == 3:
                change_pres_duration = pres_duration - 0.8 #This is the presentation duration of block number 3
            elif Block_Loop.thisRepN == 4:
                change_pres_duration = pres_duration - 1.2 #This is the presentation duration of block number 4
        import random
        numbers = random.choice(["1.wav", "2.wav","3.wav","4.wav","5.wav","6.wav","7.wav","8.wav","9.wav"])
        
        if numbers == "1.wav": 
            current_stim = 1
        elif numbers == "2.wav": 
            current_stim = 2
        elif numbers == "3.wav": 
            current_stim = 3
        elif numbers == "4.wav": 
            current_stim = 4
        elif numbers == "5.wav": 
            current_stim = 5
        elif numbers == "6.wav": 
            current_stim = 6
        elif numbers == "7.wav": 
            current_stim = 7
        elif numbers == "8.wav": 
            current_stim = 8
        elif numbers == "9.wav": 
            current_stim = 9
        
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        valid_stim = current_stim + last_stim
        sound_1.setSound('1.wav', secs=2.4, hamming=True)
        sound_1.setVolume(1, log=False)
        sound_2.setSound('2.wav', secs=1.0, hamming=True)
        sound_2.setVolume(1, log=False)
        sound_3.setSound('3.wav', secs=1.0, hamming=True)
        sound_3.setVolume(1, log=False)
        sound_4.setSound('4.wav', secs=1.0, hamming=True)
        sound_4.setVolume(1, log=False)
        sound_5.setSound('5.wav', secs=1.0, hamming=True)
        sound_5.setVolume(1, log=False)
        sound_6.setSound('6.wav', secs=1.0, hamming=True)
        sound_6.setVolume(1, log=False)
        sound_7.setSound('7.wav', secs=1.0, hamming=True)
        sound_7.setVolume(1, log=False)
        sound_8.setSound('8.wav', secs=1.0, hamming=True)
        sound_8.setVolume(1, log=False)
        sound_9.setSound('9.wav', secs=1.0, hamming=True)
        sound_9.setVolume(1, log=False)
        # keep track of which components have finished
        Trial_screenComponents = [mouse, block_1, text_1, sound_1, block_2, text_2, sound_2, block_3, text_3, sound_3, block_4, text_4, sound_4, block_5, text_5, sound_5, block_6, text_6, sound_6, block_7, text_7, sound_7, block_8, text_8, sound_8, block_9, text_9, sound_9, block_10, text_10, block_11, text_11, block_12, text_12, block_13, text_13, block_14, text_14, block_15, text_15, block_16, text_16, block_17, text_17, block_18, text_18]
        for thisComponent in Trial_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Trial_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trial_screen"-------
        while continueRoutine:
            # get current time
            t = Trial_screenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Trial_screenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #beëindig routine als pres_tijd voorbij is
            if t >= pres_duration:
                continueRoutine = False
            # *mouse* updates
            if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse.tStop = t  # not accounting for scr refresh
                    mouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                    mouse.status = FINISHED
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [block_1,block_2,block_3,block_4,block_5,block_6, block_7, block_8,block_9,block_10,block_11,block_12,block_13,block_14,block_15,block_16, block_17, block_18]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *block_1* updates
            if block_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_1.frameNStart = frameN  # exact frame index
                block_1.tStart = t  # local t and not account for scr refresh
                block_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_1, 'tStartRefresh')  # time at next scr refresh
                block_1.setAutoDraw(True)
            if block_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_1.tStop = t  # not accounting for scr refresh
                    block_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_1, 'tStopRefresh')  # time at next scr refresh
                    block_1.setAutoDraw(False)
            
            # *text_1* updates
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                text_1.setAutoDraw(True)
            if text_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_1.tStop = t  # not accounting for scr refresh
                    text_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_1, 'tStopRefresh')  # time at next scr refresh
                    text_1.setAutoDraw(False)
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and current_stim == 1:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()
            
            # *block_2* updates
            if block_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_2.frameNStart = frameN  # exact frame index
                block_2.tStart = t  # local t and not account for scr refresh
                block_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_2, 'tStartRefresh')  # time at next scr refresh
                block_2.setAutoDraw(True)
            if block_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_2.tStop = t  # not accounting for scr refresh
                    block_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_2, 'tStopRefresh')  # time at next scr refresh
                    block_2.setAutoDraw(False)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            # start/stop sound_2
            if sound_2.status == NOT_STARTED and current_stim ==2:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                sound_2.play(when=win)  # sync with win flip
            if sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_2.tStop = t  # not accounting for scr refresh
                    sound_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                    sound_2.stop()
            
            # *block_3* updates
            if block_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_3.frameNStart = frameN  # exact frame index
                block_3.tStart = t  # local t and not account for scr refresh
                block_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_3, 'tStartRefresh')  # time at next scr refresh
                block_3.setAutoDraw(True)
            if block_3.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_3.tStop = t  # not accounting for scr refresh
                    block_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_3, 'tStopRefresh')  # time at next scr refresh
                    block_3.setAutoDraw(False)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(False)
            # start/stop sound_3
            if sound_3.status == NOT_STARTED and current_stim == 3:
                # keep track of start time/frame for later
                sound_3.frameNStart = frameN  # exact frame index
                sound_3.tStart = t  # local t and not account for scr refresh
                sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                sound_3.play(when=win)  # sync with win flip
            if sound_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_3.tStop = t  # not accounting for scr refresh
                    sound_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                    sound_3.stop()
            
            # *block_4* updates
            if block_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_4.frameNStart = frameN  # exact frame index
                block_4.tStart = t  # local t and not account for scr refresh
                block_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_4, 'tStartRefresh')  # time at next scr refresh
                block_4.setAutoDraw(True)
            if block_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_4.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_4.tStop = t  # not accounting for scr refresh
                    block_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_4, 'tStopRefresh')  # time at next scr refresh
                    block_4.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            # start/stop sound_4
            if sound_4.status == NOT_STARTED and current_stim == 4:
                # keep track of start time/frame for later
                sound_4.frameNStart = frameN  # exact frame index
                sound_4.tStart = t  # local t and not account for scr refresh
                sound_4.tStartRefresh = tThisFlipGlobal  # on global time
                sound_4.play(when=win)  # sync with win flip
            if sound_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_4.tStop = t  # not accounting for scr refresh
                    sound_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                    sound_4.stop()
            
            # *block_5* updates
            if block_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_5.frameNStart = frameN  # exact frame index
                block_5.tStart = t  # local t and not account for scr refresh
                block_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_5, 'tStartRefresh')  # time at next scr refresh
                block_5.setAutoDraw(True)
            if block_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_5.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_5.tStop = t  # not accounting for scr refresh
                    block_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_5, 'tStopRefresh')  # time at next scr refresh
                    block_5.setAutoDraw(False)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            # start/stop sound_5
            if sound_5.status == NOT_STARTED and current_stim == 5:
                # keep track of start time/frame for later
                sound_5.frameNStart = frameN  # exact frame index
                sound_5.tStart = t  # local t and not account for scr refresh
                sound_5.tStartRefresh = tThisFlipGlobal  # on global time
                sound_5.play(when=win)  # sync with win flip
            if sound_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_5.tStop = t  # not accounting for scr refresh
                    sound_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_5, 'tStopRefresh')  # time at next scr refresh
                    sound_5.stop()
            
            # *block_6* updates
            if block_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_6.frameNStart = frameN  # exact frame index
                block_6.tStart = t  # local t and not account for scr refresh
                block_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_6, 'tStartRefresh')  # time at next scr refresh
                block_6.setAutoDraw(True)
            if block_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_6.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_6.tStop = t  # not accounting for scr refresh
                    block_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_6, 'tStopRefresh')  # time at next scr refresh
                    block_6.setAutoDraw(False)
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            # start/stop sound_6
            if sound_6.status == NOT_STARTED and current_stim == 6:
                # keep track of start time/frame for later
                sound_6.frameNStart = frameN  # exact frame index
                sound_6.tStart = t  # local t and not account for scr refresh
                sound_6.tStartRefresh = tThisFlipGlobal  # on global time
                sound_6.play(when=win)  # sync with win flip
            if sound_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_6.tStop = t  # not accounting for scr refresh
                    sound_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                    sound_6.stop()
            
            # *block_7* updates
            if block_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_7.frameNStart = frameN  # exact frame index
                block_7.tStart = t  # local t and not account for scr refresh
                block_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_7, 'tStartRefresh')  # time at next scr refresh
                block_7.setAutoDraw(True)
            if block_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_7.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_7.tStop = t  # not accounting for scr refresh
                    block_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_7, 'tStopRefresh')  # time at next scr refresh
                    block_7.setAutoDraw(False)
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            # start/stop sound_7
            if sound_7.status == NOT_STARTED and current_stim == 7:
                # keep track of start time/frame for later
                sound_7.frameNStart = frameN  # exact frame index
                sound_7.tStart = t  # local t and not account for scr refresh
                sound_7.tStartRefresh = tThisFlipGlobal  # on global time
                sound_7.play(when=win)  # sync with win flip
            if sound_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_7.tStop = t  # not accounting for scr refresh
                    sound_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                    sound_7.stop()
            
            # *block_8* updates
            if block_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_8.frameNStart = frameN  # exact frame index
                block_8.tStart = t  # local t and not account for scr refresh
                block_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_8, 'tStartRefresh')  # time at next scr refresh
                block_8.setAutoDraw(True)
            if block_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_8.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_8.tStop = t  # not accounting for scr refresh
                    block_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_8, 'tStopRefresh')  # time at next scr refresh
                    block_8.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            # start/stop sound_8
            if sound_8.status == NOT_STARTED and current_stim == 8:
                # keep track of start time/frame for later
                sound_8.frameNStart = frameN  # exact frame index
                sound_8.tStart = t  # local t and not account for scr refresh
                sound_8.tStartRefresh = tThisFlipGlobal  # on global time
                sound_8.play(when=win)  # sync with win flip
            if sound_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_8.tStop = t  # not accounting for scr refresh
                    sound_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                    sound_8.stop()
            
            # *block_9* updates
            if block_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_9.frameNStart = frameN  # exact frame index
                block_9.tStart = t  # local t and not account for scr refresh
                block_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_9, 'tStartRefresh')  # time at next scr refresh
                block_9.setAutoDraw(True)
            if block_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_9.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_9.tStop = t  # not accounting for scr refresh
                    block_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_9, 'tStopRefresh')  # time at next scr refresh
                    block_9.setAutoDraw(False)
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(False)
            # start/stop sound_9
            if sound_9.status == NOT_STARTED and current_stim == 9:
                # keep track of start time/frame for later
                sound_9.frameNStart = frameN  # exact frame index
                sound_9.tStart = t  # local t and not account for scr refresh
                sound_9.tStartRefresh = tThisFlipGlobal  # on global time
                sound_9.play(when=win)  # sync with win flip
            if sound_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_9.tStop = t  # not accounting for scr refresh
                    sound_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                    sound_9.stop()
            
            # *block_10* updates
            if block_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_10.frameNStart = frameN  # exact frame index
                block_10.tStart = t  # local t and not account for scr refresh
                block_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_10, 'tStartRefresh')  # time at next scr refresh
                block_10.setAutoDraw(True)
            if block_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_10.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_10.tStop = t  # not accounting for scr refresh
                    block_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_10, 'tStopRefresh')  # time at next scr refresh
                    block_10.setAutoDraw(False)
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                    text_10.setAutoDraw(False)
            
            # *block_11* updates
            if block_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_11.frameNStart = frameN  # exact frame index
                block_11.tStart = t  # local t and not account for scr refresh
                block_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_11, 'tStartRefresh')  # time at next scr refresh
                block_11.setAutoDraw(True)
            if block_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_11.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_11.tStop = t  # not accounting for scr refresh
                    block_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_11, 'tStopRefresh')  # time at next scr refresh
                    block_11.setAutoDraw(False)
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                    text_11.setAutoDraw(False)
            
            # *block_12* updates
            if block_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_12.frameNStart = frameN  # exact frame index
                block_12.tStart = t  # local t and not account for scr refresh
                block_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_12, 'tStartRefresh')  # time at next scr refresh
                block_12.setAutoDraw(True)
            if block_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_12.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_12.tStop = t  # not accounting for scr refresh
                    block_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_12, 'tStopRefresh')  # time at next scr refresh
                    block_12.setAutoDraw(False)
            
            # *text_12* updates
            if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                text_12.setAutoDraw(True)
            if text_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_12.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_12.tStop = t  # not accounting for scr refresh
                    text_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                    text_12.setAutoDraw(False)
            
            # *block_13* updates
            if block_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_13.frameNStart = frameN  # exact frame index
                block_13.tStart = t  # local t and not account for scr refresh
                block_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_13, 'tStartRefresh')  # time at next scr refresh
                block_13.setAutoDraw(True)
            if block_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_13.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_13.tStop = t  # not accounting for scr refresh
                    block_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_13, 'tStopRefresh')  # time at next scr refresh
                    block_13.setAutoDraw(False)
            
            # *text_13* updates
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                text_13.setAutoDraw(True)
            if text_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_13.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_13.tStop = t  # not accounting for scr refresh
                    text_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                    text_13.setAutoDraw(False)
            
            # *block_14* updates
            if block_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_14.frameNStart = frameN  # exact frame index
                block_14.tStart = t  # local t and not account for scr refresh
                block_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_14, 'tStartRefresh')  # time at next scr refresh
                block_14.setAutoDraw(True)
            if block_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_14.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_14.tStop = t  # not accounting for scr refresh
                    block_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_14, 'tStopRefresh')  # time at next scr refresh
                    block_14.setAutoDraw(False)
            
            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            if text_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_14.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_14.tStop = t  # not accounting for scr refresh
                    text_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                    text_14.setAutoDraw(False)
            
            # *block_15* updates
            if block_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_15.frameNStart = frameN  # exact frame index
                block_15.tStart = t  # local t and not account for scr refresh
                block_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_15, 'tStartRefresh')  # time at next scr refresh
                block_15.setAutoDraw(True)
            if block_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_15.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_15.tStop = t  # not accounting for scr refresh
                    block_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_15, 'tStopRefresh')  # time at next scr refresh
                    block_15.setAutoDraw(False)
            
            # *text_15* updates
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                text_15.setAutoDraw(True)
            if text_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_15.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_15.tStop = t  # not accounting for scr refresh
                    text_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
                    text_15.setAutoDraw(False)
            
            # *block_16* updates
            if block_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_16.frameNStart = frameN  # exact frame index
                block_16.tStart = t  # local t and not account for scr refresh
                block_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_16, 'tStartRefresh')  # time at next scr refresh
                block_16.setAutoDraw(True)
            if block_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_16.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_16.tStop = t  # not accounting for scr refresh
                    block_16.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_16, 'tStopRefresh')  # time at next scr refresh
                    block_16.setAutoDraw(False)
            
            # *text_16* updates
            if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_16.frameNStart = frameN  # exact frame index
                text_16.tStart = t  # local t and not account for scr refresh
                text_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                text_16.setAutoDraw(True)
            if text_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_16.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_16.tStop = t  # not accounting for scr refresh
                    text_16.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                    text_16.setAutoDraw(False)
            
            # *block_17* updates
            if block_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_17.frameNStart = frameN  # exact frame index
                block_17.tStart = t  # local t and not account for scr refresh
                block_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_17, 'tStartRefresh')  # time at next scr refresh
                block_17.setAutoDraw(True)
            if block_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_17.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_17.tStop = t  # not accounting for scr refresh
                    block_17.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_17, 'tStopRefresh')  # time at next scr refresh
                    block_17.setAutoDraw(False)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                text_17.setAutoDraw(True)
            if text_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_17.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_17.tStop = t  # not accounting for scr refresh
                    text_17.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                    text_17.setAutoDraw(False)
            
            # *block_18* updates
            if block_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_18.frameNStart = frameN  # exact frame index
                block_18.tStart = t  # local t and not account for scr refresh
                block_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_18, 'tStartRefresh')  # time at next scr refresh
                block_18.setAutoDraw(True)
            if block_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > block_18.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    block_18.tStop = t  # not accounting for scr refresh
                    block_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block_18, 'tStopRefresh')  # time at next scr refresh
                    block_18.setAutoDraw(False)
            
            # *text_18* updates
            if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_18.frameNStart = frameN  # exact frame index
                text_18.tStart = t  # local t and not account for scr refresh
                text_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
                text_18.setAutoDraw(True)
            if text_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_18.tStartRefresh + pres_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_18.tStop = t  # not accounting for scr refresh
                    text_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                    text_18.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial_screen"-------
        for thisComponent in Trial_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if mouse.clicked_name == ['block_1']: 
            reg_resp = 1
        elif mouse.clicked_name == ['block_2']: 
            reg_resp = 2
        elif mouse.clicked_name == ['block_3']: 
            reg_resp = 3
        elif mouse.clicked_name == ['block_4']: 
            reg_resp = 4
        elif mouse.clicked_name == ['block_5']: 
            reg_resp = 5
        elif mouse.clicked_name == ['block_6']: 
            reg_resp = 6
        elif mouse.clicked_name == ['block_7']: 
            reg_resp = 7
        elif mouse.clicked_name == ['block_8']: 
            reg_resp = 8
        elif mouse.clicked_name == ['block_9']: 
            reg_resp = 9
        elif mouse.clicked_name == ['block_10']: 
            reg_resp = 10
        elif mouse.clicked_name == ['block_11']: 
            reg_resp = 11
        elif mouse.clicked_name == ['block_12']: 
            reg_resp = 12
        elif mouse.clicked_name == ['block_13']: 
            reg_resp = 13
        elif mouse.clicked_name == ['block_14']: 
            reg_resp = 14
        elif mouse.clicked_name == ['block_15']: 
            reg_resp = 15
        elif mouse.clicked_name == ['block_16']: 
            reg_resp = 16
        elif mouse.clicked_name == ['block_17']: 
            reg_resp = 17
        elif mouse.clicked_name == ['block_18']: 
            reg_resp = 18
        elif mouse.clicked_name == [ ]:
            reg_resp = 0
        
        thisExp.addData('reg_resp', reg_resp)
        thisExp.addData('current_stim', current_stim)
        # store data for Trial_loop (TrialHandler)
        if len(mouse.x): Trial_loop.addData('mouse.x', mouse.x[0])
        if len(mouse.y): Trial_loop.addData('mouse.y', mouse.y[0])
        if len(mouse.leftButton): Trial_loop.addData('mouse.leftButton', mouse.leftButton[0])
        if len(mouse.midButton): Trial_loop.addData('mouse.midButton', mouse.midButton[0])
        if len(mouse.rightButton): Trial_loop.addData('mouse.rightButton', mouse.rightButton[0])
        if len(mouse.time): Trial_loop.addData('mouse.time', mouse.time[0])
        if len(mouse.clicked_name): Trial_loop.addData('mouse.clicked_name', mouse.clicked_name[0])
        Trial_loop.addData('mouse.started', mouse.tStartRefresh)
        Trial_loop.addData('mouse.stopped', mouse.tStopRefresh)
        thisExp.addData('last_stim', last_stim)
        thisExp.addData('valid_stim', valid_stim)
        sound_1.stop()  # ensure sound has stopped at end of routine
        sound_2.stop()  # ensure sound has stopped at end of routine
        sound_3.stop()  # ensure sound has stopped at end of routine
        sound_4.stop()  # ensure sound has stopped at end of routine
        sound_5.stop()  # ensure sound has stopped at end of routine
        sound_6.stop()  # ensure sound has stopped at end of routine
        sound_7.stop()  # ensure sound has stopped at end of routine
        sound_8.stop()  # ensure sound has stopped at end of routine
        sound_9.stop()  # ensure sound has stopped at end of routine
        # the Routine "Trial_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        
        if face_score >= perfect: 
            feedback_smiley = 'emotie1.png'
        elif face_score >= good:
            feedback_smiley = 'emotie2.png'
        elif face_score >= okay:
            feedback_smiley = 'emotie3.png'
        elif face_score >= bad:
            feedback_smiley = 'emotie4.png'
        else:
            feedback_smiley = 'emotie5.png'
        
        if reg_resp == valid_stim:
            ansColor = 'green'
            feedback_text = 'right!'
            points = 1
            if Block_Loop.thisN != 0:
                face_score += 1
        else: 
            ansColor = 'red'
            feedback_text = 'wrong!'
            points = 0
            if Block_Loop.thisN != 0:
                face_score -= 1
        
        Feedback_image.setImage(feedback_smiley)
        FB_Text_block0.setColor(ansColor, colorSpace='rgb')
        FB_Text_block0.setText(feedback_text)
        FB_text_block1234.setColor(ansColor, colorSpace='rgb')
        FB_text_block1234.setText(feedback_text)
        # keep track of which components have finished
        Feedback_screenComponents = [Feedback_image, FB_Text_block0, FB_text_block1234, B_1_FB, T_1_FB, B_2_FB, T_2_FB, B_3_FB, T_3_FB, B_4_FB, T_4_FB, B_5_FB, T_5_FB, B_6_FB, T_6_FB, B_7_FB, T_7_FB, B_8_FB, T_8_FB, B_9_FB, T_9_FB, B_10_FB, T_10_FB, B_11_FB, T_11_FB, B_12_FB, T_12_FB, B_13_FB, T_13_FB, B_14_FB, T_14_FB, B_15_FB, T_15_FB, B_16_FB, T_16_FB, B_17_FB, T_17_FB, B_18_FB, T_18_FB]
        for thisComponent in Feedback_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Feedback_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback_screen"-------
        while continueRoutine:
            # get current time
            t = Feedback_screenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Feedback_screenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #if the time last longer than 1 second, continue with next trial
            if t >= 1:
                continueRoutine = False
            
            # *Feedback_image* updates
            if Feedback_image.status == NOT_STARTED and Block_Loop.thisN  != 0 and enable_facial_feedback == 1:
                # keep track of start time/frame for later
                Feedback_image.frameNStart = frameN  # exact frame index
                Feedback_image.tStart = t  # local t and not account for scr refresh
                Feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback_image, 'tStartRefresh')  # time at next scr refresh
                Feedback_image.setAutoDraw(True)
            if Feedback_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback_image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback_image.tStop = t  # not accounting for scr refresh
                    Feedback_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Feedback_image, 'tStopRefresh')  # time at next scr refresh
                    Feedback_image.setAutoDraw(False)
            
            # *FB_Text_block0* updates
            if FB_Text_block0.status == NOT_STARTED and Block_Loop.thisN  == 0 or enable_facial_feedback == 0:
                # keep track of start time/frame for later
                FB_Text_block0.frameNStart = frameN  # exact frame index
                FB_Text_block0.tStart = t  # local t and not account for scr refresh
                FB_Text_block0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FB_Text_block0, 'tStartRefresh')  # time at next scr refresh
                FB_Text_block0.setAutoDraw(True)
            if FB_Text_block0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FB_Text_block0.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FB_Text_block0.tStop = t  # not accounting for scr refresh
                    FB_Text_block0.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FB_Text_block0, 'tStopRefresh')  # time at next scr refresh
                    FB_Text_block0.setAutoDraw(False)
            
            # *FB_text_block1234* updates
            if FB_text_block1234.status == NOT_STARTED and Block_Loop.thisN  != 0 and enable_facial_feedback == 1:
                # keep track of start time/frame for later
                FB_text_block1234.frameNStart = frameN  # exact frame index
                FB_text_block1234.tStart = t  # local t and not account for scr refresh
                FB_text_block1234.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FB_text_block1234, 'tStartRefresh')  # time at next scr refresh
                FB_text_block1234.setAutoDraw(True)
            if FB_text_block1234.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FB_text_block1234.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FB_text_block1234.tStop = t  # not accounting for scr refresh
                    FB_text_block1234.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FB_text_block1234, 'tStopRefresh')  # time at next scr refresh
                    FB_text_block1234.setAutoDraw(False)
            
            # *B_1_FB* updates
            if B_1_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_1_FB.frameNStart = frameN  # exact frame index
                B_1_FB.tStart = t  # local t and not account for scr refresh
                B_1_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_1_FB, 'tStartRefresh')  # time at next scr refresh
                B_1_FB.setAutoDraw(True)
            if B_1_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_1_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_1_FB.tStop = t  # not accounting for scr refresh
                    B_1_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_1_FB, 'tStopRefresh')  # time at next scr refresh
                    B_1_FB.setAutoDraw(False)
            
            # *T_1_FB* updates
            if T_1_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_1_FB.frameNStart = frameN  # exact frame index
                T_1_FB.tStart = t  # local t and not account for scr refresh
                T_1_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_1_FB, 'tStartRefresh')  # time at next scr refresh
                T_1_FB.setAutoDraw(True)
            if T_1_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_1_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_1_FB.tStop = t  # not accounting for scr refresh
                    T_1_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_1_FB, 'tStopRefresh')  # time at next scr refresh
                    T_1_FB.setAutoDraw(False)
            
            # *B_2_FB* updates
            if B_2_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_2_FB.frameNStart = frameN  # exact frame index
                B_2_FB.tStart = t  # local t and not account for scr refresh
                B_2_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_2_FB, 'tStartRefresh')  # time at next scr refresh
                B_2_FB.setAutoDraw(True)
            if B_2_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_2_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_2_FB.tStop = t  # not accounting for scr refresh
                    B_2_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_2_FB, 'tStopRefresh')  # time at next scr refresh
                    B_2_FB.setAutoDraw(False)
            
            # *T_2_FB* updates
            if T_2_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_2_FB.frameNStart = frameN  # exact frame index
                T_2_FB.tStart = t  # local t and not account for scr refresh
                T_2_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_2_FB, 'tStartRefresh')  # time at next scr refresh
                T_2_FB.setAutoDraw(True)
            if T_2_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_2_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_2_FB.tStop = t  # not accounting for scr refresh
                    T_2_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_2_FB, 'tStopRefresh')  # time at next scr refresh
                    T_2_FB.setAutoDraw(False)
            
            # *B_3_FB* updates
            if B_3_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_3_FB.frameNStart = frameN  # exact frame index
                B_3_FB.tStart = t  # local t and not account for scr refresh
                B_3_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_3_FB, 'tStartRefresh')  # time at next scr refresh
                B_3_FB.setAutoDraw(True)
            if B_3_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_3_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_3_FB.tStop = t  # not accounting for scr refresh
                    B_3_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_3_FB, 'tStopRefresh')  # time at next scr refresh
                    B_3_FB.setAutoDraw(False)
            
            # *T_3_FB* updates
            if T_3_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_3_FB.frameNStart = frameN  # exact frame index
                T_3_FB.tStart = t  # local t and not account for scr refresh
                T_3_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_3_FB, 'tStartRefresh')  # time at next scr refresh
                T_3_FB.setAutoDraw(True)
            if T_3_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_3_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_3_FB.tStop = t  # not accounting for scr refresh
                    T_3_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_3_FB, 'tStopRefresh')  # time at next scr refresh
                    T_3_FB.setAutoDraw(False)
            
            # *B_4_FB* updates
            if B_4_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_4_FB.frameNStart = frameN  # exact frame index
                B_4_FB.tStart = t  # local t and not account for scr refresh
                B_4_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_4_FB, 'tStartRefresh')  # time at next scr refresh
                B_4_FB.setAutoDraw(True)
            if B_4_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_4_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_4_FB.tStop = t  # not accounting for scr refresh
                    B_4_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_4_FB, 'tStopRefresh')  # time at next scr refresh
                    B_4_FB.setAutoDraw(False)
            
            # *T_4_FB* updates
            if T_4_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_4_FB.frameNStart = frameN  # exact frame index
                T_4_FB.tStart = t  # local t and not account for scr refresh
                T_4_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_4_FB, 'tStartRefresh')  # time at next scr refresh
                T_4_FB.setAutoDraw(True)
            if T_4_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_4_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_4_FB.tStop = t  # not accounting for scr refresh
                    T_4_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_4_FB, 'tStopRefresh')  # time at next scr refresh
                    T_4_FB.setAutoDraw(False)
            
            # *B_5_FB* updates
            if B_5_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_5_FB.frameNStart = frameN  # exact frame index
                B_5_FB.tStart = t  # local t and not account for scr refresh
                B_5_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_5_FB, 'tStartRefresh')  # time at next scr refresh
                B_5_FB.setAutoDraw(True)
            if B_5_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_5_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_5_FB.tStop = t  # not accounting for scr refresh
                    B_5_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_5_FB, 'tStopRefresh')  # time at next scr refresh
                    B_5_FB.setAutoDraw(False)
            
            # *T_5_FB* updates
            if T_5_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_5_FB.frameNStart = frameN  # exact frame index
                T_5_FB.tStart = t  # local t and not account for scr refresh
                T_5_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_5_FB, 'tStartRefresh')  # time at next scr refresh
                T_5_FB.setAutoDraw(True)
            if T_5_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_5_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_5_FB.tStop = t  # not accounting for scr refresh
                    T_5_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_5_FB, 'tStopRefresh')  # time at next scr refresh
                    T_5_FB.setAutoDraw(False)
            
            # *B_6_FB* updates
            if B_6_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_6_FB.frameNStart = frameN  # exact frame index
                B_6_FB.tStart = t  # local t and not account for scr refresh
                B_6_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_6_FB, 'tStartRefresh')  # time at next scr refresh
                B_6_FB.setAutoDraw(True)
            if B_6_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_6_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_6_FB.tStop = t  # not accounting for scr refresh
                    B_6_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_6_FB, 'tStopRefresh')  # time at next scr refresh
                    B_6_FB.setAutoDraw(False)
            
            # *T_6_FB* updates
            if T_6_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_6_FB.frameNStart = frameN  # exact frame index
                T_6_FB.tStart = t  # local t and not account for scr refresh
                T_6_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_6_FB, 'tStartRefresh')  # time at next scr refresh
                T_6_FB.setAutoDraw(True)
            if T_6_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_6_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_6_FB.tStop = t  # not accounting for scr refresh
                    T_6_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_6_FB, 'tStopRefresh')  # time at next scr refresh
                    T_6_FB.setAutoDraw(False)
            
            # *B_7_FB* updates
            if B_7_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_7_FB.frameNStart = frameN  # exact frame index
                B_7_FB.tStart = t  # local t and not account for scr refresh
                B_7_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_7_FB, 'tStartRefresh')  # time at next scr refresh
                B_7_FB.setAutoDraw(True)
            if B_7_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_7_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_7_FB.tStop = t  # not accounting for scr refresh
                    B_7_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_7_FB, 'tStopRefresh')  # time at next scr refresh
                    B_7_FB.setAutoDraw(False)
            
            # *T_7_FB* updates
            if T_7_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_7_FB.frameNStart = frameN  # exact frame index
                T_7_FB.tStart = t  # local t and not account for scr refresh
                T_7_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_7_FB, 'tStartRefresh')  # time at next scr refresh
                T_7_FB.setAutoDraw(True)
            if T_7_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_7_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_7_FB.tStop = t  # not accounting for scr refresh
                    T_7_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_7_FB, 'tStopRefresh')  # time at next scr refresh
                    T_7_FB.setAutoDraw(False)
            
            # *B_8_FB* updates
            if B_8_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_8_FB.frameNStart = frameN  # exact frame index
                B_8_FB.tStart = t  # local t and not account for scr refresh
                B_8_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_8_FB, 'tStartRefresh')  # time at next scr refresh
                B_8_FB.setAutoDraw(True)
            if B_8_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_8_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_8_FB.tStop = t  # not accounting for scr refresh
                    B_8_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_8_FB, 'tStopRefresh')  # time at next scr refresh
                    B_8_FB.setAutoDraw(False)
            
            # *T_8_FB* updates
            if T_8_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_8_FB.frameNStart = frameN  # exact frame index
                T_8_FB.tStart = t  # local t and not account for scr refresh
                T_8_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_8_FB, 'tStartRefresh')  # time at next scr refresh
                T_8_FB.setAutoDraw(True)
            if T_8_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_8_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_8_FB.tStop = t  # not accounting for scr refresh
                    T_8_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_8_FB, 'tStopRefresh')  # time at next scr refresh
                    T_8_FB.setAutoDraw(False)
            
            # *B_9_FB* updates
            if B_9_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_9_FB.frameNStart = frameN  # exact frame index
                B_9_FB.tStart = t  # local t and not account for scr refresh
                B_9_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_9_FB, 'tStartRefresh')  # time at next scr refresh
                B_9_FB.setAutoDraw(True)
            if B_9_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_9_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_9_FB.tStop = t  # not accounting for scr refresh
                    B_9_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_9_FB, 'tStopRefresh')  # time at next scr refresh
                    B_9_FB.setAutoDraw(False)
            
            # *T_9_FB* updates
            if T_9_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_9_FB.frameNStart = frameN  # exact frame index
                T_9_FB.tStart = t  # local t and not account for scr refresh
                T_9_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_9_FB, 'tStartRefresh')  # time at next scr refresh
                T_9_FB.setAutoDraw(True)
            if T_9_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_9_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_9_FB.tStop = t  # not accounting for scr refresh
                    T_9_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_9_FB, 'tStopRefresh')  # time at next scr refresh
                    T_9_FB.setAutoDraw(False)
            
            # *B_10_FB* updates
            if B_10_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_10_FB.frameNStart = frameN  # exact frame index
                B_10_FB.tStart = t  # local t and not account for scr refresh
                B_10_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_10_FB, 'tStartRefresh')  # time at next scr refresh
                B_10_FB.setAutoDraw(True)
            if B_10_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_10_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_10_FB.tStop = t  # not accounting for scr refresh
                    B_10_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_10_FB, 'tStopRefresh')  # time at next scr refresh
                    B_10_FB.setAutoDraw(False)
            
            # *T_10_FB* updates
            if T_10_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_10_FB.frameNStart = frameN  # exact frame index
                T_10_FB.tStart = t  # local t and not account for scr refresh
                T_10_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_10_FB, 'tStartRefresh')  # time at next scr refresh
                T_10_FB.setAutoDraw(True)
            if T_10_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_10_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_10_FB.tStop = t  # not accounting for scr refresh
                    T_10_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_10_FB, 'tStopRefresh')  # time at next scr refresh
                    T_10_FB.setAutoDraw(False)
            
            # *B_11_FB* updates
            if B_11_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_11_FB.frameNStart = frameN  # exact frame index
                B_11_FB.tStart = t  # local t and not account for scr refresh
                B_11_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_11_FB, 'tStartRefresh')  # time at next scr refresh
                B_11_FB.setAutoDraw(True)
            if B_11_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_11_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_11_FB.tStop = t  # not accounting for scr refresh
                    B_11_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_11_FB, 'tStopRefresh')  # time at next scr refresh
                    B_11_FB.setAutoDraw(False)
            
            # *T_11_FB* updates
            if T_11_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_11_FB.frameNStart = frameN  # exact frame index
                T_11_FB.tStart = t  # local t and not account for scr refresh
                T_11_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_11_FB, 'tStartRefresh')  # time at next scr refresh
                T_11_FB.setAutoDraw(True)
            if T_11_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_11_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_11_FB.tStop = t  # not accounting for scr refresh
                    T_11_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_11_FB, 'tStopRefresh')  # time at next scr refresh
                    T_11_FB.setAutoDraw(False)
            
            # *B_12_FB* updates
            if B_12_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_12_FB.frameNStart = frameN  # exact frame index
                B_12_FB.tStart = t  # local t and not account for scr refresh
                B_12_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_12_FB, 'tStartRefresh')  # time at next scr refresh
                B_12_FB.setAutoDraw(True)
            if B_12_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_12_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_12_FB.tStop = t  # not accounting for scr refresh
                    B_12_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_12_FB, 'tStopRefresh')  # time at next scr refresh
                    B_12_FB.setAutoDraw(False)
            
            # *T_12_FB* updates
            if T_12_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_12_FB.frameNStart = frameN  # exact frame index
                T_12_FB.tStart = t  # local t and not account for scr refresh
                T_12_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_12_FB, 'tStartRefresh')  # time at next scr refresh
                T_12_FB.setAutoDraw(True)
            if T_12_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_12_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_12_FB.tStop = t  # not accounting for scr refresh
                    T_12_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_12_FB, 'tStopRefresh')  # time at next scr refresh
                    T_12_FB.setAutoDraw(False)
            
            # *B_13_FB* updates
            if B_13_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_13_FB.frameNStart = frameN  # exact frame index
                B_13_FB.tStart = t  # local t and not account for scr refresh
                B_13_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_13_FB, 'tStartRefresh')  # time at next scr refresh
                B_13_FB.setAutoDraw(True)
            if B_13_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_13_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_13_FB.tStop = t  # not accounting for scr refresh
                    B_13_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_13_FB, 'tStopRefresh')  # time at next scr refresh
                    B_13_FB.setAutoDraw(False)
            
            # *T_13_FB* updates
            if T_13_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_13_FB.frameNStart = frameN  # exact frame index
                T_13_FB.tStart = t  # local t and not account for scr refresh
                T_13_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_13_FB, 'tStartRefresh')  # time at next scr refresh
                T_13_FB.setAutoDraw(True)
            if T_13_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_13_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_13_FB.tStop = t  # not accounting for scr refresh
                    T_13_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_13_FB, 'tStopRefresh')  # time at next scr refresh
                    T_13_FB.setAutoDraw(False)
            
            # *B_14_FB* updates
            if B_14_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_14_FB.frameNStart = frameN  # exact frame index
                B_14_FB.tStart = t  # local t and not account for scr refresh
                B_14_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_14_FB, 'tStartRefresh')  # time at next scr refresh
                B_14_FB.setAutoDraw(True)
            if B_14_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_14_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_14_FB.tStop = t  # not accounting for scr refresh
                    B_14_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_14_FB, 'tStopRefresh')  # time at next scr refresh
                    B_14_FB.setAutoDraw(False)
            
            # *T_14_FB* updates
            if T_14_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_14_FB.frameNStart = frameN  # exact frame index
                T_14_FB.tStart = t  # local t and not account for scr refresh
                T_14_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_14_FB, 'tStartRefresh')  # time at next scr refresh
                T_14_FB.setAutoDraw(True)
            if T_14_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_14_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_14_FB.tStop = t  # not accounting for scr refresh
                    T_14_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_14_FB, 'tStopRefresh')  # time at next scr refresh
                    T_14_FB.setAutoDraw(False)
            
            # *B_15_FB* updates
            if B_15_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_15_FB.frameNStart = frameN  # exact frame index
                B_15_FB.tStart = t  # local t and not account for scr refresh
                B_15_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_15_FB, 'tStartRefresh')  # time at next scr refresh
                B_15_FB.setAutoDraw(True)
            if B_15_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_15_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_15_FB.tStop = t  # not accounting for scr refresh
                    B_15_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_15_FB, 'tStopRefresh')  # time at next scr refresh
                    B_15_FB.setAutoDraw(False)
            
            # *T_15_FB* updates
            if T_15_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_15_FB.frameNStart = frameN  # exact frame index
                T_15_FB.tStart = t  # local t and not account for scr refresh
                T_15_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_15_FB, 'tStartRefresh')  # time at next scr refresh
                T_15_FB.setAutoDraw(True)
            if T_15_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_15_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_15_FB.tStop = t  # not accounting for scr refresh
                    T_15_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_15_FB, 'tStopRefresh')  # time at next scr refresh
                    T_15_FB.setAutoDraw(False)
            
            # *B_16_FB* updates
            if B_16_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_16_FB.frameNStart = frameN  # exact frame index
                B_16_FB.tStart = t  # local t and not account for scr refresh
                B_16_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_16_FB, 'tStartRefresh')  # time at next scr refresh
                B_16_FB.setAutoDraw(True)
            if B_16_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_16_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_16_FB.tStop = t  # not accounting for scr refresh
                    B_16_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_16_FB, 'tStopRefresh')  # time at next scr refresh
                    B_16_FB.setAutoDraw(False)
            
            # *T_16_FB* updates
            if T_16_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_16_FB.frameNStart = frameN  # exact frame index
                T_16_FB.tStart = t  # local t and not account for scr refresh
                T_16_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_16_FB, 'tStartRefresh')  # time at next scr refresh
                T_16_FB.setAutoDraw(True)
            if T_16_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_16_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_16_FB.tStop = t  # not accounting for scr refresh
                    T_16_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_16_FB, 'tStopRefresh')  # time at next scr refresh
                    T_16_FB.setAutoDraw(False)
            
            # *B_17_FB* updates
            if B_17_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_17_FB.frameNStart = frameN  # exact frame index
                B_17_FB.tStart = t  # local t and not account for scr refresh
                B_17_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_17_FB, 'tStartRefresh')  # time at next scr refresh
                B_17_FB.setAutoDraw(True)
            if B_17_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_17_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_17_FB.tStop = t  # not accounting for scr refresh
                    B_17_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_17_FB, 'tStopRefresh')  # time at next scr refresh
                    B_17_FB.setAutoDraw(False)
            
            # *T_17_FB* updates
            if T_17_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_17_FB.frameNStart = frameN  # exact frame index
                T_17_FB.tStart = t  # local t and not account for scr refresh
                T_17_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_17_FB, 'tStartRefresh')  # time at next scr refresh
                T_17_FB.setAutoDraw(True)
            if T_17_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_17_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_17_FB.tStop = t  # not accounting for scr refresh
                    T_17_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_17_FB, 'tStopRefresh')  # time at next scr refresh
                    T_17_FB.setAutoDraw(False)
            
            # *B_18_FB* updates
            if B_18_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B_18_FB.frameNStart = frameN  # exact frame index
                B_18_FB.tStart = t  # local t and not account for scr refresh
                B_18_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B_18_FB, 'tStartRefresh')  # time at next scr refresh
                B_18_FB.setAutoDraw(True)
            if B_18_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B_18_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    B_18_FB.tStop = t  # not accounting for scr refresh
                    B_18_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B_18_FB, 'tStopRefresh')  # time at next scr refresh
                    B_18_FB.setAutoDraw(False)
            
            # *T_18_FB* updates
            if T_18_FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_18_FB.frameNStart = frameN  # exact frame index
                T_18_FB.tStart = t  # local t and not account for scr refresh
                T_18_FB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_18_FB, 'tStartRefresh')  # time at next scr refresh
                T_18_FB.setAutoDraw(True)
            if T_18_FB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_18_FB.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    T_18_FB.tStop = t  # not accounting for scr refresh
                    T_18_FB.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(T_18_FB, 'tStopRefresh')  # time at next scr refresh
                    T_18_FB.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_screen"-------
        for thisComponent in Feedback_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        last_stim = current_stim
        thisExp.addData('Score', points)
        Trial_loop.addData('Feedback_image.started', Feedback_image.tStartRefresh)
        Trial_loop.addData('Feedback_image.stopped', Feedback_image.tStopRefresh)
        # the Routine "Feedback_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed Trial_repeats repeats of 'Trial_loop'
    
    # get names of stimulus parameters
    if Trial_loop.trialList in ([], [None], None):
        params = []
    else:
        params = Trial_loop.trialList[0].keys()
    # save data for this loop
    Trial_loop.saveAsExcel(filename + '.xlsx', sheetName='Trial_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Rest_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the Rest_click
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Rest_screenComponents = [Rest_text, Rest_click]
    for thisComponent in Rest_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Rest_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rest_screen"-------
    while continueRoutine:
        # get current time
        t = Rest_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Rest_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Rest_text* updates
        if Rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Rest_text.frameNStart = frameN  # exact frame index
            Rest_text.tStart = t  # local t and not account for scr refresh
            Rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rest_text, 'tStartRefresh')  # time at next scr refresh
            Rest_text.setAutoDraw(True)
        # *Rest_click* updates
        if Rest_click.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Rest_click.frameNStart = frameN  # exact frame index
            Rest_click.tStart = t  # local t and not account for scr refresh
            Rest_click.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rest_click, 'tStartRefresh')  # time at next scr refresh
            Rest_click.status = STARTED
            Rest_click.mouseClock.reset()
            prevButtonState = Rest_click.getPressed()  # if button is down already this ISN'T a new click
        if Rest_click.status == STARTED:  # only update if started and not finished!
            buttons = Rest_click.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Rest_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest_screen"-------
    for thisComponent in Rest_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block_Loop.addData('Rest_text.started', Rest_text.tStartRefresh)
    Block_Loop.addData('Rest_text.stopped', Rest_text.tStopRefresh)
    # store data for Block_Loop (TrialHandler)
    x, y = Rest_click.getPos()
    buttons = Rest_click.getPressed()
    Block_Loop.addData('Rest_click.x', x)
    Block_Loop.addData('Rest_click.y', y)
    Block_Loop.addData('Rest_click.leftButton', buttons[0])
    Block_Loop.addData('Rest_click.midButton', buttons[1])
    Block_Loop.addData('Rest_click.rightButton', buttons[2])
    Block_Loop.addData('Rest_click.started', Rest_click.tStart)
    Block_Loop.addData('Rest_click.stopped', Rest_click.tStop)
    # the Routine "Rest_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5 repeats of 'Block_Loop'


# ------Prepare to start Routine "Final_screen"-------
continueRoutine = True
# update component parameters for each repeat
end_exp.keys = []
end_exp.rt = []
_end_exp_allKeys = []
# keep track of which components have finished
Final_screenComponents = [Thanks, end_exp]
for thisComponent in Final_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Final_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Final_screen"-------
while continueRoutine:
    # get current time
    t = Final_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Final_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.tStart = t  # local t and not account for scr refresh
        Thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
        Thanks.setAutoDraw(True)
    
    # *end_exp* updates
    waitOnFlip = False
    if end_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp.frameNStart = frameN  # exact frame index
        end_exp.tStart = t  # local t and not account for scr refresh
        end_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp, 'tStartRefresh')  # time at next scr refresh
        end_exp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_exp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_exp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_exp.status == STARTED and not waitOnFlip:
        theseKeys = end_exp.getKeys(keyList=['space'], waitRelease=False)
        _end_exp_allKeys.extend(theseKeys)
        if len(_end_exp_allKeys):
            end_exp.keys = _end_exp_allKeys[-1].name  # just the last key pressed
            end_exp.rt = _end_exp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Final_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Final_screen"-------
for thisComponent in Final_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_exp.keys in ['', [], None]:  # No response was made
    end_exp.keys = None
thisExp.addData('end_exp.keys',end_exp.keys)
if end_exp.keys != None:  # we had a response
    thisExp.addData('end_exp.rt', end_exp.rt)
thisExp.nextEntry()
# the Routine "Final_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.addData("globalClockTime", globalClock.getTime())
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
