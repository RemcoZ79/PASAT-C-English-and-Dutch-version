#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

Trial_herhalingen = 4 #hoe lang wil je 1 Trialblok laten duren

#Hoelang kan de respondent reageren op een stimulus, pas aan met duur in seconden
duur = 2.4 

#Wil je gezichten als feedback hebben of niet (0 is niet, 1 is wel)
gezichtsfeedback_aanzetten = 0

#Als verander_presentatietijd = 0, dan heeft elk blok dezelfde presentatietijd
#Als verander_presentatietijd = 1, dan verandert de presentatietijd van de stimulus elk blok
verander_presentatietijd = 1 

#op welke score begint de deelnemer?
gezicht_score = 1

#welke waarden zijn van belang bij de scoring? 

# als score perfect is, wordt de beste emotie getoond
# als de score boven perfect zit, wordt de hele blije smiley getoond
#als score goed is, wordt blije smiley getoond
# als score mwa is, wordt het neutrale gezicht getoond
# als score slecht is, wordt de verdrietige smiley getoond
#alles slechter dan dat geeft de boze smiley

perfect = 3
goed = 0
mwa = -3
slecht = -5

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'PASAT_NL'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

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

# Initialize components for Routine "Instructie_scherm"
Instructie_schermClock = core.Clock()
Klik_voor_doorgaan = event.Mouse(win=win)
x, y = [None, None]
Klik_voor_doorgaan.mouseClock = core.Clock()
instructie_tekst = visual.TextStim(win=win, name='instructie_tekst',
    text='U gaat zo een taak doen waarbij u cijfers hoort. \nHet doel is om de 2 meest recente cijfers bij elkaar op te tellen. \n\nEen voorbeeld: \nU hoort eerst een 2, vervolgens een 4. Dan klikt u op de 6. \nVervolgens hoort u een 8. Dit houdt in dat u de 4 en de 8 bij elkaar optelt. \nDit betekent dus dat u 12 moet aanklikken. \n\nMocht u het even kwijt zijn, stop dan met tellen en pak de draad weer op vanaf het volgende nummer. \n\nKlik met de computermuis om te starten. ',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Bepaal_tijden_voor_stimuluspresentatie"
Bepaal_tijden_voor_stimuluspresentatieClock = core.Clock()
ronde_nummer = 0
time_zero = core.monotonicClock.getTime()

# Initialize components for Routine "Trial_scherm"
Trial_schermClock = core.Clock()
muis = event.Mouse(win=win)
x, y = [None, None]
muis.mouseClock = core.Clock()
laatste_stim= 0
blok_1 = visual.Rect(
    win=win, name='blok_1',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
tekst_1 = visual.TextStim(win=win, name='tekst_1',
    text='1',
    font='Arial',
    pos=(0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
geluid_1 = sound.Sound('1_NL.wav', secs=-1, stereo=True, hamming=True,
    name='geluid_1')
geluid_1.setVolume(1)
blok_2 = visual.Rect(
    win=win, name='blok_2',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
tekst_2 = visual.TextStim(win=win, name='tekst_2',
    text='2',
    font='Arial',
    pos=(0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
geluid_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_2')
geluid_2.setVolume(1)
blok_3 = visual.Rect(
    win=win, name='blok_3',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
tekst_3 = visual.TextStim(win=win, name='tekst_3',
    text='3',
    font='Arial',
    pos=(0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
geluid_3 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_3')
geluid_3.setVolume(1)
blok_4 = visual.Rect(
    win=win, name='blok_4',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
tekst_4 = visual.TextStim(win=win, name='tekst_4',
    text='4',
    font='Arial',
    pos=(0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
geluid_4 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_4')
geluid_4.setVolume(1)
blok_5 = visual.Rect(
    win=win, name='blok_5',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
tekst_5 = visual.TextStim(win=win, name='tekst_5',
    text='5',
    font='Arial',
    pos=(0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
geluid_5 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_5')
geluid_5.setVolume(1)
blok_6 = visual.Rect(
    win=win, name='blok_6',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
tekst_6 = visual.TextStim(win=win, name='tekst_6',
    text='6',
    font='Arial',
    pos=(0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
geluid_6 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_6')
geluid_6.setVolume(1)
blok_7 = visual.Rect(
    win=win, name='blok_7',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-23.0, interpolate=True)
tekst_7 = visual.TextStim(win=win, name='tekst_7',
    text='7',
    font='Arial',
    pos=(0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
geluid_7 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_7')
geluid_7.setVolume(1)
blok_8 = visual.Rect(
    win=win, name='blok_8',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
tekst_8 = visual.TextStim(win=win, name='tekst_8',
    text='8',
    font='Arial',
    pos=(0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
geluid_8 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_8')
geluid_8.setVolume(1)
blok_9 = visual.Rect(
    win=win, name='blok_9',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-29.0, interpolate=True)
tekst_9 = visual.TextStim(win=win, name='tekst_9',
    text='9',
    font='Arial',
    pos=(0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
geluid_9 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='geluid_9')
geluid_9.setVolume(1)
blok_10 = visual.Rect(
    win=win, name='blok_10',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,-0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-32.0, interpolate=True)
tekst_10 = visual.TextStim(win=win, name='tekst_10',
    text='10',
    font='Arial',
    pos=(-0.05,-0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
blok_11 = visual.Rect(
    win=win, name='blok_11',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,-0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-34.0, interpolate=True)
tekst_11 = visual.TextStim(win=win, name='tekst_11',
    text='11',
    font='Arial',
    pos=(-0.15,-0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
blok_12 = visual.Rect(
    win=win, name='blok_12',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,-0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-36.0, interpolate=True)
tekst_12 = visual.TextStim(win=win, name='tekst_12',
    text='12',
    font='Arial',
    pos=(-0.232843,-0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-37.0);
blok_13 = visual.Rect(
    win=win, name='blok_13',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,-0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-38.0, interpolate=True)
tekst_13 = visual.TextStim(win=win, name='tekst_13',
    text='13',
    font='Arial',
    pos=(-0.29641,-0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-39.0);
blok_14 = visual.Rect(
    win=win, name='blok_14',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.35,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-40.0, interpolate=True)
tekst_14 = visual.TextStim(win=win, name='tekst_14',
    text='14',
    font='Arial',
    pos=(-0.35,0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-41.0);
blok_15 = visual.Rect(
    win=win, name='blok_15',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.29641,0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-42.0, interpolate=True)
tekst_15 = visual.TextStim(win=win, name='tekst_15',
    text='15',
    font='Arial',
    pos=(-0.29641,0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-43.0);
blok_16 = visual.Rect(
    win=win, name='blok_16',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.232843,0.182843),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-44.0, interpolate=True)
tekst_16 = visual.TextStim(win=win, name='tekst_16',
    text='16',
    font='Arial',
    pos=(-0.232843,0.182843), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-45.0);
blok_17 = visual.Rect(
    win=win, name='blok_17',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.15,0.24641),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-46.0, interpolate=True)
tekst_17 = visual.TextStim(win=win, name='tekst_17',
    text='17',
    font='Arial',
    pos=(-0.15,0.24641), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-47.0);
blok_18 = visual.Rect(
    win=win, name='blok_18',
    width=(0.08, 0.08)[0], height=(0.08, 0.08)[1],
    ori=0, pos=(-0.05,0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-48.0, interpolate=True)
tekst_18 = visual.TextStim(win=win, name='tekst_18',
    text='18',
    font='Arial',
    pos=(-0.05,0.3), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-49.0);

# Initialize components for Routine "Feedback_scherm"
Feedback_schermClock = core.Clock()
kleurAntw = ''

Smiley_plaatje = visual.ImageStim(
    win=win,
    name='Smiley_plaatje', 
    image='sin', mask=None,
    ori=0, pos=(0,-0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
FB_Tekst_B0 = visual.TextStim(win=win, name='FB_Tekst_B0',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
FB_tekst_B1234 = visual.TextStim(win=win, name='FB_tekst_B1234',
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

# Initialize components for Routine "Pauze_scherm"
Pauze_schermClock = core.Clock()
Pauze_Tekst = visual.TextStim(win=win, name='Pauze_Tekst',
    text='Het blok is nu voorbij, neem even pauze en klik met de muis om weer door te gaan. ',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Pauze_klik = event.Mouse(win=win)
x, y = [None, None]
Pauze_klik.mouseClock = core.Clock()

# Initialize components for Routine "Eind_scherm"
Eind_schermClock = core.Clock()
Bedankt = visual.TextStim(win=win, name='Bedankt',
    text='Dank voor uw deelname aan het onderzoek! \nU mag de onderzoeker informeren dat u klaar bent.',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beëindig_exp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructie_scherm"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the Klik_voor_doorgaan
gotValidClick = False  # until a click is received
# keep track of which components have finished
Instructie_schermComponents = [Klik_voor_doorgaan, instructie_tekst]
for thisComponent in Instructie_schermComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructie_schermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructie_scherm"-------
while continueRoutine:
    # get current time
    t = Instructie_schermClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructie_schermClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Klik_voor_doorgaan* updates
    if Klik_voor_doorgaan.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Klik_voor_doorgaan.frameNStart = frameN  # exact frame index
        Klik_voor_doorgaan.tStart = t  # local t and not account for scr refresh
        Klik_voor_doorgaan.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Klik_voor_doorgaan, 'tStartRefresh')  # time at next scr refresh
        Klik_voor_doorgaan.status = STARTED
        Klik_voor_doorgaan.mouseClock.reset()
        prevButtonState = Klik_voor_doorgaan.getPressed()  # if button is down already this ISN'T a new click
    if Klik_voor_doorgaan.status == STARTED:  # only update if started and not finished!
        buttons = Klik_voor_doorgaan.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *instructie_tekst* updates
    if instructie_tekst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructie_tekst.frameNStart = frameN  # exact frame index
        instructie_tekst.tStart = t  # local t and not account for scr refresh
        instructie_tekst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructie_tekst, 'tStartRefresh')  # time at next scr refresh
        instructie_tekst.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructie_schermComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructie_scherm"-------
for thisComponent in Instructie_schermComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructie_tekst.started', instructie_tekst.tStartRefresh)
thisExp.addData('instructie_tekst.stopped', instructie_tekst.tStopRefresh)
# the Routine "Instructie_scherm" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blok_Loop = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blok_Loop')
thisExp.addLoop(Blok_Loop)  # add the loop to the experiment
thisBlok_Loop = Blok_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlok_Loop.rgb)
if thisBlok_Loop != None:
    for paramName in thisBlok_Loop:
        exec('{} = thisBlok_Loop[paramName]'.format(paramName))

for thisBlok_Loop in Blok_Loop:
    currentLoop = Blok_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlok_Loop.rgb)
    if thisBlok_Loop != None:
        for paramName in thisBlok_Loop:
            exec('{} = thisBlok_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Bepaal_tijden_voor_stimuluspresentatie"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Bepaal_tijden_voor_stimuluspresentatieComponents = []
    for thisComponent in Bepaal_tijden_voor_stimuluspresentatieComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Bepaal_tijden_voor_stimuluspresentatieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Bepaal_tijden_voor_stimuluspresentatie"-------
    while continueRoutine:
        # get current time
        t = Bepaal_tijden_voor_stimuluspresentatieClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Bepaal_tijden_voor_stimuluspresentatieClock)
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
        for thisComponent in Bepaal_tijden_voor_stimuluspresentatieComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Bepaal_tijden_voor_stimuluspresentatie"-------
    for thisComponent in Bepaal_tijden_voor_stimuluspresentatieComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ronde_nummer += 1
    laatste_stim = 0
    thisExp.addData('ronde', ronde_nummer)
    # the Routine "Bepaal_tijden_voor_stimuluspresentatie" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trial_loop = data.TrialHandler(nReps=Trial_herhalingen, method='random', 
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
        
        # ------Prepare to start Routine "Trial_scherm"-------
        continueRoutine = True
        # update component parameters for each repeat
        if verander_presentatietijd ==0:
            pres_tijd = duur
        elif verander_presentatietijd ==1:
            if Blok_Loop.thisRepN == 0:
                pres_tijd = duur #oefenblok, dus duur is gelijk aan blok 1
            elif Blok_Loop.thisRepN == 1:
                pres_tijd = duur #blok 1 tijd om te reageren
            elif Blok_Loop.thisRepN == 2:
                pres_tijd = duur - 0.4 #blok 2 tijd om te reageren
            elif Blok_Loop.thisRepN == 3:
                pres_tijd = duur - 0.8 #blok 3 tijd om te reageren
            elif Blok_Loop.thisRepN == 4:
                pres_tijd = duur - 1.2 #blok 4 tijd om te reageren
        import random
        cijfers = random.choice(["1_NL.wav", "2_NL.wav","3_NL.wav","4_NL.wav","5_NL.wav","6_NL.wav","7_NL.wav","8_NL.wav","9_NL.wav"])
        
        if cijfers == "1_NL.wav": 
            huidige_stim = 1
        elif cijfers == "2_NL.wav": 
            huidige_stim = 2
        elif cijfers == "3_NL.wav": 
            huidige_stim = 3
        elif cijfers == "4_NL.wav": 
            huidige_stim = 4
        elif cijfers == "5_NL.wav": 
            huidige_stim = 5
        elif cijfers == "6_NL.wav": 
            huidige_stim = 6
        elif cijfers == "7_NL.wav": 
            huidige_stim = 7
        elif cijfers == "8_NL.wav": 
            huidige_stim = 8
        elif cijfers == "9_NL.wav": 
            huidige_stim = 9
        
        # setup some python lists for storing info about the muis
        muis.x = []
        muis.y = []
        muis.leftButton = []
        muis.midButton = []
        muis.rightButton = []
        muis.time = []
        muis.clicked_name = []
        gotValidClick = False  # until a click is received
        juiste_waarde = huidige_stim + laatste_stim
        geluid_1.setSound('1_NL.wav', secs=2.4, hamming=True)
        geluid_1.setVolume(1, log=False)
        geluid_2.setSound('2_NL.wav', secs=1.0, hamming=True)
        geluid_2.setVolume(1, log=False)
        geluid_3.setSound('3_NL.wav', secs=1.0, hamming=True)
        geluid_3.setVolume(1, log=False)
        geluid_4.setSound('4_NL.wav', secs=1.0, hamming=True)
        geluid_4.setVolume(1, log=False)
        geluid_5.setSound('5_NL.wav', secs=1.0, hamming=True)
        geluid_5.setVolume(1, log=False)
        geluid_6.setSound('6_NL.wav', secs=1.0, hamming=True)
        geluid_6.setVolume(1, log=False)
        geluid_7.setSound('7_NL.wav', secs=1.0, hamming=True)
        geluid_7.setVolume(1, log=False)
        geluid_8.setSound('8_NL.wav', secs=1.0, hamming=True)
        geluid_8.setVolume(1, log=False)
        geluid_9.setSound('9_NL.wav', secs=1.0, hamming=True)
        geluid_9.setVolume(1, log=False)
        # keep track of which components have finished
        Trial_schermComponents = [muis, blok_1, tekst_1, geluid_1, blok_2, tekst_2, geluid_2, blok_3, tekst_3, geluid_3, blok_4, tekst_4, geluid_4, blok_5, tekst_5, geluid_5, blok_6, tekst_6, geluid_6, blok_7, tekst_7, geluid_7, blok_8, tekst_8, geluid_8, blok_9, tekst_9, geluid_9, blok_10, tekst_10, blok_11, tekst_11, blok_12, tekst_12, blok_13, tekst_13, blok_14, tekst_14, blok_15, tekst_15, blok_16, tekst_16, blok_17, tekst_17, blok_18, tekst_18]
        for thisComponent in Trial_schermComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Trial_schermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trial_scherm"-------
        while continueRoutine:
            # get current time
            t = Trial_schermClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Trial_schermClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #beëindig routine als pres_tijd voorbij is
            if t >= pres_tijd:
                continueRoutine = False
            # *muis* updates
            if muis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                muis.frameNStart = frameN  # exact frame index
                muis.tStart = t  # local t and not account for scr refresh
                muis.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(muis, 'tStartRefresh')  # time at next scr refresh
                muis.status = STARTED
                muis.mouseClock.reset()
                prevButtonState = muis.getPressed()  # if button is down already this ISN'T a new click
            if muis.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    muis.tStop = t  # not accounting for scr refresh
                    muis.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(muis, 'tStopRefresh')  # time at next scr refresh
                    muis.status = FINISHED
            if muis.status == STARTED:  # only update if started and not finished!
                buttons = muis.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [blok_1,blok_2,blok_3,blok_4,blok_5,blok_6, blok_7, blok_8,blok_9,blok_10,blok_11,blok_12,blok_13,blok_14,blok_15,blok_16, blok_17, blok_18]:
                            if obj.contains(muis):
                                gotValidClick = True
                                muis.clicked_name.append(obj.name)
                        x, y = muis.getPos()
                        muis.x.append(x)
                        muis.y.append(y)
                        buttons = muis.getPressed()
                        muis.leftButton.append(buttons[0])
                        muis.midButton.append(buttons[1])
                        muis.rightButton.append(buttons[2])
                        muis.time.append(muis.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *blok_1* updates
            if blok_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_1.frameNStart = frameN  # exact frame index
                blok_1.tStart = t  # local t and not account for scr refresh
                blok_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_1, 'tStartRefresh')  # time at next scr refresh
                blok_1.setAutoDraw(True)
            if blok_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_1.tStop = t  # not accounting for scr refresh
                    blok_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_1, 'tStopRefresh')  # time at next scr refresh
                    blok_1.setAutoDraw(False)
            
            # *tekst_1* updates
            if tekst_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_1.frameNStart = frameN  # exact frame index
                tekst_1.tStart = t  # local t and not account for scr refresh
                tekst_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_1, 'tStartRefresh')  # time at next scr refresh
                tekst_1.setAutoDraw(True)
            if tekst_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_1.tStop = t  # not accounting for scr refresh
                    tekst_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_1, 'tStopRefresh')  # time at next scr refresh
                    tekst_1.setAutoDraw(False)
            # start/stop geluid_1
            if geluid_1.status == NOT_STARTED and huidige_stim == 1:
                # keep track of start time/frame for later
                geluid_1.frameNStart = frameN  # exact frame index
                geluid_1.tStart = t  # local t and not account for scr refresh
                geluid_1.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_1.play(when=win)  # sync with win flip
            if geluid_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_1.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_1.tStop = t  # not accounting for scr refresh
                    geluid_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_1, 'tStopRefresh')  # time at next scr refresh
                    geluid_1.stop()
            
            # *blok_2* updates
            if blok_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_2.frameNStart = frameN  # exact frame index
                blok_2.tStart = t  # local t and not account for scr refresh
                blok_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_2, 'tStartRefresh')  # time at next scr refresh
                blok_2.setAutoDraw(True)
            if blok_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_2.tStop = t  # not accounting for scr refresh
                    blok_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_2, 'tStopRefresh')  # time at next scr refresh
                    blok_2.setAutoDraw(False)
            
            # *tekst_2* updates
            if tekst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_2.frameNStart = frameN  # exact frame index
                tekst_2.tStart = t  # local t and not account for scr refresh
                tekst_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_2, 'tStartRefresh')  # time at next scr refresh
                tekst_2.setAutoDraw(True)
            if tekst_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_2.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_2.tStop = t  # not accounting for scr refresh
                    tekst_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_2, 'tStopRefresh')  # time at next scr refresh
                    tekst_2.setAutoDraw(False)
            # start/stop geluid_2
            if geluid_2.status == NOT_STARTED and huidige_stim == 2:
                # keep track of start time/frame for later
                geluid_2.frameNStart = frameN  # exact frame index
                geluid_2.tStart = t  # local t and not account for scr refresh
                geluid_2.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_2.play(when=win)  # sync with win flip
            if geluid_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_2.tStop = t  # not accounting for scr refresh
                    geluid_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_2, 'tStopRefresh')  # time at next scr refresh
                    geluid_2.stop()
            
            # *blok_3* updates
            if blok_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_3.frameNStart = frameN  # exact frame index
                blok_3.tStart = t  # local t and not account for scr refresh
                blok_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_3, 'tStartRefresh')  # time at next scr refresh
                blok_3.setAutoDraw(True)
            if blok_3.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_3.tStop = t  # not accounting for scr refresh
                    blok_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_3, 'tStopRefresh')  # time at next scr refresh
                    blok_3.setAutoDraw(False)
            
            # *tekst_3* updates
            if tekst_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_3.frameNStart = frameN  # exact frame index
                tekst_3.tStart = t  # local t and not account for scr refresh
                tekst_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_3, 'tStartRefresh')  # time at next scr refresh
                tekst_3.setAutoDraw(True)
            if tekst_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_3.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_3.tStop = t  # not accounting for scr refresh
                    tekst_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_3, 'tStopRefresh')  # time at next scr refresh
                    tekst_3.setAutoDraw(False)
            # start/stop geluid_3
            if geluid_3.status == NOT_STARTED and huidige_stim == 3:
                # keep track of start time/frame for later
                geluid_3.frameNStart = frameN  # exact frame index
                geluid_3.tStart = t  # local t and not account for scr refresh
                geluid_3.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_3.play(when=win)  # sync with win flip
            if geluid_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_3.tStop = t  # not accounting for scr refresh
                    geluid_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_3, 'tStopRefresh')  # time at next scr refresh
                    geluid_3.stop()
            
            # *blok_4* updates
            if blok_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_4.frameNStart = frameN  # exact frame index
                blok_4.tStart = t  # local t and not account for scr refresh
                blok_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_4, 'tStartRefresh')  # time at next scr refresh
                blok_4.setAutoDraw(True)
            if blok_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_4.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_4.tStop = t  # not accounting for scr refresh
                    blok_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_4, 'tStopRefresh')  # time at next scr refresh
                    blok_4.setAutoDraw(False)
            
            # *tekst_4* updates
            if tekst_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_4.frameNStart = frameN  # exact frame index
                tekst_4.tStart = t  # local t and not account for scr refresh
                tekst_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_4, 'tStartRefresh')  # time at next scr refresh
                tekst_4.setAutoDraw(True)
            if tekst_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_4.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_4.tStop = t  # not accounting for scr refresh
                    tekst_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_4, 'tStopRefresh')  # time at next scr refresh
                    tekst_4.setAutoDraw(False)
            # start/stop geluid_4
            if geluid_4.status == NOT_STARTED and huidige_stim == 4:
                # keep track of start time/frame for later
                geluid_4.frameNStart = frameN  # exact frame index
                geluid_4.tStart = t  # local t and not account for scr refresh
                geluid_4.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_4.play(when=win)  # sync with win flip
            if geluid_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_4.tStop = t  # not accounting for scr refresh
                    geluid_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_4, 'tStopRefresh')  # time at next scr refresh
                    geluid_4.stop()
            
            # *blok_5* updates
            if blok_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_5.frameNStart = frameN  # exact frame index
                blok_5.tStart = t  # local t and not account for scr refresh
                blok_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_5, 'tStartRefresh')  # time at next scr refresh
                blok_5.setAutoDraw(True)
            if blok_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_5.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_5.tStop = t  # not accounting for scr refresh
                    blok_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_5, 'tStopRefresh')  # time at next scr refresh
                    blok_5.setAutoDraw(False)
            
            # *tekst_5* updates
            if tekst_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_5.frameNStart = frameN  # exact frame index
                tekst_5.tStart = t  # local t and not account for scr refresh
                tekst_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_5, 'tStartRefresh')  # time at next scr refresh
                tekst_5.setAutoDraw(True)
            if tekst_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_5.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_5.tStop = t  # not accounting for scr refresh
                    tekst_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_5, 'tStopRefresh')  # time at next scr refresh
                    tekst_5.setAutoDraw(False)
            # start/stop geluid_5
            if geluid_5.status == NOT_STARTED and huidige_stim == 5:
                # keep track of start time/frame for later
                geluid_5.frameNStart = frameN  # exact frame index
                geluid_5.tStart = t  # local t and not account for scr refresh
                geluid_5.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_5.play(when=win)  # sync with win flip
            if geluid_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_5.tStop = t  # not accounting for scr refresh
                    geluid_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_5, 'tStopRefresh')  # time at next scr refresh
                    geluid_5.stop()
            
            # *blok_6* updates
            if blok_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_6.frameNStart = frameN  # exact frame index
                blok_6.tStart = t  # local t and not account for scr refresh
                blok_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_6, 'tStartRefresh')  # time at next scr refresh
                blok_6.setAutoDraw(True)
            if blok_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_6.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_6.tStop = t  # not accounting for scr refresh
                    blok_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_6, 'tStopRefresh')  # time at next scr refresh
                    blok_6.setAutoDraw(False)
            
            # *tekst_6* updates
            if tekst_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_6.frameNStart = frameN  # exact frame index
                tekst_6.tStart = t  # local t and not account for scr refresh
                tekst_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_6, 'tStartRefresh')  # time at next scr refresh
                tekst_6.setAutoDraw(True)
            if tekst_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_6.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_6.tStop = t  # not accounting for scr refresh
                    tekst_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_6, 'tStopRefresh')  # time at next scr refresh
                    tekst_6.setAutoDraw(False)
            # start/stop geluid_6
            if geluid_6.status == NOT_STARTED and huidige_stim == 6:
                # keep track of start time/frame for later
                geluid_6.frameNStart = frameN  # exact frame index
                geluid_6.tStart = t  # local t and not account for scr refresh
                geluid_6.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_6.play(when=win)  # sync with win flip
            if geluid_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_6.tStop = t  # not accounting for scr refresh
                    geluid_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_6, 'tStopRefresh')  # time at next scr refresh
                    geluid_6.stop()
            
            # *blok_7* updates
            if blok_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_7.frameNStart = frameN  # exact frame index
                blok_7.tStart = t  # local t and not account for scr refresh
                blok_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_7, 'tStartRefresh')  # time at next scr refresh
                blok_7.setAutoDraw(True)
            if blok_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_7.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_7.tStop = t  # not accounting for scr refresh
                    blok_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_7, 'tStopRefresh')  # time at next scr refresh
                    blok_7.setAutoDraw(False)
            
            # *tekst_7* updates
            if tekst_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_7.frameNStart = frameN  # exact frame index
                tekst_7.tStart = t  # local t and not account for scr refresh
                tekst_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_7, 'tStartRefresh')  # time at next scr refresh
                tekst_7.setAutoDraw(True)
            if tekst_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_7.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_7.tStop = t  # not accounting for scr refresh
                    tekst_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_7, 'tStopRefresh')  # time at next scr refresh
                    tekst_7.setAutoDraw(False)
            # start/stop geluid_7
            if geluid_7.status == NOT_STARTED and huidige_stim == 7:
                # keep track of start time/frame for later
                geluid_7.frameNStart = frameN  # exact frame index
                geluid_7.tStart = t  # local t and not account for scr refresh
                geluid_7.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_7.play(when=win)  # sync with win flip
            if geluid_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_7.tStop = t  # not accounting for scr refresh
                    geluid_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_7, 'tStopRefresh')  # time at next scr refresh
                    geluid_7.stop()
            
            # *blok_8* updates
            if blok_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_8.frameNStart = frameN  # exact frame index
                blok_8.tStart = t  # local t and not account for scr refresh
                blok_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_8, 'tStartRefresh')  # time at next scr refresh
                blok_8.setAutoDraw(True)
            if blok_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_8.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_8.tStop = t  # not accounting for scr refresh
                    blok_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_8, 'tStopRefresh')  # time at next scr refresh
                    blok_8.setAutoDraw(False)
            
            # *tekst_8* updates
            if tekst_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_8.frameNStart = frameN  # exact frame index
                tekst_8.tStart = t  # local t and not account for scr refresh
                tekst_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_8, 'tStartRefresh')  # time at next scr refresh
                tekst_8.setAutoDraw(True)
            if tekst_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_8.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_8.tStop = t  # not accounting for scr refresh
                    tekst_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_8, 'tStopRefresh')  # time at next scr refresh
                    tekst_8.setAutoDraw(False)
            # start/stop geluid_8
            if geluid_8.status == NOT_STARTED and huidige_stim == 8:
                # keep track of start time/frame for later
                geluid_8.frameNStart = frameN  # exact frame index
                geluid_8.tStart = t  # local t and not account for scr refresh
                geluid_8.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_8.play(when=win)  # sync with win flip
            if geluid_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_8.tStop = t  # not accounting for scr refresh
                    geluid_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_8, 'tStopRefresh')  # time at next scr refresh
                    geluid_8.stop()
            
            # *blok_9* updates
            if blok_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_9.frameNStart = frameN  # exact frame index
                blok_9.tStart = t  # local t and not account for scr refresh
                blok_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_9, 'tStartRefresh')  # time at next scr refresh
                blok_9.setAutoDraw(True)
            if blok_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_9.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_9.tStop = t  # not accounting for scr refresh
                    blok_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_9, 'tStopRefresh')  # time at next scr refresh
                    blok_9.setAutoDraw(False)
            
            # *tekst_9* updates
            if tekst_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_9.frameNStart = frameN  # exact frame index
                tekst_9.tStart = t  # local t and not account for scr refresh
                tekst_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_9, 'tStartRefresh')  # time at next scr refresh
                tekst_9.setAutoDraw(True)
            if tekst_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_9.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_9.tStop = t  # not accounting for scr refresh
                    tekst_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_9, 'tStopRefresh')  # time at next scr refresh
                    tekst_9.setAutoDraw(False)
            # start/stop geluid_9
            if geluid_9.status == NOT_STARTED and huidige_stim == 9:
                # keep track of start time/frame for later
                geluid_9.frameNStart = frameN  # exact frame index
                geluid_9.tStart = t  # local t and not account for scr refresh
                geluid_9.tStartRefresh = tThisFlipGlobal  # on global time
                geluid_9.play(when=win)  # sync with win flip
            if geluid_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > geluid_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    geluid_9.tStop = t  # not accounting for scr refresh
                    geluid_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(geluid_9, 'tStopRefresh')  # time at next scr refresh
                    geluid_9.stop()
            
            # *blok_10* updates
            if blok_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_10.frameNStart = frameN  # exact frame index
                blok_10.tStart = t  # local t and not account for scr refresh
                blok_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_10, 'tStartRefresh')  # time at next scr refresh
                blok_10.setAutoDraw(True)
            if blok_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_10.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_10.tStop = t  # not accounting for scr refresh
                    blok_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_10, 'tStopRefresh')  # time at next scr refresh
                    blok_10.setAutoDraw(False)
            
            # *tekst_10* updates
            if tekst_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_10.frameNStart = frameN  # exact frame index
                tekst_10.tStart = t  # local t and not account for scr refresh
                tekst_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_10, 'tStartRefresh')  # time at next scr refresh
                tekst_10.setAutoDraw(True)
            if tekst_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_10.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_10.tStop = t  # not accounting for scr refresh
                    tekst_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_10, 'tStopRefresh')  # time at next scr refresh
                    tekst_10.setAutoDraw(False)
            
            # *blok_11* updates
            if blok_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_11.frameNStart = frameN  # exact frame index
                blok_11.tStart = t  # local t and not account for scr refresh
                blok_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_11, 'tStartRefresh')  # time at next scr refresh
                blok_11.setAutoDraw(True)
            if blok_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_11.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_11.tStop = t  # not accounting for scr refresh
                    blok_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_11, 'tStopRefresh')  # time at next scr refresh
                    blok_11.setAutoDraw(False)
            
            # *tekst_11* updates
            if tekst_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_11.frameNStart = frameN  # exact frame index
                tekst_11.tStart = t  # local t and not account for scr refresh
                tekst_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_11, 'tStartRefresh')  # time at next scr refresh
                tekst_11.setAutoDraw(True)
            if tekst_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_11.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_11.tStop = t  # not accounting for scr refresh
                    tekst_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_11, 'tStopRefresh')  # time at next scr refresh
                    tekst_11.setAutoDraw(False)
            
            # *blok_12* updates
            if blok_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_12.frameNStart = frameN  # exact frame index
                blok_12.tStart = t  # local t and not account for scr refresh
                blok_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_12, 'tStartRefresh')  # time at next scr refresh
                blok_12.setAutoDraw(True)
            if blok_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_12.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_12.tStop = t  # not accounting for scr refresh
                    blok_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_12, 'tStopRefresh')  # time at next scr refresh
                    blok_12.setAutoDraw(False)
            
            # *tekst_12* updates
            if tekst_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_12.frameNStart = frameN  # exact frame index
                tekst_12.tStart = t  # local t and not account for scr refresh
                tekst_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_12, 'tStartRefresh')  # time at next scr refresh
                tekst_12.setAutoDraw(True)
            if tekst_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_12.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_12.tStop = t  # not accounting for scr refresh
                    tekst_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_12, 'tStopRefresh')  # time at next scr refresh
                    tekst_12.setAutoDraw(False)
            
            # *blok_13* updates
            if blok_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_13.frameNStart = frameN  # exact frame index
                blok_13.tStart = t  # local t and not account for scr refresh
                blok_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_13, 'tStartRefresh')  # time at next scr refresh
                blok_13.setAutoDraw(True)
            if blok_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_13.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_13.tStop = t  # not accounting for scr refresh
                    blok_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_13, 'tStopRefresh')  # time at next scr refresh
                    blok_13.setAutoDraw(False)
            
            # *tekst_13* updates
            if tekst_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_13.frameNStart = frameN  # exact frame index
                tekst_13.tStart = t  # local t and not account for scr refresh
                tekst_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_13, 'tStartRefresh')  # time at next scr refresh
                tekst_13.setAutoDraw(True)
            if tekst_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_13.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_13.tStop = t  # not accounting for scr refresh
                    tekst_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_13, 'tStopRefresh')  # time at next scr refresh
                    tekst_13.setAutoDraw(False)
            
            # *blok_14* updates
            if blok_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_14.frameNStart = frameN  # exact frame index
                blok_14.tStart = t  # local t and not account for scr refresh
                blok_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_14, 'tStartRefresh')  # time at next scr refresh
                blok_14.setAutoDraw(True)
            if blok_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_14.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_14.tStop = t  # not accounting for scr refresh
                    blok_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_14, 'tStopRefresh')  # time at next scr refresh
                    blok_14.setAutoDraw(False)
            
            # *tekst_14* updates
            if tekst_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_14.frameNStart = frameN  # exact frame index
                tekst_14.tStart = t  # local t and not account for scr refresh
                tekst_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_14, 'tStartRefresh')  # time at next scr refresh
                tekst_14.setAutoDraw(True)
            if tekst_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_14.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_14.tStop = t  # not accounting for scr refresh
                    tekst_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_14, 'tStopRefresh')  # time at next scr refresh
                    tekst_14.setAutoDraw(False)
            
            # *blok_15* updates
            if blok_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_15.frameNStart = frameN  # exact frame index
                blok_15.tStart = t  # local t and not account for scr refresh
                blok_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_15, 'tStartRefresh')  # time at next scr refresh
                blok_15.setAutoDraw(True)
            if blok_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_15.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_15.tStop = t  # not accounting for scr refresh
                    blok_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_15, 'tStopRefresh')  # time at next scr refresh
                    blok_15.setAutoDraw(False)
            
            # *tekst_15* updates
            if tekst_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_15.frameNStart = frameN  # exact frame index
                tekst_15.tStart = t  # local t and not account for scr refresh
                tekst_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_15, 'tStartRefresh')  # time at next scr refresh
                tekst_15.setAutoDraw(True)
            if tekst_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_15.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_15.tStop = t  # not accounting for scr refresh
                    tekst_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_15, 'tStopRefresh')  # time at next scr refresh
                    tekst_15.setAutoDraw(False)
            
            # *blok_16* updates
            if blok_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_16.frameNStart = frameN  # exact frame index
                blok_16.tStart = t  # local t and not account for scr refresh
                blok_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_16, 'tStartRefresh')  # time at next scr refresh
                blok_16.setAutoDraw(True)
            if blok_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_16.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_16.tStop = t  # not accounting for scr refresh
                    blok_16.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_16, 'tStopRefresh')  # time at next scr refresh
                    blok_16.setAutoDraw(False)
            
            # *tekst_16* updates
            if tekst_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_16.frameNStart = frameN  # exact frame index
                tekst_16.tStart = t  # local t and not account for scr refresh
                tekst_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_16, 'tStartRefresh')  # time at next scr refresh
                tekst_16.setAutoDraw(True)
            if tekst_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_16.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_16.tStop = t  # not accounting for scr refresh
                    tekst_16.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_16, 'tStopRefresh')  # time at next scr refresh
                    tekst_16.setAutoDraw(False)
            
            # *blok_17* updates
            if blok_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_17.frameNStart = frameN  # exact frame index
                blok_17.tStart = t  # local t and not account for scr refresh
                blok_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_17, 'tStartRefresh')  # time at next scr refresh
                blok_17.setAutoDraw(True)
            if blok_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_17.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_17.tStop = t  # not accounting for scr refresh
                    blok_17.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_17, 'tStopRefresh')  # time at next scr refresh
                    blok_17.setAutoDraw(False)
            
            # *tekst_17* updates
            if tekst_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_17.frameNStart = frameN  # exact frame index
                tekst_17.tStart = t  # local t and not account for scr refresh
                tekst_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_17, 'tStartRefresh')  # time at next scr refresh
                tekst_17.setAutoDraw(True)
            if tekst_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_17.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_17.tStop = t  # not accounting for scr refresh
                    tekst_17.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_17, 'tStopRefresh')  # time at next scr refresh
                    tekst_17.setAutoDraw(False)
            
            # *blok_18* updates
            if blok_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blok_18.frameNStart = frameN  # exact frame index
                blok_18.tStart = t  # local t and not account for scr refresh
                blok_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blok_18, 'tStartRefresh')  # time at next scr refresh
                blok_18.setAutoDraw(True)
            if blok_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blok_18.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    blok_18.tStop = t  # not accounting for scr refresh
                    blok_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blok_18, 'tStopRefresh')  # time at next scr refresh
                    blok_18.setAutoDraw(False)
            
            # *tekst_18* updates
            if tekst_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tekst_18.frameNStart = frameN  # exact frame index
                tekst_18.tStart = t  # local t and not account for scr refresh
                tekst_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tekst_18, 'tStartRefresh')  # time at next scr refresh
                tekst_18.setAutoDraw(True)
            if tekst_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tekst_18.tStartRefresh + pres_tijd-frameTolerance:
                    # keep track of stop time/frame for later
                    tekst_18.tStop = t  # not accounting for scr refresh
                    tekst_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tekst_18, 'tStopRefresh')  # time at next scr refresh
                    tekst_18.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_schermComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial_scherm"-------
        for thisComponent in Trial_schermComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if muis.clicked_name == ['blok_1']: 
            geregistreerd_resp = 1
        elif muis.clicked_name == ['blok_2']: 
            geregistreerd_resp = 2
        elif muis.clicked_name == ['blok_3']: 
            geregistreerd_resp = 3
        elif muis.clicked_name == ['blok_4']: 
            geregistreerd_resp = 4
        elif muis.clicked_name == ['blok_5']: 
            geregistreerd_resp = 5
        elif muis.clicked_name == ['blok_6']: 
            geregistreerd_resp = 6
        elif muis.clicked_name == ['blok_7']: 
            geregistreerd_resp = 7
        elif muis.clicked_name == ['blok_8']: 
            geregistreerd_resp = 8
        elif muis.clicked_name == ['blok_9']: 
            geregistreerd_resp = 9
        elif muis.clicked_name == ['blok_10']: 
            geregistreerd_resp = 10
        elif muis.clicked_name == ['blok_11']: 
            geregistreerd_resp = 11
        elif muis.clicked_name == ['blok_12']: 
            geregistreerd_resp = 12
        elif muis.clicked_name == ['blok_13']: 
            geregistreerd_resp = 13
        elif muis.clicked_name == ['blok_14']: 
            geregistreerd_resp = 14
        elif muis.clicked_name == ['blok_15']: 
            geregistreerd_resp = 15
        elif muis.clicked_name == ['blok_16']: 
            geregistreerd_resp = 16
        elif muis.clicked_name == ['blok_17']: 
            geregistreerd_resp = 17
        elif muis.clicked_name == ['blok_18']: 
            geregistreerd_resp = 18
        elif muis.clicked_name == [ ]:
            geregistreerd_resp = 0
        
        thisExp.addData('geregistreerd_resp', geregistreerd_resp)
        thisExp.addData('huidige_stim', huidige_stim)
        # store data for Trial_loop (TrialHandler)
        if len(muis.x): Trial_loop.addData('muis.x', muis.x[0])
        if len(muis.y): Trial_loop.addData('muis.y', muis.y[0])
        if len(muis.leftButton): Trial_loop.addData('muis.leftButton', muis.leftButton[0])
        if len(muis.midButton): Trial_loop.addData('muis.midButton', muis.midButton[0])
        if len(muis.rightButton): Trial_loop.addData('muis.rightButton', muis.rightButton[0])
        if len(muis.time): Trial_loop.addData('muis.time', muis.time[0])
        if len(muis.clicked_name): Trial_loop.addData('muis.clicked_name', muis.clicked_name[0])
        Trial_loop.addData('muis.started', muis.tStartRefresh)
        Trial_loop.addData('muis.stopped', muis.tStopRefresh)
        thisExp.addData('laatste_stim', laatste_stim)
        thisExp.addData('juiste_waarde', juiste_waarde)
        geluid_1.stop()  # ensure sound has stopped at end of routine
        geluid_2.stop()  # ensure sound has stopped at end of routine
        geluid_3.stop()  # ensure sound has stopped at end of routine
        geluid_4.stop()  # ensure sound has stopped at end of routine
        geluid_5.stop()  # ensure sound has stopped at end of routine
        geluid_6.stop()  # ensure sound has stopped at end of routine
        geluid_7.stop()  # ensure sound has stopped at end of routine
        geluid_8.stop()  # ensure sound has stopped at end of routine
        geluid_9.stop()  # ensure sound has stopped at end of routine
        # the Routine "Trial_scherm" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_scherm"-------
        continueRoutine = True
        # update component parameters for each repeat
        
        if gezicht_score >= perfect: 
            feedback_smiley = 'emotie1.png'
        elif gezicht_score >= goed:
            feedback_smiley = 'emotie2.png'
        elif gezicht_score >= mwa:
            feedback_smiley = 'emotie3.png'
        elif gezicht_score >= slecht:
            feedback_smiley = 'emotie4.png'
        else:
            feedback_smiley = 'emotie5.png'
        
        if geregistreerd_resp == juiste_waarde:
            kleurAntw = 'green'
            feedback_tekst = 'juist'
            punten = 1
            if Blok_Loop.thisN != 0:
                gezicht_score += 1
        else: 
            kleurAntw = 'red'
            feedback_tekst = 'onjuist'
            punten = 0
            if Blok_Loop.thisN != 0:
                gezicht_score -= 1
        
        Smiley_plaatje.setImage(feedback_smiley)
        FB_Tekst_B0.setColor(kleurAntw, colorSpace='rgb')
        FB_Tekst_B0.setText(feedback_tekst)
        FB_tekst_B1234.setColor(kleurAntw, colorSpace='rgb')
        FB_tekst_B1234.setText(feedback_tekst)
        # keep track of which components have finished
        Feedback_schermComponents = [Smiley_plaatje, FB_Tekst_B0, FB_tekst_B1234, B_1_FB, T_1_FB, B_2_FB, T_2_FB, B_3_FB, T_3_FB, B_4_FB, T_4_FB, B_5_FB, T_5_FB, B_6_FB, T_6_FB, B_7_FB, T_7_FB, B_8_FB, T_8_FB, B_9_FB, T_9_FB, B_10_FB, T_10_FB, B_11_FB, T_11_FB, B_12_FB, T_12_FB, B_13_FB, T_13_FB, B_14_FB, T_14_FB, B_15_FB, T_15_FB, B_16_FB, T_16_FB, B_17_FB, T_17_FB, B_18_FB, T_18_FB]
        for thisComponent in Feedback_schermComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Feedback_schermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback_scherm"-------
        while continueRoutine:
            # get current time
            t = Feedback_schermClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Feedback_schermClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #als routine langer duurt dan 1 sec, ga door met trials
            if t >= 1:
                continueRoutine = False
            
            # *Smiley_plaatje* updates
            if Smiley_plaatje.status == NOT_STARTED and Blok_Loop.thisN  != 0 and gezichtsfeedback_aanzetten ==1:
                # keep track of start time/frame for later
                Smiley_plaatje.frameNStart = frameN  # exact frame index
                Smiley_plaatje.tStart = t  # local t and not account for scr refresh
                Smiley_plaatje.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Smiley_plaatje, 'tStartRefresh')  # time at next scr refresh
                Smiley_plaatje.setAutoDraw(True)
            if Smiley_plaatje.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Smiley_plaatje.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Smiley_plaatje.tStop = t  # not accounting for scr refresh
                    Smiley_plaatje.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Smiley_plaatje, 'tStopRefresh')  # time at next scr refresh
                    Smiley_plaatje.setAutoDraw(False)
            
            # *FB_Tekst_B0* updates
            if FB_Tekst_B0.status == NOT_STARTED and Blok_Loop.thisN  == 0 or gezichtsfeedback_aanzetten ==0:
                # keep track of start time/frame for later
                FB_Tekst_B0.frameNStart = frameN  # exact frame index
                FB_Tekst_B0.tStart = t  # local t and not account for scr refresh
                FB_Tekst_B0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FB_Tekst_B0, 'tStartRefresh')  # time at next scr refresh
                FB_Tekst_B0.setAutoDraw(True)
            if FB_Tekst_B0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FB_Tekst_B0.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FB_Tekst_B0.tStop = t  # not accounting for scr refresh
                    FB_Tekst_B0.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FB_Tekst_B0, 'tStopRefresh')  # time at next scr refresh
                    FB_Tekst_B0.setAutoDraw(False)
            
            # *FB_tekst_B1234* updates
            if FB_tekst_B1234.status == NOT_STARTED and Blok_Loop.thisN  != 0 and gezichtsfeedback_aanzetten == 1:
                # keep track of start time/frame for later
                FB_tekst_B1234.frameNStart = frameN  # exact frame index
                FB_tekst_B1234.tStart = t  # local t and not account for scr refresh
                FB_tekst_B1234.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FB_tekst_B1234, 'tStartRefresh')  # time at next scr refresh
                FB_tekst_B1234.setAutoDraw(True)
            if FB_tekst_B1234.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FB_tekst_B1234.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FB_tekst_B1234.tStop = t  # not accounting for scr refresh
                    FB_tekst_B1234.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FB_tekst_B1234, 'tStopRefresh')  # time at next scr refresh
                    FB_tekst_B1234.setAutoDraw(False)
            
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
            for thisComponent in Feedback_schermComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_scherm"-------
        for thisComponent in Feedback_schermComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        laatste_stim = huidige_stim
        thisExp.addData('Score', punten)
        Trial_loop.addData('Smiley_plaatje.started', Smiley_plaatje.tStartRefresh)
        Trial_loop.addData('Smiley_plaatje.stopped', Smiley_plaatje.tStopRefresh)
        # the Routine "Feedback_scherm" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed Trial_herhalingen repeats of 'Trial_loop'
    
    # get names of stimulus parameters
    if Trial_loop.trialList in ([], [None], None):
        params = []
    else:
        params = Trial_loop.trialList[0].keys()
    # save data for this loop
    Trial_loop.saveAsExcel(filename + '.xlsx', sheetName='Trial_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Pauze_scherm"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the Pauze_klik
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Pauze_schermComponents = [Pauze_Tekst, Pauze_klik]
    for thisComponent in Pauze_schermComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pauze_schermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pauze_scherm"-------
    while continueRoutine:
        # get current time
        t = Pauze_schermClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pauze_schermClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pauze_Tekst* updates
        if Pauze_Tekst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pauze_Tekst.frameNStart = frameN  # exact frame index
            Pauze_Tekst.tStart = t  # local t and not account for scr refresh
            Pauze_Tekst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pauze_Tekst, 'tStartRefresh')  # time at next scr refresh
            Pauze_Tekst.setAutoDraw(True)
        # *Pauze_klik* updates
        if Pauze_klik.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pauze_klik.frameNStart = frameN  # exact frame index
            Pauze_klik.tStart = t  # local t and not account for scr refresh
            Pauze_klik.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pauze_klik, 'tStartRefresh')  # time at next scr refresh
            Pauze_klik.status = STARTED
            Pauze_klik.mouseClock.reset()
            prevButtonState = Pauze_klik.getPressed()  # if button is down already this ISN'T a new click
        if Pauze_klik.status == STARTED:  # only update if started and not finished!
            buttons = Pauze_klik.getPressed()
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
        for thisComponent in Pauze_schermComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pauze_scherm"-------
    for thisComponent in Pauze_schermComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blok_Loop.addData('Pauze_Tekst.started', Pauze_Tekst.tStartRefresh)
    Blok_Loop.addData('Pauze_Tekst.stopped', Pauze_Tekst.tStopRefresh)
    # store data for Blok_Loop (TrialHandler)
    x, y = Pauze_klik.getPos()
    buttons = Pauze_klik.getPressed()
    Blok_Loop.addData('Pauze_klik.x', x)
    Blok_Loop.addData('Pauze_klik.y', y)
    Blok_Loop.addData('Pauze_klik.leftButton', buttons[0])
    Blok_Loop.addData('Pauze_klik.midButton', buttons[1])
    Blok_Loop.addData('Pauze_klik.rightButton', buttons[2])
    Blok_Loop.addData('Pauze_klik.started', Pauze_klik.tStart)
    Blok_Loop.addData('Pauze_klik.stopped', Pauze_klik.tStop)
    # the Routine "Pauze_scherm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5 repeats of 'Blok_Loop'


# ------Prepare to start Routine "Eind_scherm"-------
continueRoutine = True
# update component parameters for each repeat
beëindig_exp.keys = []
beëindig_exp.rt = []
_beëindig_exp_allKeys = []
# keep track of which components have finished
Eind_schermComponents = [Bedankt, beëindig_exp]
for thisComponent in Eind_schermComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Eind_schermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Eind_scherm"-------
while continueRoutine:
    # get current time
    t = Eind_schermClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Eind_schermClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Bedankt* updates
    if Bedankt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bedankt.frameNStart = frameN  # exact frame index
        Bedankt.tStart = t  # local t and not account for scr refresh
        Bedankt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bedankt, 'tStartRefresh')  # time at next scr refresh
        Bedankt.setAutoDraw(True)
    
    # *beëindig_exp* updates
    waitOnFlip = False
    if beëindig_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beëindig_exp.frameNStart = frameN  # exact frame index
        beëindig_exp.tStart = t  # local t and not account for scr refresh
        beëindig_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beëindig_exp, 'tStartRefresh')  # time at next scr refresh
        beëindig_exp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(beëindig_exp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(beëindig_exp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if beëindig_exp.status == STARTED and not waitOnFlip:
        theseKeys = beëindig_exp.getKeys(keyList=['space'], waitRelease=False)
        _beëindig_exp_allKeys.extend(theseKeys)
        if len(_beëindig_exp_allKeys):
            beëindig_exp.keys = _beëindig_exp_allKeys[-1].name  # just the last key pressed
            beëindig_exp.rt = _beëindig_exp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Eind_schermComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Eind_scherm"-------
for thisComponent in Eind_schermComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if beëindig_exp.keys in ['', [], None]:  # No response was made
    beëindig_exp.keys = None
thisExp.addData('beëindig_exp.keys',beëindig_exp.keys)
if beëindig_exp.keys != None:  # we had a response
    thisExp.addData('beëindig_exp.rt', beëindig_exp.rt)
thisExp.nextEntry()
# the Routine "Eind_scherm" was not non-slip safe, so reset the non-slip timer
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
