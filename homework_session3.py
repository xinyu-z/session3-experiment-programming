# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
import pandas as pd
import os
import psychopy
from psychopy import visual, core, event, clock, sound
# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
stimuli = pd.read_csv("/Users/mymacbookair/Documents/IMPRSPythonCourse/session3-experiment-programming/picture_verification_stimuli.csv")
# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
#create window:
window = visual.Window(size=(400, 400))
message = visual.TextStim(window)
grating = visual.GratingStim(window, tex='sin', mask='gauss', sf=10, name='gabor')

for item in stimuli.loc[:,"item"]:
    print(item)

# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
for item in stimuli.loc[:,"item"]:
    message.text = item  
    message.draw()
    window.flip()
    core.wait(1.0)

# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

window = visual.Window()
clock = core.Clock()
folderPath = "/Users/mymacbookair/Documents/IMPRSPythonCourse/session3-experiment-programming/images"
stimuli = os.path.join(folderPath, 'image_file')
images = []

for item_path in stimuli ['image_file']:
    stimuli = os.path.join(folderPath, item_path)
    image_stim = visual.ImageStim(window, image=item_path)
    image.append(image_stim)

images = np.random.permutation(images)
results = []
for image in images[:4]:
    image.draw()
    window.flip()
    clock.reset()
    start_time = clock.getTime()
    keys = event.waitKeys(maxWait=5, keyList=['z', 'm'], timeStamped = clock, ckearEvents = True)
    if keys is not None:
        key, end_time = keys[0]
    else:
        key = None
        endtime = clock.getTime()

results.append({
    'start_time': start_time,
    'end_time': end_time,
    'key': key
})
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to.csv('demo.output.csv')
print(results)



## Exercise B
# 1. Load the lexical decision stimuli file 
stimuli = pd.read_csv("/Users/mymacbookair/Documents/IMPRSPythonCourse/session3-experiment-programming/lexical_decision_stimuli.csv")

# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
mask = stimuli["freq_category"] == "HF"
HF = stimuli[mask]
# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
for sound_name in range (2-49) in HF:
#(because"for sound_name in HF" returned "could not find a sound file named sounds/HF/stim_id.wav"
#sound_name = stimuli["word"].iloc[i]
    relPath = f'sounds/HF/{sound_name}.wav'
# 4. Play the sounds one-by-one, making sure there is some time between them
    audio = sound.Sound(relPath)
    window.flip()
    audio.play()
#this returned " 'bool' object no iterable"
## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!
