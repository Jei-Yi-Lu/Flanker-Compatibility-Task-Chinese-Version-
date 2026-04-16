# Flanker Compatibility Task

Task Version:
Green, C. S., & Bavelier, D. (2003). Action video game modifies visual selective attention. Nature, 423(6939), 534-537.



## The Label in Data Output (.csv)

*difficulty*: the number of the stimulus in the circles (1: target only; 2: including target and one other stimulus; 3: including target and three other stimuli; 4: including target and five other stimuli).

*target_type*: the target (i.e., square or diamond) in the circles.

*compatibility*: the target type is the same (i.e., compatible, comp) or different (i.e., incompatible, incomp) from the distractor out of the circles.

*dist_pos_x*: the x-axis position of the distractor that is out of the circles.

*ans*: the correct answer for the trial (a: square appears in the circle; l: diamond appears in the circle)

*target_idx*: the position where the target appears (the coordinate of 1 to 6,  1: (0, 6); 2: (5.20, 3); 3: (5.20, -3), 4: : (0,-6), 5: (-5.20, -3), 6: (-5.20, 3))

*Anskey.corr*: correct or not for each trial (1 = correct; 0 = incorrect).

*Anskey.rt*: reaction time of the key response for each trial (unit: second).





## Data Analysis (.py)

1. The data in the practice routine will be excluded.

2. The pilot data will be excluded if the overall accuracy is lower than 85%.

2. All of the incorrect trials will be excluded.

3. Translate the unit of reaction time from seconds to milliseconds.

4. The reaction time that is outside the range of two standard deviations for the individual will be excluded.

5. Calculate the mean for each compatibility condition.

6. Compare the average reaction time between compatibility and incompatibility.

7. Plot the chart for the comparison. (x: condition; y: reaction time; error bar: SEM)





*Note.* About where and how to analyze these code...

Please first enter the IPython interactive shell: Type ipython in your PowerShell and press Enter.
(If it is not installed, run pip install ipython first.)

Type the Magic Command %cpaste and press Enter,

Paste the code after you see a message: "Pasting code; enter '--' alone on the line to stop or use Ctrl-D."

After pasting, type -- on a new line and press Enter, or press Ctrl-D.

IPython will then read and execute the entire block at once, ensuring that the indentation remains intact.