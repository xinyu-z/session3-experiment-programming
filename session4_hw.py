#Lexical decision task
##make a demo that presents a couple of stimuli regardless of the condition
import pandas as pd
import numpy as np
from psychopy import core, sound, visual, event
window = visual.Window(size=(400, 400))
lexical_decision_stimuli = pd.read_csv('lexical_decision_stimuli.csv')
hf_words = lexical_decision_stimuli[lexical_decision_stimuli['freq_category'] == 'HF']

clock = core.Clock()
hwResults = []
for word in hf_words['word']:
    text_stim = visual.TextStim(window)
    text_stim.text = "Is this a real word?  Press 'r' for 'real word', 'n' for 'non-word'"
    text_stim.draw()
    sound_stim = sound.Sound(f'sounds/HF/{word}.wav')
    #suond_stim = np.random.permutation(sound_stim)
    sound_stim.play()
    window.flip()
    core.wait(1) #so that the key press and the presentation of the next word is not simultaneous, which can get confusing
    clock.reset()
    start_time = clock.getTime()
    keys = event.waitKeys(maxWait = 8, keyList = ['r', 'n'], timeStamped = clock, clearEvents = True)
    if keys is not None:
        key, end_time = keys[0]
    else:
        key = None
        end_time = clock.getTime()
    
    hwResults.append({
        'start_time': start_time,
        'end_time': end_time,
        'key': key
    })
   
   
results = pd.DataFrame(hwResults)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv('hw_output.csv')
