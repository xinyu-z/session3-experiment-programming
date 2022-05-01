#Lexical decision task
##make a demo that presents a couple of stimuli regardless of the condition
import pandas as pd
from psychopy import core, sound, visual, event
window = visual.Window(size=(400, 400))
lexical_decision_stimuli = pd.read_csv('lexical_decision_stimuli.csv')
hf_words = lexical_decision_stimuli[lexical_decision_stimuli['freq_category'] == 'HF']

for word in hf_words['word']:
    text_stim = visual.TextStim(window)
    text_stim.text = "Is this a real word? Press 'r' for 'real word', 'n' for 'non word'"
    text_stim.draw()
    sound_stim = sound.Sound(f'sounds/HF/{word}.wav')
    sound_stim.play()
    window.flip()
    core.wait(0.5)

#collect keyboard input
#collect RT? <- check instruction