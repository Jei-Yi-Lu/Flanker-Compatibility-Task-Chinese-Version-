#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on 四月 17, 2026, at 20:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'Flanker Compatibility Task'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999):06.0f}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (2048, 1600)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\user\\Desktop\\研究所\\碩二下\\The Applications of Computer Hardware and Programming Languages in Behavioral Experiments and Big-Data Analyses\\Midtern Report\\Flanker Compatibility Task\\Flanker Compatibility Task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color='Black', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='deg',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'Black'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'deg'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Loading...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Intro" ---
    # Run 'Begin Experiment' code from code_2
    # 初始化練習計數器
    prac_corr_cnt = 0
    
    # 初始化正式實驗計數器
    total_trials_cnt = 0
    Intro_text = visual.TextStim(win=win, name='Intro_text',
        text='歡迎參與本作業。\n\n您將看到六個圓圈圍繞螢幕中央的十字凝視點。\n作業過程中，可能會有數量不等的形狀個別出現在圓圈中。\n\n請您在看到形狀出現後，盡快判斷「圓圈內的形狀」\n是否包含「正方形」或「菱形」，\n並盡可能又快又正確地按鍵反應：\n\n- 圓圈內出現正方形：按下「A」鍵。\n- 圓圈內出現菱形：按下「L」鍵。\n\n然而，請無視圓圈之外出現的正方形或菱形，\n並只判斷「圓圈內」的形狀包含正方形或菱形。\n\n我們會先練習個幾題，再開始正式作業。\n\n\n【準備好後，請按「空白鍵」開始練習】\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=26.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Intro_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Trial_Routine" ---
    Stim_1 = visual.Rect(
        win=win, name='Stim_1',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(0, 6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    Stim_2 = visual.Rect(
        win=win, name='Stim_2',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(5.20, 3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    Stim_3 = visual.Rect(
        win=win, name='Stim_3',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(5.20, -3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-2.0, interpolate=True)
    Stim_4 = visual.Rect(
        win=win, name='Stim_4',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(0, -6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-3.0, interpolate=True)
    Stim_5 = visual.Rect(
        win=win, name='Stim_5',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(-5.20, -3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-4.0, interpolate=True)
    Stim_6 = visual.Rect(
        win=win, name='Stim_6',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(-5.20, 3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-5.0, interpolate=True)
    # Run 'Begin Experiment' code from Trials_code
    total_trials_cnt = 0
    
    # 形狀頂點定義
    shapes = {
        'square': [(-0.7,-0.7), (0.7,-0.7), (0.7,0.7), (-0.7,0.7)],
        'diamond': [(0,1), (1,0), (0,-1), (-1,0)],
        'tri': [(0,0.8), (-0.8,-0.7), (0.8,-0.7)],
        'tri_inv': [(0,-0.8), (-0.8,0.7), (0.8,0.7)],
        'penta': [(0, 0.8), (-0.76, 0.25), (-0.47, -0.65), (0.47, -0.65), (0.76, 0.25)],
        'penta_inv': [(0, -0.8), (0.76, -0.25), (0.47, 0.65), (-0.47, 0.65), (-0.76, -0.25)]
    }
    
    filler_pool = ['tri', 'tri_inv', 'penta', 'penta_inv']
    diff_map = {1: 0, 2: 1, 3: 3, 4: 5}
    
    # 把刺激組件放進清單
    stims = [Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6]
    Fixation = visual.TextStim(win=win, name='Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    Circle_1 = visual.ShapeStim(
        win=win, name='Circle_1',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(0, 6), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    Circle_2 = visual.ShapeStim(
        win=win, name='Circle_2',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(5.20, 3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    Circle_3 = visual.ShapeStim(
        win=win, name='Circle_3',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(5.20, -3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-10.0, interpolate=True)
    Circle_4 = visual.ShapeStim(
        win=win, name='Circle_4',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(0, -6), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-11.0, interpolate=True)
    Circle_5 = visual.ShapeStim(
        win=win, name='Circle_5',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(-5.20, -3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-12.0, interpolate=True)
    Circle_6 = visual.ShapeStim(
        win=win, name='Circle_6',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(-5.20, 3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    Distractor = visual.Rect(
        win=win, name='Distractor',
        width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-14.0, interpolate=True)
    Anskey = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Feedback_Routine" ---
    Feedback_text = visual.TextStim(win=win, name='Feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Prac_Check" ---
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Ready" ---
    Ready_text = visual.TextStim(win=win, name='Ready_text',
        text='接下來即將開始正式作業。\n\n\n請您在看到形狀出現後，盡快判斷「圓圈內的形狀」\n是否包含「正方形」或「菱形」，\n並盡可能又快又正確地按鍵反應：\n\n- 圓圈內出現正方形：按下「A」鍵。\n- 圓圈內出現菱形：按下「L」鍵。\n\n然而，請無視圓圈之外出現的正方形或菱形，\n並只判斷「圓圈內」的形狀包含正方形或菱形。\n\n\n【準備好後，請按「空白鍵」開始正式作業】\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=26.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Ready_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Trial_Routine" ---
    Stim_1 = visual.Rect(
        win=win, name='Stim_1',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(0, 6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    Stim_2 = visual.Rect(
        win=win, name='Stim_2',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(5.20, 3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    Stim_3 = visual.Rect(
        win=win, name='Stim_3',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(5.20, -3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-2.0, interpolate=True)
    Stim_4 = visual.Rect(
        win=win, name='Stim_4',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(0, -6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-3.0, interpolate=True)
    Stim_5 = visual.Rect(
        win=win, name='Stim_5',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(-5.20, -3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-4.0, interpolate=True)
    Stim_6 = visual.Rect(
        win=win, name='Stim_6',
        width=(1, 1)[0], height=(1, 1)[1],
        ori=0.0, pos=(-5.20, 3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-5.0, interpolate=True)
    # Run 'Begin Experiment' code from Trials_code
    total_trials_cnt = 0
    
    # 形狀頂點定義
    shapes = {
        'square': [(-0.7,-0.7), (0.7,-0.7), (0.7,0.7), (-0.7,0.7)],
        'diamond': [(0,1), (1,0), (0,-1), (-1,0)],
        'tri': [(0,0.8), (-0.8,-0.7), (0.8,-0.7)],
        'tri_inv': [(0,-0.8), (-0.8,0.7), (0.8,0.7)],
        'penta': [(0, 0.8), (-0.76, 0.25), (-0.47, -0.65), (0.47, -0.65), (0.76, 0.25)],
        'penta_inv': [(0, -0.8), (0.76, -0.25), (0.47, 0.65), (-0.47, 0.65), (-0.76, -0.25)]
    }
    
    filler_pool = ['tri', 'tri_inv', 'penta', 'penta_inv']
    diff_map = {1: 0, 2: 1, 3: 3, 4: 5}
    
    # 把刺激組件放進清單
    stims = [Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6]
    Fixation = visual.TextStim(win=win, name='Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    Circle_1 = visual.ShapeStim(
        win=win, name='Circle_1',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(0, 6), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    Circle_2 = visual.ShapeStim(
        win=win, name='Circle_2',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(5.20, 3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    Circle_3 = visual.ShapeStim(
        win=win, name='Circle_3',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(5.20, -3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-10.0, interpolate=True)
    Circle_4 = visual.ShapeStim(
        win=win, name='Circle_4',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(0, -6), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-11.0, interpolate=True)
    Circle_5 = visual.ShapeStim(
        win=win, name='Circle_5',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(-5.20, -3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-12.0, interpolate=True)
    Circle_6 = visual.ShapeStim(
        win=win, name='Circle_6',
        size=(3, 3), vertices='circle',
        ori=0.0, pos=(-5.20, 3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    Distractor = visual.Rect(
        win=win, name='Distractor',
        width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-14.0, interpolate=True)
    Anskey = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "BreakTime_Routine" ---
    # Run 'Begin Experiment' code from BreakTime_code
    # 初始化計數器
    total_trials_cnt = 0
    BreakTime_text = visual.TextStim(win=win, name='BreakTime_text',
        text='您現在可以稍作休息一下！\n\n\n【準備好後，請按「空白鍵」繼續作業】\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=26.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    BreakTime_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ThankYou" ---
    Thanks_text = visual.TextStim(win=win, name='Thanks_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=26.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Thanks_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Intro" ---
    # create an object to store info about Routine Intro
    Intro = data.Routine(
        name='Intro',
        components=[Intro_text, Intro_keyresp],
    )
    Intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Intro_keyresp
    Intro_keyresp.keys = []
    Intro_keyresp.rt = []
    _Intro_keyresp_allKeys = []
    # store start times for Intro
    Intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Intro.tStart = globalClock.getTime(format='float')
    Intro.status = STARTED
    thisExp.addData('Intro.started', Intro.tStart)
    Intro.maxDuration = None
    # keep track of which components have finished
    IntroComponents = Intro.components
    for thisComponent in Intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Intro" ---
    thisExp.currentRoutine = Intro
    Intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intro_text* updates
        
        # if Intro_text is starting this frame...
        if Intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Intro_text.frameNStart = frameN  # exact frame index
            Intro_text.tStart = t  # local t and not account for scr refresh
            Intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Intro_text.status = STARTED
            Intro_text.setAutoDraw(True)
        
        # if Intro_text is active this frame...
        if Intro_text.status == STARTED:
            # update params
            pass
        
        # *Intro_keyresp* updates
        waitOnFlip = False
        
        # if Intro_keyresp is starting this frame...
        if Intro_keyresp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Intro_keyresp.frameNStart = frameN  # exact frame index
            Intro_keyresp.tStart = t  # local t and not account for scr refresh
            Intro_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            Intro_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Intro_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Intro_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Intro_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = Intro_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Intro_keyresp_allKeys.extend(theseKeys)
            if len(_Intro_keyresp_allKeys):
                Intro_keyresp.keys = _Intro_keyresp_allKeys[-1].name  # just the last key pressed
                Intro_keyresp.rt = _Intro_keyresp_allKeys[-1].rt
                Intro_keyresp.duration = _Intro_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Intro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Intro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Intro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro" ---
    for thisComponent in Intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Intro
    Intro.tStop = globalClock.getTime(format='float')
    Intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Intro.stopped', Intro.tStop)
    # check responses
    if Intro_keyresp.keys in ['', [], None]:  # No response was made
        Intro_keyresp.keys = None
    thisExp.addData('Intro_keyresp.keys',Intro_keyresp.keys)
    if Intro_keyresp.keys != None:  # we had a response
        thisExp.addData('Intro_keyresp.rt', Intro_keyresp.rt)
        thisExp.addData('Intro_keyresp.duration', Intro_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Repeat_Prac_Loop = data.TrialHandler2(
        name='Repeat_Prac_Loop',
        nReps=99, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(Repeat_Prac_Loop)  # add the loop to the experiment
    thisRepeat_Prac_Loop = Repeat_Prac_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_Prac_Loop.rgb)
    if thisRepeat_Prac_Loop != None:
        for paramName in thisRepeat_Prac_Loop:
            globals()[paramName] = thisRepeat_Prac_Loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRepeat_Prac_Loop in Repeat_Prac_Loop:
        Repeat_Prac_Loop.status = STARTED
        if hasattr(thisRepeat_Prac_Loop, 'status'):
            thisRepeat_Prac_Loop.status = STARTED
        currentLoop = Repeat_Prac_Loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_Prac_Loop.rgb)
        if thisRepeat_Prac_Loop != None:
            for paramName in thisRepeat_Prac_Loop:
                globals()[paramName] = thisRepeat_Prac_Loop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        Prac_Loop = data.TrialHandler2(
            name='Prac_Loop',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Prac_Stimulus_Configurations.xlsx'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(Prac_Loop)  # add the loop to the experiment
        thisPrac_Loop = Prac_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_Loop.rgb)
        if thisPrac_Loop != None:
            for paramName in thisPrac_Loop:
                globals()[paramName] = thisPrac_Loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPrac_Loop in Prac_Loop:
            Prac_Loop.status = STARTED
            if hasattr(thisPrac_Loop, 'status'):
                thisPrac_Loop.status = STARTED
            currentLoop = Prac_Loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_Loop.rgb)
            if thisPrac_Loop != None:
                for paramName in thisPrac_Loop:
                    globals()[paramName] = thisPrac_Loop[paramName]
            
            # --- Prepare to start Routine "Trial_Routine" ---
            # create an object to store info about Routine Trial_Routine
            Trial_Routine = data.Routine(
                name='Trial_Routine',
                components=[Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6, Fixation, Circle_1, Circle_2, Circle_3, Circle_4, Circle_5, Circle_6, Distractor, Anskey],
            )
            Trial_Routine.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            Stim_1.setOpacity(1.0)
            Stim_2.setOpacity(1.0)
            Stim_3.setOpacity(1.0)
            Stim_4.setOpacity(1.0)
            Stim_5.setOpacity(1.0)
            Stim_6.setOpacity(1.0)
            # Run 'Begin Routine' code from Trials_code
            import random
            
            # 1. 確保組件清單正確
            stims = [Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6]
            
            # 2. 位置隨機化計算
            num_fillers = diff_map[difficulty]
            other_indices = [i for i in range(6) if i != target_idx]
            random.shuffle(other_indices)
            filler_indices = other_indices[:num_fillers]
            
            # 3. 遍歷設定每個 Stim 組件的屬性
            for i, s_cong in enumerate(stims):
                if i == target_idx:
                    # 設定目標（vertices 決定形狀，opacity 決定顯示與否）：
                    s_cong.setVertices(shapes[target_type])
                    s_cong.setOpacity(1)
                elif i in filler_indices:
                    # 設定干擾物
                    rand_f = random.choice(filler_pool)
                    s_cong.setVertices(shapes[rand_f])
                    s_cong.setOpacity(1)
                else:
                    # 隱藏沒用到的位置
                    s_cong.setOpacity(0)
            
            # 4. 設定外圍 Distractor
            if condition == 'cong':
                d_v = shapes[target_type]
            else:
                d_v = shapes['diamond'] if target_type == 'square' else shapes['square']
            
            Distractor.setVertices(d_v)
            Distractor.setOpacity(1)
            # 位置由 Excel 的 dist_pos_x 控制，這部分可以留在 Builder 的 Pos 欄位填 [dist_pos_x, 0]
            Distractor.setPos((dist_pos_x, 0))
            # create starting attributes for Anskey
            Anskey.keys = []
            Anskey.rt = []
            _Anskey_allKeys = []
            # store start times for Trial_Routine
            Trial_Routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Trial_Routine.tStart = globalClock.getTime(format='float')
            Trial_Routine.status = STARTED
            thisExp.addData('Trial_Routine.started', Trial_Routine.tStart)
            Trial_Routine.maxDuration = None
            # keep track of which components have finished
            Trial_RoutineComponents = Trial_Routine.components
            for thisComponent in Trial_Routine.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trial_Routine" ---
            thisExp.currentRoutine = Trial_Routine
            Trial_Routine.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 4.0:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_Loop, 'status') and thisPrac_Loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Stim_1* updates
                
                # if Stim_1 is starting this frame...
                if Stim_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_1.frameNStart = frameN  # exact frame index
                    Stim_1.tStart = t  # local t and not account for scr refresh
                    Stim_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_1.status = STARTED
                    Stim_1.setAutoDraw(True)
                
                # if Stim_1 is active this frame...
                if Stim_1.status == STARTED:
                    # update params
                    pass
                
                # if Stim_1 is stopping this frame...
                if Stim_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_1.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_1.tStop = t  # not accounting for scr refresh
                        Stim_1.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_1.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_1.status = FINISHED
                        Stim_1.setAutoDraw(False)
                
                # *Stim_2* updates
                
                # if Stim_2 is starting this frame...
                if Stim_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_2.frameNStart = frameN  # exact frame index
                    Stim_2.tStart = t  # local t and not account for scr refresh
                    Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_2.status = STARTED
                    Stim_2.setAutoDraw(True)
                
                # if Stim_2 is active this frame...
                if Stim_2.status == STARTED:
                    # update params
                    pass
                
                # if Stim_2 is stopping this frame...
                if Stim_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_2.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_2.tStop = t  # not accounting for scr refresh
                        Stim_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_2.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_2.status = FINISHED
                        Stim_2.setAutoDraw(False)
                
                # *Stim_3* updates
                
                # if Stim_3 is starting this frame...
                if Stim_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_3.frameNStart = frameN  # exact frame index
                    Stim_3.tStart = t  # local t and not account for scr refresh
                    Stim_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_3.status = STARTED
                    Stim_3.setAutoDraw(True)
                
                # if Stim_3 is active this frame...
                if Stim_3.status == STARTED:
                    # update params
                    pass
                
                # if Stim_3 is stopping this frame...
                if Stim_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_3.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_3.tStop = t  # not accounting for scr refresh
                        Stim_3.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_3.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_3.status = FINISHED
                        Stim_3.setAutoDraw(False)
                
                # *Stim_4* updates
                
                # if Stim_4 is starting this frame...
                if Stim_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_4.frameNStart = frameN  # exact frame index
                    Stim_4.tStart = t  # local t and not account for scr refresh
                    Stim_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_4.status = STARTED
                    Stim_4.setAutoDraw(True)
                
                # if Stim_4 is active this frame...
                if Stim_4.status == STARTED:
                    # update params
                    pass
                
                # if Stim_4 is stopping this frame...
                if Stim_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_4.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_4.tStop = t  # not accounting for scr refresh
                        Stim_4.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_4.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_4.status = FINISHED
                        Stim_4.setAutoDraw(False)
                
                # *Stim_5* updates
                
                # if Stim_5 is starting this frame...
                if Stim_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_5.frameNStart = frameN  # exact frame index
                    Stim_5.tStart = t  # local t and not account for scr refresh
                    Stim_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_5.status = STARTED
                    Stim_5.setAutoDraw(True)
                
                # if Stim_5 is active this frame...
                if Stim_5.status == STARTED:
                    # update params
                    pass
                
                # if Stim_5 is stopping this frame...
                if Stim_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_5.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_5.tStop = t  # not accounting for scr refresh
                        Stim_5.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_5.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_5.status = FINISHED
                        Stim_5.setAutoDraw(False)
                
                # *Stim_6* updates
                
                # if Stim_6 is starting this frame...
                if Stim_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_6.frameNStart = frameN  # exact frame index
                    Stim_6.tStart = t  # local t and not account for scr refresh
                    Stim_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Stim_6.status = STARTED
                    Stim_6.setAutoDraw(True)
                
                # if Stim_6 is active this frame...
                if Stim_6.status == STARTED:
                    # update params
                    pass
                
                # if Stim_6 is stopping this frame...
                if Stim_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Stim_6.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Stim_6.tStop = t  # not accounting for scr refresh
                        Stim_6.tStopRefresh = tThisFlipGlobal  # on global time
                        Stim_6.frameNStop = frameN  # exact frame index
                        # update status
                        Stim_6.status = FINISHED
                        Stim_6.setAutoDraw(False)
                
                # *Fixation* updates
                
                # if Fixation is starting this frame...
                if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation.frameNStart = frameN  # exact frame index
                    Fixation.tStart = t  # local t and not account for scr refresh
                    Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Fixation.status = STARTED
                    Fixation.setAutoDraw(True)
                
                # if Fixation is active this frame...
                if Fixation.status == STARTED:
                    # update params
                    pass
                
                # if Fixation is stopping this frame...
                if Fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation.tStop = t  # not accounting for scr refresh
                        Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        Fixation.frameNStop = frameN  # exact frame index
                        # update status
                        Fixation.status = FINISHED
                        Fixation.setAutoDraw(False)
                
                # *Circle_1* updates
                
                # if Circle_1 is starting this frame...
                if Circle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_1.frameNStart = frameN  # exact frame index
                    Circle_1.tStart = t  # local t and not account for scr refresh
                    Circle_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_1.status = STARTED
                    Circle_1.setAutoDraw(True)
                
                # if Circle_1 is active this frame...
                if Circle_1.status == STARTED:
                    # update params
                    pass
                
                # if Circle_1 is stopping this frame...
                if Circle_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_1.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_1.tStop = t  # not accounting for scr refresh
                        Circle_1.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_1.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_1.status = FINISHED
                        Circle_1.setAutoDraw(False)
                
                # *Circle_2* updates
                
                # if Circle_2 is starting this frame...
                if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_2.frameNStart = frameN  # exact frame index
                    Circle_2.tStart = t  # local t and not account for scr refresh
                    Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_2.status = STARTED
                    Circle_2.setAutoDraw(True)
                
                # if Circle_2 is active this frame...
                if Circle_2.status == STARTED:
                    # update params
                    pass
                
                # if Circle_2 is stopping this frame...
                if Circle_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_2.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_2.tStop = t  # not accounting for scr refresh
                        Circle_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_2.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_2.status = FINISHED
                        Circle_2.setAutoDraw(False)
                
                # *Circle_3* updates
                
                # if Circle_3 is starting this frame...
                if Circle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_3.frameNStart = frameN  # exact frame index
                    Circle_3.tStart = t  # local t and not account for scr refresh
                    Circle_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_3.status = STARTED
                    Circle_3.setAutoDraw(True)
                
                # if Circle_3 is active this frame...
                if Circle_3.status == STARTED:
                    # update params
                    pass
                
                # if Circle_3 is stopping this frame...
                if Circle_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_3.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_3.tStop = t  # not accounting for scr refresh
                        Circle_3.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_3.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_3.status = FINISHED
                        Circle_3.setAutoDraw(False)
                
                # *Circle_4* updates
                
                # if Circle_4 is starting this frame...
                if Circle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_4.frameNStart = frameN  # exact frame index
                    Circle_4.tStart = t  # local t and not account for scr refresh
                    Circle_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_4.status = STARTED
                    Circle_4.setAutoDraw(True)
                
                # if Circle_4 is active this frame...
                if Circle_4.status == STARTED:
                    # update params
                    pass
                
                # if Circle_4 is stopping this frame...
                if Circle_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_4.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_4.tStop = t  # not accounting for scr refresh
                        Circle_4.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_4.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_4.status = FINISHED
                        Circle_4.setAutoDraw(False)
                
                # *Circle_5* updates
                
                # if Circle_5 is starting this frame...
                if Circle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_5.frameNStart = frameN  # exact frame index
                    Circle_5.tStart = t  # local t and not account for scr refresh
                    Circle_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_5.status = STARTED
                    Circle_5.setAutoDraw(True)
                
                # if Circle_5 is active this frame...
                if Circle_5.status == STARTED:
                    # update params
                    pass
                
                # if Circle_5 is stopping this frame...
                if Circle_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_5.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_5.tStop = t  # not accounting for scr refresh
                        Circle_5.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_5.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_5.status = FINISHED
                        Circle_5.setAutoDraw(False)
                
                # *Circle_6* updates
                
                # if Circle_6 is starting this frame...
                if Circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_6.frameNStart = frameN  # exact frame index
                    Circle_6.tStart = t  # local t and not account for scr refresh
                    Circle_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Circle_6.status = STARTED
                    Circle_6.setAutoDraw(True)
                
                # if Circle_6 is active this frame...
                if Circle_6.status == STARTED:
                    # update params
                    pass
                
                # if Circle_6 is stopping this frame...
                if Circle_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Circle_6.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        Circle_6.tStop = t  # not accounting for scr refresh
                        Circle_6.tStopRefresh = tThisFlipGlobal  # on global time
                        Circle_6.frameNStop = frameN  # exact frame index
                        # update status
                        Circle_6.status = FINISHED
                        Circle_6.setAutoDraw(False)
                
                # *Distractor* updates
                
                # if Distractor is starting this frame...
                if Distractor.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Distractor.frameNStart = frameN  # exact frame index
                    Distractor.tStart = t  # local t and not account for scr refresh
                    Distractor.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Distractor, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Distractor.status = STARTED
                    Distractor.setAutoDraw(True)
                
                # if Distractor is active this frame...
                if Distractor.status == STARTED:
                    # update params
                    pass
                
                # if Distractor is stopping this frame...
                if Distractor.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Distractor.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Distractor.tStop = t  # not accounting for scr refresh
                        Distractor.tStopRefresh = tThisFlipGlobal  # on global time
                        Distractor.frameNStop = frameN  # exact frame index
                        # update status
                        Distractor.status = FINISHED
                        Distractor.setAutoDraw(False)
                
                # *Anskey* updates
                waitOnFlip = False
                
                # if Anskey is starting this frame...
                if Anskey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Anskey.frameNStart = frameN  # exact frame index
                    Anskey.tStart = t  # local t and not account for scr refresh
                    Anskey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Anskey, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Anskey.started')
                    # update status
                    Anskey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Anskey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Anskey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if Anskey is stopping this frame...
                if Anskey.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Anskey.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Anskey.tStop = t  # not accounting for scr refresh
                        Anskey.tStopRefresh = tThisFlipGlobal  # on global time
                        Anskey.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Anskey.stopped')
                        # update status
                        Anskey.status = FINISHED
                        Anskey.status = FINISHED
                if Anskey.status == STARTED and not waitOnFlip:
                    theseKeys = Anskey.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _Anskey_allKeys.extend(theseKeys)
                    if len(_Anskey_allKeys):
                        Anskey.keys = _Anskey_allKeys[-1].name  # just the last key pressed
                        Anskey.rt = _Anskey_allKeys[-1].rt
                        Anskey.duration = _Anskey_allKeys[-1].duration
                        # was this correct?
                        if (Anskey.keys == str(ans)) or (Anskey.keys == ans):
                            Anskey.corr = 1
                        else:
                            Anskey.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=Trial_Routine,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    Trial_Routine.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if Trial_Routine.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in Trial_Routine.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trial_Routine" ---
            for thisComponent in Trial_Routine.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Trial_Routine
            Trial_Routine.tStop = globalClock.getTime(format='float')
            Trial_Routine.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Trial_Routine.stopped', Trial_Routine.tStop)
            # Run 'End Routine' code from Trials_code
            # --- 練習回合的計數 ---
            if 'Prac_Loop' in locals() and Prac_Loop.status == STARTED:
                if Anskey.corr == 1:
                    prac_corr_cnt += 1
            
            # --- 正式實驗的計數與統計 ---
            if 'Trials_Loop' in locals() and Trials_Loop.status == STARTED:
                # 休息計數
                total_trials_cnt += 1
                
                # 數據統計初始化
                if 'summary' not in expInfo:
                    expInfo['summary'] = {'corr': 0, 'cong_rt': [], 'incong_rt': []}
                
                # 紀錄正確率與 RT
                if Anskey.corr == 1:
                    expInfo['summary']['corr'] += 1
                    if Anskey.rt is not None:
                        if condition == 'cong':
                            expInfo['summary']['cong_rt'].append(Anskey.rt)
                        else:
                            expInfo['summary']['incong_rt'].append(Anskey.rt)
            # check responses
            if Anskey.keys in ['', [], None]:  # No response was made
                Anskey.keys = None
                # was no response the correct answer?!
                if str(ans).lower() == 'none':
                   Anskey.corr = 1;  # correct non-response
                else:
                   Anskey.corr = 0;  # failed to respond (incorrectly)
            # store data for Prac_Loop (TrialHandler)
            Prac_Loop.addData('Anskey.keys',Anskey.keys)
            Prac_Loop.addData('Anskey.corr', Anskey.corr)
            if Anskey.keys != None:  # we had a response
                Prac_Loop.addData('Anskey.rt', Anskey.rt)
                Prac_Loop.addData('Anskey.duration', Anskey.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Trial_Routine.maxDurationReached:
                routineTimer.addTime(-Trial_Routine.maxDuration)
            elif Trial_Routine.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            
            # --- Prepare to start Routine "Feedback_Routine" ---
            # create an object to store info about Routine Feedback_Routine
            Feedback_Routine = data.Routine(
                name='Feedback_Routine',
                components=[Feedback_text],
            )
            Feedback_Routine.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            # 檢查 Anskey 的結果
            if not Anskey.keys:
                fb_msg = "太慢作答！"
            
            elif Anskey.corr == 1:
                fb_msg = "正確"
            
            else:
                fb_msg = "錯誤"
            
            
            # 將顏色套用到文字組件
            Feedback_text.setText(fb_msg)
            Feedback_text.setText(fb_msg)
            # store start times for Feedback_Routine
            Feedback_Routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Feedback_Routine.tStart = globalClock.getTime(format='float')
            Feedback_Routine.status = STARTED
            thisExp.addData('Feedback_Routine.started', Feedback_Routine.tStart)
            Feedback_Routine.maxDuration = None
            # keep track of which components have finished
            Feedback_RoutineComponents = Feedback_Routine.components
            for thisComponent in Feedback_Routine.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Feedback_Routine" ---
            thisExp.currentRoutine = Feedback_Routine
            Feedback_Routine.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_Loop, 'status') and thisPrac_Loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Feedback_text* updates
                
                # if Feedback_text is starting this frame...
                if Feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Feedback_text.frameNStart = frameN  # exact frame index
                    Feedback_text.tStart = t  # local t and not account for scr refresh
                    Feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Feedback_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Feedback_text.status = STARTED
                    Feedback_text.setAutoDraw(True)
                
                # if Feedback_text is active this frame...
                if Feedback_text.status == STARTED:
                    # update params
                    pass
                
                # if Feedback_text is stopping this frame...
                if Feedback_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Feedback_text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Feedback_text.tStop = t  # not accounting for scr refresh
                        Feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                        Feedback_text.frameNStop = frameN  # exact frame index
                        # update status
                        Feedback_text.status = FINISHED
                        Feedback_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=Feedback_Routine,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    Feedback_Routine.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if Feedback_Routine.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in Feedback_Routine.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Feedback_Routine" ---
            for thisComponent in Feedback_Routine.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Feedback_Routine
            Feedback_Routine.tStop = globalClock.getTime(format='float')
            Feedback_Routine.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Feedback_Routine.stopped', Feedback_Routine.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Feedback_Routine.maxDurationReached:
                routineTimer.addTime(-Feedback_Routine.maxDuration)
            elif Feedback_Routine.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            # mark thisPrac_Loop as finished
            if hasattr(thisPrac_Loop, 'status'):
                thisPrac_Loop.status = FINISHED
            # if awaiting a pause, pause now
            if Prac_Loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                Prac_Loop.status = STARTED
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Prac_Loop'
        Prac_Loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "Prac_Check" ---
        # create an object to store info about Routine Prac_Check
        Prac_Check = data.Routine(
            name='Prac_Check',
            components=[text, key_resp],
        )
        Prac_Check.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Prac_Check_code
        # 設定達標門檻
        required_score = 14
        
        if prac_corr_cnt >= required_score:
            # 達標：結束外層迴圈，進入正式實驗
            Repeat_Prac_Loop.finished = True
            prac_feedback_msg = f"練習階段結束。您的正確題數為 {prac_corr_cnt}。\n\n\n【請按「空白鍵」繼續】"
        else:
            # 未達標：不結束外層迴圈，它會自動重跑一次內層 Prac_Loop
            prac_feedback_msg = f"練習正確題數為 {prac_corr_cnt}，\n未達練習階段之通過門檻 14 題。\n\n要請您再重新練習一次，確保您熟悉作業規則。\n\n\n【請按「空白鍵」開始重新練習】"
            prac_corr_cnt = 0
        text.setText(prac_feedback_msg)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for Prac_Check
        Prac_Check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Prac_Check.tStart = globalClock.getTime(format='float')
        Prac_Check.status = STARTED
        thisExp.addData('Prac_Check.started', Prac_Check.tStart)
        Prac_Check.maxDuration = None
        # keep track of which components have finished
        Prac_CheckComponents = Prac_Check.components
        for thisComponent in Prac_Check.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Prac_Check" ---
        thisExp.currentRoutine = Prac_Check
        Prac_Check.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisRepeat_Prac_Loop, 'status') and thisRepeat_Prac_Loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Prac_Check,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Prac_Check.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Prac_Check.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Prac_Check.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Prac_Check" ---
        for thisComponent in Prac_Check.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Prac_Check
        Prac_Check.tStop = globalClock.getTime(format='float')
        Prac_Check.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Prac_Check.stopped', Prac_Check.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        Repeat_Prac_Loop.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            Repeat_Prac_Loop.addData('key_resp.rt', key_resp.rt)
            Repeat_Prac_Loop.addData('key_resp.duration', key_resp.duration)
        # the Routine "Prac_Check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisRepeat_Prac_Loop as finished
        if hasattr(thisRepeat_Prac_Loop, 'status'):
            thisRepeat_Prac_Loop.status = FINISHED
        # if awaiting a pause, pause now
        if Repeat_Prac_Loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Repeat_Prac_Loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 99 repeats of 'Repeat_Prac_Loop'
    Repeat_Prac_Loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Ready" ---
    # create an object to store info about Routine Ready
    Ready = data.Routine(
        name='Ready',
        components=[Ready_text, Ready_keyresp],
    )
    Ready.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Ready_keyresp
    Ready_keyresp.keys = []
    Ready_keyresp.rt = []
    _Ready_keyresp_allKeys = []
    # store start times for Ready
    Ready.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Ready.tStart = globalClock.getTime(format='float')
    Ready.status = STARTED
    thisExp.addData('Ready.started', Ready.tStart)
    Ready.maxDuration = None
    # keep track of which components have finished
    ReadyComponents = Ready.components
    for thisComponent in Ready.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Ready" ---
    thisExp.currentRoutine = Ready
    Ready.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Ready_text* updates
        
        # if Ready_text is starting this frame...
        if Ready_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ready_text.frameNStart = frameN  # exact frame index
            Ready_text.tStart = t  # local t and not account for scr refresh
            Ready_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ready_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ready_text.status = STARTED
            Ready_text.setAutoDraw(True)
        
        # if Ready_text is active this frame...
        if Ready_text.status == STARTED:
            # update params
            pass
        
        # *Ready_keyresp* updates
        waitOnFlip = False
        
        # if Ready_keyresp is starting this frame...
        if Ready_keyresp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Ready_keyresp.frameNStart = frameN  # exact frame index
            Ready_keyresp.tStart = t  # local t and not account for scr refresh
            Ready_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ready_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ready_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Ready_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Ready_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Ready_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = Ready_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Ready_keyresp_allKeys.extend(theseKeys)
            if len(_Ready_keyresp_allKeys):
                Ready_keyresp.keys = _Ready_keyresp_allKeys[-1].name  # just the last key pressed
                Ready_keyresp.rt = _Ready_keyresp_allKeys[-1].rt
                Ready_keyresp.duration = _Ready_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Ready,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Ready.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Ready.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Ready.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ready" ---
    for thisComponent in Ready.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Ready
    Ready.tStop = globalClock.getTime(format='float')
    Ready.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Ready.stopped', Ready.tStop)
    # check responses
    if Ready_keyresp.keys in ['', [], None]:  # No response was made
        Ready_keyresp.keys = None
    thisExp.addData('Ready_keyresp.keys',Ready_keyresp.keys)
    if Ready_keyresp.keys != None:  # we had a response
        thisExp.addData('Ready_keyresp.rt', Ready_keyresp.rt)
        thisExp.addData('Ready_keyresp.duration', Ready_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "Ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trials_Loop = data.TrialHandler2(
        name='Trials_Loop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Stimulus_Configurations.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(Trials_Loop)  # add the loop to the experiment
    thisTrials_Loop = Trials_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Loop.rgb)
    if thisTrials_Loop != None:
        for paramName in thisTrials_Loop:
            globals()[paramName] = thisTrials_Loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_Loop in Trials_Loop:
        Trials_Loop.status = STARTED
        if hasattr(thisTrials_Loop, 'status'):
            thisTrials_Loop.status = STARTED
        currentLoop = Trials_Loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Loop.rgb)
        if thisTrials_Loop != None:
            for paramName in thisTrials_Loop:
                globals()[paramName] = thisTrials_Loop[paramName]
        
        # --- Prepare to start Routine "Trial_Routine" ---
        # create an object to store info about Routine Trial_Routine
        Trial_Routine = data.Routine(
            name='Trial_Routine',
            components=[Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6, Fixation, Circle_1, Circle_2, Circle_3, Circle_4, Circle_5, Circle_6, Distractor, Anskey],
        )
        Trial_Routine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Stim_1.setOpacity(1.0)
        Stim_2.setOpacity(1.0)
        Stim_3.setOpacity(1.0)
        Stim_4.setOpacity(1.0)
        Stim_5.setOpacity(1.0)
        Stim_6.setOpacity(1.0)
        # Run 'Begin Routine' code from Trials_code
        import random
        
        # 1. 確保組件清單正確
        stims = [Stim_1, Stim_2, Stim_3, Stim_4, Stim_5, Stim_6]
        
        # 2. 位置隨機化計算
        num_fillers = diff_map[difficulty]
        other_indices = [i for i in range(6) if i != target_idx]
        random.shuffle(other_indices)
        filler_indices = other_indices[:num_fillers]
        
        # 3. 遍歷設定每個 Stim 組件的屬性
        for i, s_cong in enumerate(stims):
            if i == target_idx:
                # 設定目標（vertices 決定形狀，opacity 決定顯示與否）：
                s_cong.setVertices(shapes[target_type])
                s_cong.setOpacity(1)
            elif i in filler_indices:
                # 設定干擾物
                rand_f = random.choice(filler_pool)
                s_cong.setVertices(shapes[rand_f])
                s_cong.setOpacity(1)
            else:
                # 隱藏沒用到的位置
                s_cong.setOpacity(0)
        
        # 4. 設定外圍 Distractor
        if condition == 'cong':
            d_v = shapes[target_type]
        else:
            d_v = shapes['diamond'] if target_type == 'square' else shapes['square']
        
        Distractor.setVertices(d_v)
        Distractor.setOpacity(1)
        # 位置由 Excel 的 dist_pos_x 控制，這部分可以留在 Builder 的 Pos 欄位填 [dist_pos_x, 0]
        Distractor.setPos((dist_pos_x, 0))
        # create starting attributes for Anskey
        Anskey.keys = []
        Anskey.rt = []
        _Anskey_allKeys = []
        # store start times for Trial_Routine
        Trial_Routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Trial_Routine.tStart = globalClock.getTime(format='float')
        Trial_Routine.status = STARTED
        thisExp.addData('Trial_Routine.started', Trial_Routine.tStart)
        Trial_Routine.maxDuration = None
        # keep track of which components have finished
        Trial_RoutineComponents = Trial_Routine.components
        for thisComponent in Trial_Routine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial_Routine" ---
        thisExp.currentRoutine = Trial_Routine
        Trial_Routine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_Loop, 'status') and thisTrials_Loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_1* updates
            
            # if Stim_1 is starting this frame...
            if Stim_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_1.frameNStart = frameN  # exact frame index
                Stim_1.tStart = t  # local t and not account for scr refresh
                Stim_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_1.status = STARTED
                Stim_1.setAutoDraw(True)
            
            # if Stim_1 is active this frame...
            if Stim_1.status == STARTED:
                # update params
                pass
            
            # if Stim_1 is stopping this frame...
            if Stim_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_1.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_1.tStop = t  # not accounting for scr refresh
                    Stim_1.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_1.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_1.status = FINISHED
                    Stim_1.setAutoDraw(False)
            
            # *Stim_2* updates
            
            # if Stim_2 is starting this frame...
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_2.status = STARTED
                Stim_2.setAutoDraw(True)
            
            # if Stim_2 is active this frame...
            if Stim_2.status == STARTED:
                # update params
                pass
            
            # if Stim_2 is stopping this frame...
            if Stim_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_2.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_2.tStop = t  # not accounting for scr refresh
                    Stim_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_2.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_2.status = FINISHED
                    Stim_2.setAutoDraw(False)
            
            # *Stim_3* updates
            
            # if Stim_3 is starting this frame...
            if Stim_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_3.frameNStart = frameN  # exact frame index
                Stim_3.tStart = t  # local t and not account for scr refresh
                Stim_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_3.status = STARTED
                Stim_3.setAutoDraw(True)
            
            # if Stim_3 is active this frame...
            if Stim_3.status == STARTED:
                # update params
                pass
            
            # if Stim_3 is stopping this frame...
            if Stim_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_3.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_3.tStop = t  # not accounting for scr refresh
                    Stim_3.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_3.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_3.status = FINISHED
                    Stim_3.setAutoDraw(False)
            
            # *Stim_4* updates
            
            # if Stim_4 is starting this frame...
            if Stim_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_4.frameNStart = frameN  # exact frame index
                Stim_4.tStart = t  # local t and not account for scr refresh
                Stim_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_4.status = STARTED
                Stim_4.setAutoDraw(True)
            
            # if Stim_4 is active this frame...
            if Stim_4.status == STARTED:
                # update params
                pass
            
            # if Stim_4 is stopping this frame...
            if Stim_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_4.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_4.tStop = t  # not accounting for scr refresh
                    Stim_4.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_4.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_4.status = FINISHED
                    Stim_4.setAutoDraw(False)
            
            # *Stim_5* updates
            
            # if Stim_5 is starting this frame...
            if Stim_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_5.frameNStart = frameN  # exact frame index
                Stim_5.tStart = t  # local t and not account for scr refresh
                Stim_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_5.status = STARTED
                Stim_5.setAutoDraw(True)
            
            # if Stim_5 is active this frame...
            if Stim_5.status == STARTED:
                # update params
                pass
            
            # if Stim_5 is stopping this frame...
            if Stim_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_5.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_5.tStop = t  # not accounting for scr refresh
                    Stim_5.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_5.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_5.status = FINISHED
                    Stim_5.setAutoDraw(False)
            
            # *Stim_6* updates
            
            # if Stim_6 is starting this frame...
            if Stim_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Stim_6.frameNStart = frameN  # exact frame index
                Stim_6.tStart = t  # local t and not account for scr refresh
                Stim_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                Stim_6.status = STARTED
                Stim_6.setAutoDraw(True)
            
            # if Stim_6 is active this frame...
            if Stim_6.status == STARTED:
                # update params
                pass
            
            # if Stim_6 is stopping this frame...
            if Stim_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_6.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_6.tStop = t  # not accounting for scr refresh
                    Stim_6.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_6.frameNStop = frameN  # exact frame index
                    # update status
                    Stim_6.status = FINISHED
                    Stim_6.setAutoDraw(False)
            
            # *Fixation* updates
            
            # if Fixation is starting this frame...
            if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation.frameNStart = frameN  # exact frame index
                Fixation.tStart = t  # local t and not account for scr refresh
                Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                Fixation.status = STARTED
                Fixation.setAutoDraw(True)
            
            # if Fixation is active this frame...
            if Fixation.status == STARTED:
                # update params
                pass
            
            # if Fixation is stopping this frame...
            if Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation.tStop = t  # not accounting for scr refresh
                    Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    Fixation.frameNStop = frameN  # exact frame index
                    # update status
                    Fixation.status = FINISHED
                    Fixation.setAutoDraw(False)
            
            # *Circle_1* updates
            
            # if Circle_1 is starting this frame...
            if Circle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_1.frameNStart = frameN  # exact frame index
                Circle_1.tStart = t  # local t and not account for scr refresh
                Circle_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_1.status = STARTED
                Circle_1.setAutoDraw(True)
            
            # if Circle_1 is active this frame...
            if Circle_1.status == STARTED:
                # update params
                pass
            
            # if Circle_1 is stopping this frame...
            if Circle_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_1.tStop = t  # not accounting for scr refresh
                    Circle_1.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_1.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_1.status = FINISHED
                    Circle_1.setAutoDraw(False)
            
            # *Circle_2* updates
            
            # if Circle_2 is starting this frame...
            if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_2.frameNStart = frameN  # exact frame index
                Circle_2.tStart = t  # local t and not account for scr refresh
                Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_2.status = STARTED
                Circle_2.setAutoDraw(True)
            
            # if Circle_2 is active this frame...
            if Circle_2.status == STARTED:
                # update params
                pass
            
            # if Circle_2 is stopping this frame...
            if Circle_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_2.tStop = t  # not accounting for scr refresh
                    Circle_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_2.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_2.status = FINISHED
                    Circle_2.setAutoDraw(False)
            
            # *Circle_3* updates
            
            # if Circle_3 is starting this frame...
            if Circle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_3.frameNStart = frameN  # exact frame index
                Circle_3.tStart = t  # local t and not account for scr refresh
                Circle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_3.status = STARTED
                Circle_3.setAutoDraw(True)
            
            # if Circle_3 is active this frame...
            if Circle_3.status == STARTED:
                # update params
                pass
            
            # if Circle_3 is stopping this frame...
            if Circle_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_3.tStop = t  # not accounting for scr refresh
                    Circle_3.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_3.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_3.status = FINISHED
                    Circle_3.setAutoDraw(False)
            
            # *Circle_4* updates
            
            # if Circle_4 is starting this frame...
            if Circle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_4.frameNStart = frameN  # exact frame index
                Circle_4.tStart = t  # local t and not account for scr refresh
                Circle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_4.status = STARTED
                Circle_4.setAutoDraw(True)
            
            # if Circle_4 is active this frame...
            if Circle_4.status == STARTED:
                # update params
                pass
            
            # if Circle_4 is stopping this frame...
            if Circle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_4.tStop = t  # not accounting for scr refresh
                    Circle_4.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_4.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_4.status = FINISHED
                    Circle_4.setAutoDraw(False)
            
            # *Circle_5* updates
            
            # if Circle_5 is starting this frame...
            if Circle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_5.frameNStart = frameN  # exact frame index
                Circle_5.tStart = t  # local t and not account for scr refresh
                Circle_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_5.status = STARTED
                Circle_5.setAutoDraw(True)
            
            # if Circle_5 is active this frame...
            if Circle_5.status == STARTED:
                # update params
                pass
            
            # if Circle_5 is stopping this frame...
            if Circle_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_5.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_5.tStop = t  # not accounting for scr refresh
                    Circle_5.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_5.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_5.status = FINISHED
                    Circle_5.setAutoDraw(False)
            
            # *Circle_6* updates
            
            # if Circle_6 is starting this frame...
            if Circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_6.frameNStart = frameN  # exact frame index
                Circle_6.tStart = t  # local t and not account for scr refresh
                Circle_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle_6.status = STARTED
                Circle_6.setAutoDraw(True)
            
            # if Circle_6 is active this frame...
            if Circle_6.status == STARTED:
                # update params
                pass
            
            # if Circle_6 is stopping this frame...
            if Circle_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_6.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_6.tStop = t  # not accounting for scr refresh
                    Circle_6.tStopRefresh = tThisFlipGlobal  # on global time
                    Circle_6.frameNStop = frameN  # exact frame index
                    # update status
                    Circle_6.status = FINISHED
                    Circle_6.setAutoDraw(False)
            
            # *Distractor* updates
            
            # if Distractor is starting this frame...
            if Distractor.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Distractor.frameNStart = frameN  # exact frame index
                Distractor.tStart = t  # local t and not account for scr refresh
                Distractor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Distractor, 'tStartRefresh')  # time at next scr refresh
                # update status
                Distractor.status = STARTED
                Distractor.setAutoDraw(True)
            
            # if Distractor is active this frame...
            if Distractor.status == STARTED:
                # update params
                pass
            
            # if Distractor is stopping this frame...
            if Distractor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Distractor.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Distractor.tStop = t  # not accounting for scr refresh
                    Distractor.tStopRefresh = tThisFlipGlobal  # on global time
                    Distractor.frameNStop = frameN  # exact frame index
                    # update status
                    Distractor.status = FINISHED
                    Distractor.setAutoDraw(False)
            
            # *Anskey* updates
            waitOnFlip = False
            
            # if Anskey is starting this frame...
            if Anskey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Anskey.frameNStart = frameN  # exact frame index
                Anskey.tStart = t  # local t and not account for scr refresh
                Anskey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Anskey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Anskey.started')
                # update status
                Anskey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Anskey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Anskey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if Anskey is stopping this frame...
            if Anskey.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Anskey.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Anskey.tStop = t  # not accounting for scr refresh
                    Anskey.tStopRefresh = tThisFlipGlobal  # on global time
                    Anskey.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Anskey.stopped')
                    # update status
                    Anskey.status = FINISHED
                    Anskey.status = FINISHED
            if Anskey.status == STARTED and not waitOnFlip:
                theseKeys = Anskey.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _Anskey_allKeys.extend(theseKeys)
                if len(_Anskey_allKeys):
                    Anskey.keys = _Anskey_allKeys[-1].name  # just the last key pressed
                    Anskey.rt = _Anskey_allKeys[-1].rt
                    Anskey.duration = _Anskey_allKeys[-1].duration
                    # was this correct?
                    if (Anskey.keys == str(ans)) or (Anskey.keys == ans):
                        Anskey.corr = 1
                    else:
                        Anskey.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Trial_Routine,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Trial_Routine.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Trial_Routine.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Trial_Routine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Routine" ---
        for thisComponent in Trial_Routine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Trial_Routine
        Trial_Routine.tStop = globalClock.getTime(format='float')
        Trial_Routine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Trial_Routine.stopped', Trial_Routine.tStop)
        # Run 'End Routine' code from Trials_code
        # --- 練習回合的計數 ---
        if 'Prac_Loop' in locals() and Prac_Loop.status == STARTED:
            if Anskey.corr == 1:
                prac_corr_cnt += 1
        
        # --- 正式實驗的計數與統計 ---
        if 'Trials_Loop' in locals() and Trials_Loop.status == STARTED:
            # 休息計數
            total_trials_cnt += 1
            
            # 數據統計初始化
            if 'summary' not in expInfo:
                expInfo['summary'] = {'corr': 0, 'cong_rt': [], 'incong_rt': []}
            
            # 紀錄正確率與 RT
            if Anskey.corr == 1:
                expInfo['summary']['corr'] += 1
                if Anskey.rt is not None:
                    if condition == 'cong':
                        expInfo['summary']['cong_rt'].append(Anskey.rt)
                    else:
                        expInfo['summary']['incong_rt'].append(Anskey.rt)
        # check responses
        if Anskey.keys in ['', [], None]:  # No response was made
            Anskey.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               Anskey.corr = 1;  # correct non-response
            else:
               Anskey.corr = 0;  # failed to respond (incorrectly)
        # store data for Trials_Loop (TrialHandler)
        Trials_Loop.addData('Anskey.keys',Anskey.keys)
        Trials_Loop.addData('Anskey.corr', Anskey.corr)
        if Anskey.keys != None:  # we had a response
            Trials_Loop.addData('Anskey.rt', Anskey.rt)
            Trials_Loop.addData('Anskey.duration', Anskey.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Trial_Routine.maxDurationReached:
            routineTimer.addTime(-Trial_Routine.maxDuration)
        elif Trial_Routine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "BreakTime_Routine" ---
        # create an object to store info about Routine BreakTime_Routine
        BreakTime_Routine = data.Routine(
            name='BreakTime_Routine',
            components=[BreakTime_text, BreakTime_keyresp],
        )
        BreakTime_Routine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from BreakTime_code
        # 執行第 96 題後顯示休息畫面
        # 使用 total_trials_cnt % 96 == 0 且不為 0 的邏輯
        total_trials_cnt += 1
        
        if total_trials_cnt == 96:
            continueRoutine = True
        else:
            continueRoutine = False # 沒到 96 題就跳過休息
        # create starting attributes for BreakTime_keyresp
        BreakTime_keyresp.keys = []
        BreakTime_keyresp.rt = []
        _BreakTime_keyresp_allKeys = []
        # store start times for BreakTime_Routine
        BreakTime_Routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        BreakTime_Routine.tStart = globalClock.getTime(format='float')
        BreakTime_Routine.status = STARTED
        thisExp.addData('BreakTime_Routine.started', BreakTime_Routine.tStart)
        BreakTime_Routine.maxDuration = None
        # keep track of which components have finished
        BreakTime_RoutineComponents = BreakTime_Routine.components
        for thisComponent in BreakTime_Routine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "BreakTime_Routine" ---
        thisExp.currentRoutine = BreakTime_Routine
        BreakTime_Routine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_Loop, 'status') and thisTrials_Loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BreakTime_text* updates
            
            # if BreakTime_text is starting this frame...
            if BreakTime_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakTime_text.frameNStart = frameN  # exact frame index
                BreakTime_text.tStart = t  # local t and not account for scr refresh
                BreakTime_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakTime_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                BreakTime_text.status = STARTED
                BreakTime_text.setAutoDraw(True)
            
            # if BreakTime_text is active this frame...
            if BreakTime_text.status == STARTED:
                # update params
                pass
            
            # *BreakTime_keyresp* updates
            waitOnFlip = False
            
            # if BreakTime_keyresp is starting this frame...
            if BreakTime_keyresp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                BreakTime_keyresp.frameNStart = frameN  # exact frame index
                BreakTime_keyresp.tStart = t  # local t and not account for scr refresh
                BreakTime_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakTime_keyresp, 'tStartRefresh')  # time at next scr refresh
                # update status
                BreakTime_keyresp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(BreakTime_keyresp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(BreakTime_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if BreakTime_keyresp.status == STARTED and not waitOnFlip:
                theseKeys = BreakTime_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _BreakTime_keyresp_allKeys.extend(theseKeys)
                if len(_BreakTime_keyresp_allKeys):
                    BreakTime_keyresp.keys = _BreakTime_keyresp_allKeys[-1].name  # just the last key pressed
                    BreakTime_keyresp.rt = _BreakTime_keyresp_allKeys[-1].rt
                    BreakTime_keyresp.duration = _BreakTime_keyresp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=BreakTime_Routine,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                BreakTime_Routine.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if BreakTime_Routine.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in BreakTime_Routine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "BreakTime_Routine" ---
        for thisComponent in BreakTime_Routine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for BreakTime_Routine
        BreakTime_Routine.tStop = globalClock.getTime(format='float')
        BreakTime_Routine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('BreakTime_Routine.stopped', BreakTime_Routine.tStop)
        # Run 'End Routine' code from BreakTime_code
        if total_trials_cnt == 96:
            continueRoutine = True
            print("Break Time!")
        else:
            continueRoutine = False
        # check responses
        if BreakTime_keyresp.keys in ['', [], None]:  # No response was made
            BreakTime_keyresp.keys = None
        Trials_Loop.addData('BreakTime_keyresp.keys',BreakTime_keyresp.keys)
        if BreakTime_keyresp.keys != None:  # we had a response
            Trials_Loop.addData('BreakTime_keyresp.rt', BreakTime_keyresp.rt)
            Trials_Loop.addData('BreakTime_keyresp.duration', BreakTime_keyresp.duration)
        # the Routine "BreakTime_Routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrials_Loop as finished
        if hasattr(thisTrials_Loop, 'status'):
            thisTrials_Loop.status = FINISHED
        # if awaiting a pause, pause now
        if Trials_Loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Trials_Loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Trials_Loop'
    Trials_Loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "ThankYou" ---
    # create an object to store info about Routine ThankYou
    ThankYou = data.Routine(
        name='ThankYou',
        components=[Thanks_text, Thanks_keyresp],
    )
    ThankYou.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Thanks_code
    # 計算平均值
    stats = expInfo['summary']
    total_q = Trials_Loop.nTotal
    
    acc = (stats['corr'] / total_q) * 100
    avg_cong = sum(stats['cong_rt']) / len(stats['cong_rt']) if stats['cong_rt'] else 0
    avg_incong = sum(stats['incong_rt']) / len(stats['incong_rt']) if stats['incong_rt'] else 0
    
    avg_cong_ms = avg_cong * 1000
    avg_incong_ms = avg_incong * 1000
    
    # 2. 格式化顯示文字
    # 使用 :.2f 將數值格式化為小數點後兩位
    # 並將單位字樣從「秒」更換為「毫秒」
    final_msg = f"作業結束，您的表現如下：\n\n" \
                f"總正確率：{acc:.1f}%\n" \
                f"[Congruent] RT：{avg_cong_ms:.2f} 毫秒\n" \
                f"[Incongruent] RT：{avg_incong_ms:.2f} 毫秒\n\n" \
                f"感謝您的參與！\n\n\n" \
                f"【請按「空白鍵」退出作業】"
    Thanks_text.setText(final_msg)
    # create starting attributes for Thanks_keyresp
    Thanks_keyresp.keys = []
    Thanks_keyresp.rt = []
    _Thanks_keyresp_allKeys = []
    # store start times for ThankYou
    ThankYou.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ThankYou.tStart = globalClock.getTime(format='float')
    ThankYou.status = STARTED
    thisExp.addData('ThankYou.started', ThankYou.tStart)
    ThankYou.maxDuration = None
    # keep track of which components have finished
    ThankYouComponents = ThankYou.components
    for thisComponent in ThankYou.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYou" ---
    thisExp.currentRoutine = ThankYou
    ThankYou.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Thanks_text* updates
        
        # if Thanks_text is starting this frame...
        if Thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thanks_text.frameNStart = frameN  # exact frame index
            Thanks_text.tStart = t  # local t and not account for scr refresh
            Thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thanks_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Thanks_text.status = STARTED
            Thanks_text.setAutoDraw(True)
        
        # if Thanks_text is active this frame...
        if Thanks_text.status == STARTED:
            # update params
            pass
        
        # if Thanks_text is stopping this frame...
        if Thanks_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Thanks_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                Thanks_text.tStop = t  # not accounting for scr refresh
                Thanks_text.tStopRefresh = tThisFlipGlobal  # on global time
                Thanks_text.frameNStop = frameN  # exact frame index
                # update status
                Thanks_text.status = FINISHED
                Thanks_text.setAutoDraw(False)
        
        # *Thanks_keyresp* updates
        waitOnFlip = False
        
        # if Thanks_keyresp is starting this frame...
        if Thanks_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thanks_keyresp.frameNStart = frameN  # exact frame index
            Thanks_keyresp.tStart = t  # local t and not account for scr refresh
            Thanks_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thanks_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            Thanks_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Thanks_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Thanks_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Thanks_keyresp is stopping this frame...
        if Thanks_keyresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Thanks_keyresp.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                Thanks_keyresp.tStop = t  # not accounting for scr refresh
                Thanks_keyresp.tStopRefresh = tThisFlipGlobal  # on global time
                Thanks_keyresp.frameNStop = frameN  # exact frame index
                # update status
                Thanks_keyresp.status = FINISHED
                Thanks_keyresp.status = FINISHED
        if Thanks_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = Thanks_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Thanks_keyresp_allKeys.extend(theseKeys)
            if len(_Thanks_keyresp_allKeys):
                Thanks_keyresp.keys = _Thanks_keyresp_allKeys[-1].name  # just the last key pressed
                Thanks_keyresp.rt = _Thanks_keyresp_allKeys[-1].rt
                Thanks_keyresp.duration = _Thanks_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ThankYou,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            ThankYou.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if ThankYou.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in ThankYou.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYou" ---
    for thisComponent in ThankYou.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ThankYou
    ThankYou.tStop = globalClock.getTime(format='float')
    ThankYou.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ThankYou.stopped', ThankYou.tStop)
    # check responses
    if Thanks_keyresp.keys in ['', [], None]:  # No response was made
        Thanks_keyresp.keys = None
    thisExp.addData('Thanks_keyresp.keys',Thanks_keyresp.keys)
    if Thanks_keyresp.keys != None:  # we had a response
        thisExp.addData('Thanks_keyresp.rt', Thanks_keyresp.rt)
        thisExp.addData('Thanks_keyresp.duration', Thanks_keyresp.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ThankYou.maxDurationReached:
        routineTimer.addTime(-ThankYou.maxDuration)
    elif ThankYou.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
