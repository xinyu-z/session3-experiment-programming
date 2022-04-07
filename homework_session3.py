# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

## Exercise B
# 1. Load the lexical decision stimuli file 
# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
# 4. Play the sounds one-by-one, making sure there is some time between them

## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!
