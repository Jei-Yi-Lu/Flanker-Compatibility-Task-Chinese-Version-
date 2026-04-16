/*********************************** 
 * Flanker Compatibility Task *
 ***********************************/


// store info about the experiment session:
let expName = 'Flanker Compatibility Task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999)).toFixed(0), 6)}`,
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('Black'),
  units: 'deg',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(IntroRoutineBegin());
flowScheduler.add(IntroRoutineEachFrame());
flowScheduler.add(IntroRoutineEnd());
const Prac_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Prac_LoopLoopBegin(Prac_LoopLoopScheduler));
flowScheduler.add(Prac_LoopLoopScheduler);
flowScheduler.add(Prac_LoopLoopEnd);


flowScheduler.add(ReadyRoutineBegin());
flowScheduler.add(ReadyRoutineEachFrame());
flowScheduler.add(ReadyRoutineEnd());
const Trials_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Trials_LoopLoopBegin(Trials_LoopLoopScheduler));
flowScheduler.add(Trials_LoopLoopScheduler);
flowScheduler.add(Trials_LoopLoopEnd);


flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Prac_Stimulus_Configurations.xlsx', 'path': 'Prac_Stimulus_Configurations.xlsx'},
    {'name': 'Stimulus_Configurations.xlsx', 'path': 'Stimulus_Configurations.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var IntroClock;
var Intro_text;
var Intro_keyresp;
var Trial_RoutineClock;
var Stim_1;
var Stim_2;
var Stim_3;
var Stim_4;
var Stim_5;
var Stim_6;
var Fixation;
var Circle_1;
var Circle_2;
var Circle_3;
var Circle_4;
var Circle_5;
var Circle_6;
var Distractor;
var Anskey;
var ReadyClock;
var Ready_text;
var Ready_keyresp;
var ThankYouClock;
var Thanks_text;
var Thanks_keyresp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Intro"
  IntroClock = new util.Clock();
  Intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Intro_text',
    text: '歡迎參與本作業。\n\n您將看到六個圓圈圍繞螢幕中央的十字凝視點。\n作業過程中，可能會有數量不等的形狀個別出現在圓圈中。\n\n請您在看到形狀出現後，盡快判斷「圓圈內的形狀」\n是否包含「正方形」或「菱形」，\n並盡可能又快又正確地按鍵反應：\n\n- 圓圈內出現正方形：按下「A」鍵。\n- 圓圈內出現菱形：按下「L」鍵。\n\n然而，請無視圓圈之外出現的正方形或菱形，\n並只判斷「圓圈內」的形狀包含正方形或菱形。\n\n我們會先練習個幾題，再開始正式作業。\n\n\n【準備好後，請按「空白鍵」開始練習】\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.5,  wrapWidth: 26.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Intro_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial_Routine"
  Trial_RoutineClock = new util.Clock();
  Stim_1 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_1', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [0, 6], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: 0, 
    interpolate: true, 
  });
  
  Stim_2 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_2', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [5.2, 3], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -1, 
    interpolate: true, 
  });
  
  Stim_3 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_3', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [5.2, (- 3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  Stim_4 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_4', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 6)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -3, 
    interpolate: true, 
  });
  
  Stim_5 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_5', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [(- 5.2), (- 3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -4, 
    interpolate: true, 
  });
  
  Stim_6 = new visual.ShapeStim({
    win: psychoJS.window, name: 'Stim_6', 
    vertices: 4, size: [1, 1],
    ori: 0.0, 
    pos: [(- 5.2), 3], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -5, 
    interpolate: true, 
  });
  
  Fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.75,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  Circle_1 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_1', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [0, 6], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -8, 
    interpolate: true, 
  });
  
  Circle_2 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_2', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [5.2, 3], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -9, 
    interpolate: true, 
  });
  
  Circle_3 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_3', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [5.2, (- 3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -10, 
    interpolate: true, 
  });
  
  Circle_4 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_4', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [0, (- 6)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -11, 
    interpolate: true, 
  });
  
  Circle_5 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_5', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [(- 5.2), (- 3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -12, 
    interpolate: true, 
  });
  
  Circle_6 = new visual.Polygon({
    win: psychoJS.window, name: 'Circle_6', 
    edges: 100, size:[3, 3],
    ori: 0.0, 
    pos: [(- 5.2), 3], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('white'), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -13, 
    interpolate: true, 
  });
  
  Distractor = new visual.ShapeStim({
    win: psychoJS.window, name: 'Distractor', 
    vertices: 4, size: [1.5, 1.5],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -14, 
    interpolate: true, 
  });
  
  Anskey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ready"
  ReadyClock = new util.Clock();
  Ready_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ready_text',
    text: '接下來即將開始正式作業。\n\n\n請您在看到形狀出現後，盡快判斷「圓圈內的形狀」\n是否包含「正方形」或「菱形」，\n並盡可能又快又正確地按鍵反應：\n\n- 圓圈內出現正方形：按下「A」鍵。\n- 圓圈內出現菱形：按下「L」鍵。\n\n然而，請無視圓圈之外出現的正方形或菱形，\n並只判斷「圓圈內」的形狀包含正方形或菱形。\n\n\n【準備好後，請按「空白鍵」開始正式作業】\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.5,  wrapWidth: 26.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Ready_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  Thanks_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Thanks_text',
    text: '作業結束。\n\n感謝您的參與及配合！\n\n\n【請按「空白鍵」退出】',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: 26.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Thanks_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var IntroMaxDurationReached;
var _Intro_keyresp_allKeys;
var IntroMaxDuration;
var IntroComponents;
function IntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Intro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    IntroClock.reset();
    routineTimer.reset();
    IntroMaxDurationReached = false;
    // update component parameters for each repeat
    Intro_keyresp.keys = undefined;
    Intro_keyresp.rt = undefined;
    _Intro_keyresp_allKeys = [];
    psychoJS.experiment.addData('Intro.started', globalClock.getTime());
    IntroMaxDuration = null
    // keep track of which components have finished
    IntroComponents = [];
    IntroComponents.push(Intro_text);
    IntroComponents.push(Intro_keyresp);
    
    IntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function IntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Intro' ---
    // get current time
    t = IntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Intro_text* updates
    if (t >= 0.0 && Intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro_text.tStart = t;  // (not accounting for frame time here)
      Intro_text.frameNStart = frameN;  // exact frame index
      
      Intro_text.setAutoDraw(true);
    }
    
    
    // if Intro_text is active this frame...
    if (Intro_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *Intro_keyresp* updates
    if (t >= 0.5 && Intro_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro_keyresp.tStart = t;  // (not accounting for frame time here)
      Intro_keyresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Intro_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Intro_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Intro_keyresp.clearEvents(); });
    }
    
    // if Intro_keyresp is active this frame...
    if (Intro_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Intro_keyresp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _Intro_keyresp_allKeys = _Intro_keyresp_allKeys.concat(theseKeys);
      if (_Intro_keyresp_allKeys.length > 0) {
        Intro_keyresp.keys = _Intro_keyresp_allKeys[_Intro_keyresp_allKeys.length - 1].name;  // just the last key pressed
        Intro_keyresp.rt = _Intro_keyresp_allKeys[_Intro_keyresp_allKeys.length - 1].rt;
        Intro_keyresp.duration = _Intro_keyresp_allKeys[_Intro_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    IntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Intro' ---
    IntroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Intro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Intro_keyresp.corr, level);
    }
    psychoJS.experiment.addData('Intro_keyresp.keys', Intro_keyresp.keys);
    if (typeof Intro_keyresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Intro_keyresp.rt', Intro_keyresp.rt);
        psychoJS.experiment.addData('Intro_keyresp.duration', Intro_keyresp.duration);
        routineTimer.reset();
        }
    
    Intro_keyresp.stop();
    // the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prac_Loop;
function Prac_LoopLoopBegin(Prac_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Prac_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Prac_Stimulus_Configurations.xlsx',
      seed: undefined, name: 'Prac_Loop'
    });
    psychoJS.experiment.addLoop(Prac_Loop); // add the loop to the experiment
    currentLoop = Prac_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Prac_Loop.forEach(function() {
      snapshot = Prac_Loop.getSnapshot();
    
      Prac_LoopLoopScheduler.add(importConditions(snapshot));
      Prac_LoopLoopScheduler.add(Trial_RoutineRoutineBegin(snapshot));
      Prac_LoopLoopScheduler.add(Trial_RoutineRoutineEachFrame());
      Prac_LoopLoopScheduler.add(Trial_RoutineRoutineEnd(snapshot));
      Prac_LoopLoopScheduler.add(Prac_LoopLoopEndIteration(Prac_LoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Prac_LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Prac_Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Prac_LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trials_Loop;
function Trials_LoopLoopBegin(Trials_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trials_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimulus_Configurations.xlsx',
      seed: undefined, name: 'Trials_Loop'
    });
    psychoJS.experiment.addLoop(Trials_Loop); // add the loop to the experiment
    currentLoop = Trials_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Trials_Loop.forEach(function() {
      snapshot = Trials_Loop.getSnapshot();
    
      Trials_LoopLoopScheduler.add(importConditions(snapshot));
      Trials_LoopLoopScheduler.add(Trial_RoutineRoutineBegin(snapshot));
      Trials_LoopLoopScheduler.add(Trial_RoutineRoutineEachFrame());
      Trials_LoopLoopScheduler.add(Trial_RoutineRoutineEnd(snapshot));
      Trials_LoopLoopScheduler.add(Trials_LoopLoopEndIteration(Trials_LoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Trials_LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trials_Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Trials_LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trial_RoutineMaxDurationReached;
var _Anskey_allKeys;
var Trial_RoutineMaxDuration;
var Trial_RoutineComponents;
function Trial_RoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_Routine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Trial_RoutineClock.reset(routineTimer.getTime());
    routineTimer.add(4.000000);
    Trial_RoutineMaxDurationReached = false;
    // update component parameters for each repeat
    Stim_1.setOpacity(1.0);
    Stim_2.setOpacity(1.0);
    Stim_3.setOpacity(1.0);
    Stim_4.setOpacity(1.0);
    Stim_5.setOpacity(1.0);
    Stim_6.setOpacity(1.0);
    // Run 'Begin Routine' code from Trials_code_2
    /* Syntax Error: Fix Python code */
    Distractor.setPos([dist_pos_x, 0]);
    Anskey.keys = undefined;
    Anskey.rt = undefined;
    _Anskey_allKeys = [];
    psychoJS.experiment.addData('Trial_Routine.started', globalClock.getTime());
    Trial_RoutineMaxDuration = null
    // keep track of which components have finished
    Trial_RoutineComponents = [];
    Trial_RoutineComponents.push(Stim_1);
    Trial_RoutineComponents.push(Stim_2);
    Trial_RoutineComponents.push(Stim_3);
    Trial_RoutineComponents.push(Stim_4);
    Trial_RoutineComponents.push(Stim_5);
    Trial_RoutineComponents.push(Stim_6);
    Trial_RoutineComponents.push(Fixation);
    Trial_RoutineComponents.push(Circle_1);
    Trial_RoutineComponents.push(Circle_2);
    Trial_RoutineComponents.push(Circle_3);
    Trial_RoutineComponents.push(Circle_4);
    Trial_RoutineComponents.push(Circle_5);
    Trial_RoutineComponents.push(Circle_6);
    Trial_RoutineComponents.push(Distractor);
    Trial_RoutineComponents.push(Anskey);
    
    Trial_RoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Trial_RoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_Routine' ---
    // get current time
    t = Trial_RoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Stim_1* updates
    if (t >= 0.5 && Stim_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_1.tStart = t;  // (not accounting for frame time here)
      Stim_1.frameNStart = frameN;  // exact frame index
      
      Stim_1.setAutoDraw(true);
    }
    
    
    // if Stim_1 is active this frame...
    if (Stim_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_1.tStop = t;  // not accounting for scr refresh
      Stim_1.frameNStop = frameN;  // exact frame index
      // update status
      Stim_1.status = PsychoJS.Status.FINISHED;
      Stim_1.setAutoDraw(false);
    }
    
    
    // *Stim_2* updates
    if (t >= 0.5 && Stim_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_2.tStart = t;  // (not accounting for frame time here)
      Stim_2.frameNStart = frameN;  // exact frame index
      
      Stim_2.setAutoDraw(true);
    }
    
    
    // if Stim_2 is active this frame...
    if (Stim_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_2.tStop = t;  // not accounting for scr refresh
      Stim_2.frameNStop = frameN;  // exact frame index
      // update status
      Stim_2.status = PsychoJS.Status.FINISHED;
      Stim_2.setAutoDraw(false);
    }
    
    
    // *Stim_3* updates
    if (t >= 0.5 && Stim_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_3.tStart = t;  // (not accounting for frame time here)
      Stim_3.frameNStart = frameN;  // exact frame index
      
      Stim_3.setAutoDraw(true);
    }
    
    
    // if Stim_3 is active this frame...
    if (Stim_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_3.tStop = t;  // not accounting for scr refresh
      Stim_3.frameNStop = frameN;  // exact frame index
      // update status
      Stim_3.status = PsychoJS.Status.FINISHED;
      Stim_3.setAutoDraw(false);
    }
    
    
    // *Stim_4* updates
    if (t >= 0.5 && Stim_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_4.tStart = t;  // (not accounting for frame time here)
      Stim_4.frameNStart = frameN;  // exact frame index
      
      Stim_4.setAutoDraw(true);
    }
    
    
    // if Stim_4 is active this frame...
    if (Stim_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_4.tStop = t;  // not accounting for scr refresh
      Stim_4.frameNStop = frameN;  // exact frame index
      // update status
      Stim_4.status = PsychoJS.Status.FINISHED;
      Stim_4.setAutoDraw(false);
    }
    
    
    // *Stim_5* updates
    if (t >= 0.5 && Stim_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_5.tStart = t;  // (not accounting for frame time here)
      Stim_5.frameNStart = frameN;  // exact frame index
      
      Stim_5.setAutoDraw(true);
    }
    
    
    // if Stim_5 is active this frame...
    if (Stim_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_5.tStop = t;  // not accounting for scr refresh
      Stim_5.frameNStop = frameN;  // exact frame index
      // update status
      Stim_5.status = PsychoJS.Status.FINISHED;
      Stim_5.setAutoDraw(false);
    }
    
    
    // *Stim_6* updates
    if (t >= 0.5 && Stim_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_6.tStart = t;  // (not accounting for frame time here)
      Stim_6.frameNStart = frameN;  // exact frame index
      
      Stim_6.setAutoDraw(true);
    }
    
    
    // if Stim_6 is active this frame...
    if (Stim_6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Stim_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Stim_6.tStop = t;  // not accounting for scr refresh
      Stim_6.frameNStop = frameN;  // exact frame index
      // update status
      Stim_6.status = PsychoJS.Status.FINISHED;
      Stim_6.setAutoDraw(false);
    }
    
    
    // *Fixation* updates
    if (t >= 0.0 && Fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation.tStart = t;  // (not accounting for frame time here)
      Fixation.frameNStart = frameN;  // exact frame index
      
      Fixation.setAutoDraw(true);
    }
    
    
    // if Fixation is active this frame...
    if (Fixation.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Fixation.tStop = t;  // not accounting for scr refresh
      Fixation.frameNStop = frameN;  // exact frame index
      // update status
      Fixation.status = PsychoJS.Status.FINISHED;
      Fixation.setAutoDraw(false);
    }
    
    
    // *Circle_1* updates
    if (t >= 0.0 && Circle_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_1.tStart = t;  // (not accounting for frame time here)
      Circle_1.frameNStart = frameN;  // exact frame index
      
      Circle_1.setAutoDraw(true);
    }
    
    
    // if Circle_1 is active this frame...
    if (Circle_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_1.tStop = t;  // not accounting for scr refresh
      Circle_1.frameNStop = frameN;  // exact frame index
      // update status
      Circle_1.status = PsychoJS.Status.FINISHED;
      Circle_1.setAutoDraw(false);
    }
    
    
    // *Circle_2* updates
    if (t >= 0.0 && Circle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_2.tStart = t;  // (not accounting for frame time here)
      Circle_2.frameNStart = frameN;  // exact frame index
      
      Circle_2.setAutoDraw(true);
    }
    
    
    // if Circle_2 is active this frame...
    if (Circle_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_2.tStop = t;  // not accounting for scr refresh
      Circle_2.frameNStop = frameN;  // exact frame index
      // update status
      Circle_2.status = PsychoJS.Status.FINISHED;
      Circle_2.setAutoDraw(false);
    }
    
    
    // *Circle_3* updates
    if (t >= 0.0 && Circle_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_3.tStart = t;  // (not accounting for frame time here)
      Circle_3.frameNStart = frameN;  // exact frame index
      
      Circle_3.setAutoDraw(true);
    }
    
    
    // if Circle_3 is active this frame...
    if (Circle_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_3.tStop = t;  // not accounting for scr refresh
      Circle_3.frameNStop = frameN;  // exact frame index
      // update status
      Circle_3.status = PsychoJS.Status.FINISHED;
      Circle_3.setAutoDraw(false);
    }
    
    
    // *Circle_4* updates
    if (t >= 0.0 && Circle_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_4.tStart = t;  // (not accounting for frame time here)
      Circle_4.frameNStart = frameN;  // exact frame index
      
      Circle_4.setAutoDraw(true);
    }
    
    
    // if Circle_4 is active this frame...
    if (Circle_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_4.tStop = t;  // not accounting for scr refresh
      Circle_4.frameNStop = frameN;  // exact frame index
      // update status
      Circle_4.status = PsychoJS.Status.FINISHED;
      Circle_4.setAutoDraw(false);
    }
    
    
    // *Circle_5* updates
    if (t >= 0.0 && Circle_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_5.tStart = t;  // (not accounting for frame time here)
      Circle_5.frameNStart = frameN;  // exact frame index
      
      Circle_5.setAutoDraw(true);
    }
    
    
    // if Circle_5 is active this frame...
    if (Circle_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_5.tStop = t;  // not accounting for scr refresh
      Circle_5.frameNStop = frameN;  // exact frame index
      // update status
      Circle_5.status = PsychoJS.Status.FINISHED;
      Circle_5.setAutoDraw(false);
    }
    
    
    // *Circle_6* updates
    if (t >= 0.0 && Circle_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_6.tStart = t;  // (not accounting for frame time here)
      Circle_6.frameNStart = frameN;  // exact frame index
      
      Circle_6.setAutoDraw(true);
    }
    
    
    // if Circle_6 is active this frame...
    if (Circle_6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Circle_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Circle_6.tStop = t;  // not accounting for scr refresh
      Circle_6.frameNStop = frameN;  // exact frame index
      // update status
      Circle_6.status = PsychoJS.Status.FINISHED;
      Circle_6.setAutoDraw(false);
    }
    
    
    // *Distractor* updates
    if (t >= 0.5 && Distractor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Distractor.tStart = t;  // (not accounting for frame time here)
      Distractor.frameNStart = frameN;  // exact frame index
      
      Distractor.setAutoDraw(true);
    }
    
    
    // if Distractor is active this frame...
    if (Distractor.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Distractor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Distractor.tStop = t;  // not accounting for scr refresh
      Distractor.frameNStop = frameN;  // exact frame index
      // update status
      Distractor.status = PsychoJS.Status.FINISHED;
      Distractor.setAutoDraw(false);
    }
    
    
    // *Anskey* updates
    if (t >= 0.5 && Anskey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Anskey.tStart = t;  // (not accounting for frame time here)
      Anskey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Anskey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Anskey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Anskey.clearEvents(); });
    }
    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Anskey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      Anskey.tStop = t;  // not accounting for scr refresh
      Anskey.frameNStop = frameN;  // exact frame index
      // update status
      Anskey.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Anskey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Anskey.tStop = t;  // not accounting for scr refresh
        Anskey.frameNStop = frameN;  // exact frame index
        // update status
        Anskey.status = PsychoJS.Status.FINISHED;
        Anskey.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if Anskey is active this frame...
      if (Anskey.status === PsychoJS.Status.STARTED) {
        let theseKeys = Anskey.getKeys({
          keyList: typeof ['a','l'] === 'string' ? [['a','l']] : ['a','l'], 
          waitRelease: false
        });
        _Anskey_allKeys = _Anskey_allKeys.concat(theseKeys);
        if (_Anskey_allKeys.length > 0) {
          Anskey.keys = _Anskey_allKeys[_Anskey_allKeys.length - 1].name;  // just the last key pressed
          Anskey.rt = _Anskey_allKeys[_Anskey_allKeys.length - 1].rt;
          Anskey.duration = _Anskey_allKeys[_Anskey_allKeys.length - 1].duration;
          // was this correct?
          if (Anskey.keys == ans) {
              Anskey.corr = 1;
          } else {
              Anskey.corr = 0;
          }
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Trial_RoutineComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Trial_RoutineRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Trial_Routine' ---
      Trial_RoutineComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Trial_Routine.stopped', globalClock.getTime());
      // was no response the correct answer?!
      if (Anskey.keys === undefined) {
        if (['None','none',undefined].includes(ans)) {
           Anskey.corr = 1;  // correct non-response
        } else {
           Anskey.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(Anskey.corr, level);
      }
      psychoJS.experiment.addData('Anskey.keys', Anskey.keys);
      psychoJS.experiment.addData('Anskey.corr', Anskey.corr);
      if (typeof Anskey.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('Anskey.rt', Anskey.rt);
          psychoJS.experiment.addData('Anskey.duration', Anskey.duration);
          routineTimer.reset();
          }
      
      Anskey.stop();
      if (routineForceEnded) {
          routineTimer.reset();} else if (Trial_RoutineMaxDurationReached) {
          Trial_RoutineClock.add(Trial_RoutineMaxDuration);
      } else {
          Trial_RoutineClock.add(4.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var ReadyMaxDurationReached;
var _Ready_keyresp_allKeys;
var ReadyMaxDuration;
var ReadyComponents;
function ReadyRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Ready' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      ReadyClock.reset();
      routineTimer.reset();
      ReadyMaxDurationReached = false;
      // update component parameters for each repeat
      Ready_keyresp.keys = undefined;
      Ready_keyresp.rt = undefined;
      _Ready_keyresp_allKeys = [];
      psychoJS.experiment.addData('Ready.started', globalClock.getTime());
      ReadyMaxDuration = null
      // keep track of which components have finished
      ReadyComponents = [];
      ReadyComponents.push(Ready_text);
      ReadyComponents.push(Ready_keyresp);
      
      ReadyComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function ReadyRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Ready' ---
      // get current time
      t = ReadyClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *Ready_text* updates
      if (t >= 0.0 && Ready_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Ready_text.tStart = t;  // (not accounting for frame time here)
        Ready_text.frameNStart = frameN;  // exact frame index
        
        Ready_text.setAutoDraw(true);
      }
      
      
      // if Ready_text is active this frame...
      if (Ready_text.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Ready_keyresp* updates
      if (t >= 0.5 && Ready_keyresp.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Ready_keyresp.tStart = t;  // (not accounting for frame time here)
        Ready_keyresp.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { Ready_keyresp.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { Ready_keyresp.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { Ready_keyresp.clearEvents(); });
      }
      
      // if Ready_keyresp is active this frame...
      if (Ready_keyresp.status === PsychoJS.Status.STARTED) {
        let theseKeys = Ready_keyresp.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _Ready_keyresp_allKeys = _Ready_keyresp_allKeys.concat(theseKeys);
        if (_Ready_keyresp_allKeys.length > 0) {
          Ready_keyresp.keys = _Ready_keyresp_allKeys[_Ready_keyresp_allKeys.length - 1].name;  // just the last key pressed
          Ready_keyresp.rt = _Ready_keyresp_allKeys[_Ready_keyresp_allKeys.length - 1].rt;
          Ready_keyresp.duration = _Ready_keyresp_allKeys[_Ready_keyresp_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      ReadyComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function ReadyRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Ready' ---
      ReadyComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Ready.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(Ready_keyresp.corr, level);
      }
      psychoJS.experiment.addData('Ready_keyresp.keys', Ready_keyresp.keys);
      if (typeof Ready_keyresp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('Ready_keyresp.rt', Ready_keyresp.rt);
          psychoJS.experiment.addData('Ready_keyresp.duration', Ready_keyresp.duration);
          routineTimer.reset();
          }
      
      Ready_keyresp.stop();
      // the Routine "Ready" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var ThankYouMaxDurationReached;
var _Thanks_keyresp_allKeys;
var ThankYouMaxDuration;
var ThankYouComponents;
function ThankYouRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'ThankYou' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      ThankYouClock.reset(routineTimer.getTime());
      routineTimer.add(10.000000);
      ThankYouMaxDurationReached = false;
      // update component parameters for each repeat
      Thanks_keyresp.keys = undefined;
      Thanks_keyresp.rt = undefined;
      _Thanks_keyresp_allKeys = [];
      psychoJS.experiment.addData('ThankYou.started', globalClock.getTime());
      ThankYouMaxDuration = null
      // keep track of which components have finished
      ThankYouComponents = [];
      ThankYouComponents.push(Thanks_text);
      ThankYouComponents.push(Thanks_keyresp);
      
      ThankYouComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function ThankYouRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'ThankYou' ---
      // get current time
      t = ThankYouClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *Thanks_text* updates
      if (t >= 0.0 && Thanks_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Thanks_text.tStart = t;  // (not accounting for frame time here)
        Thanks_text.frameNStart = frameN;  // exact frame index
        
        Thanks_text.setAutoDraw(true);
      }
      
      
      // if Thanks_text is active this frame...
      if (Thanks_text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Thanks_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Thanks_text.tStop = t;  // not accounting for scr refresh
        Thanks_text.frameNStop = frameN;  // exact frame index
        // update status
        Thanks_text.status = PsychoJS.Status.FINISHED;
        Thanks_text.setAutoDraw(false);
      }
      
      
      // *Thanks_keyresp* updates
      if (t >= 0.0 && Thanks_keyresp.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Thanks_keyresp.tStart = t;  // (not accounting for frame time here)
        Thanks_keyresp.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { Thanks_keyresp.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { Thanks_keyresp.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { Thanks_keyresp.clearEvents(); });
      }
      frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Thanks_keyresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Thanks_keyresp.tStop = t;  // not accounting for scr refresh
        Thanks_keyresp.frameNStop = frameN;  // exact frame index
        // update status
        Thanks_keyresp.status = PsychoJS.Status.FINISHED;
        frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (Thanks_keyresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          Thanks_keyresp.tStop = t;  // not accounting for scr refresh
          Thanks_keyresp.frameNStop = frameN;  // exact frame index
          // update status
          Thanks_keyresp.status = PsychoJS.Status.FINISHED;
          Thanks_keyresp.status = PsychoJS.Status.FINISHED;
            }
          
        }
        
        // if Thanks_keyresp is active this frame...
        if (Thanks_keyresp.status === PsychoJS.Status.STARTED) {
          let theseKeys = Thanks_keyresp.getKeys({
            keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
            waitRelease: false
          });
          _Thanks_keyresp_allKeys = _Thanks_keyresp_allKeys.concat(theseKeys);
          if (_Thanks_keyresp_allKeys.length > 0) {
            Thanks_keyresp.keys = _Thanks_keyresp_allKeys[_Thanks_keyresp_allKeys.length - 1].name;  // just the last key pressed
            Thanks_keyresp.rt = _Thanks_keyresp_allKeys[_Thanks_keyresp_allKeys.length - 1].rt;
            Thanks_keyresp.duration = _Thanks_keyresp_allKeys[_Thanks_keyresp_allKeys.length - 1].duration;
            // a response ends the routine
            continueRoutine = false;
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        ThankYouComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function ThankYouRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'ThankYou' ---
        ThankYouComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('ThankYou.stopped', globalClock.getTime());
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(Thanks_keyresp.corr, level);
        }
        psychoJS.experiment.addData('Thanks_keyresp.keys', Thanks_keyresp.keys);
        if (typeof Thanks_keyresp.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('Thanks_keyresp.rt', Thanks_keyresp.rt);
            psychoJS.experiment.addData('Thanks_keyresp.duration', Thanks_keyresp.duration);
            routineTimer.reset();
            }
        
        Thanks_keyresp.stop();
        if (routineForceEnded) {
            routineTimer.reset();} else if (ThankYouMaxDurationReached) {
            ThankYouClock.add(ThankYouMaxDuration);
        } else {
            ThankYouClock.add(10.000000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
function importConditions(currentLoop) {
      return async function () {
        psychoJS.importAttributes(currentLoop.getCurrentTrial());
        return Scheduler.Event.NEXT;
        };
    }
    
    
async function quitPsychoJS(message, isCompleted) {
      // Check for and save orphaned data
      if (psychoJS.experiment.isEntryEmpty()) {
        psychoJS.experiment.nextEntry();
      }
      psychoJS.window.close();
      psychoJS.quit({message: message, isCompleted: isCompleted});
      
      return Scheduler.Event.QUIT;
    }
