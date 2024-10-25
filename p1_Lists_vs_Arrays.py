# In Python, you deal with all kinds of different data structures.
# Two data structures that I, personally, get mixed up all the time are Lists and (n-Dimensional) Arrays.

#######################

# Let's first conquer ***LISTS*** :
  # Say we create some list, named "areas," which represents different areas (sq.ft.) of rooms in my house.
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

  # Since we're being real basic rn (and we can literally /see/ the list), let's just say we want to print the area of whichever room is third on the list.
print(areas.index(2))

  # Oh hey yeah now let's see how many rooms in my house are 10.75 sq.ft.
print(areas.count(10.75))

  # I won the lottery and I want to make some additions to my property (add a poolhouse and a garage)
areas.append(24.5)
areas.append(15.45)

  # Super duper cool, let's check to make sure that that actually worked...
print(areas)

  # Oooh nice, now let's reverse the order of the lists just for giggles (then check it)
areas.reverse()
print(areas)
  # Notice how using the <.reverse> method on the areas list permanently changed it!

# I'm going to show 2 more list example to show how lists can have different variable types in them, and the "arithmetic" that we perform on them is not quite as someone might expect
  # List of lists:
house_1 = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
  # Use the appropriate subset of the house_1 "list of lists" in order to print out the float, 9.50
house_1[4][1]

  # Now for a single list, but with multiple different variable types within it:
house_2 = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
    # Print out second element from house_2
print(house_2[1])
    # Print out last element from house_2
print(house_2[-1])
    # Print out the area of the living room
print(house_2[5])

  # Add poolhouse data to house_2. You have to make a new list in order to make this change 'stick'
house_3 = house_2 + ["poolhouse", 24.5]
  # Add yet another room: the garage. You have to make a new list (NOTE that we're appending to the new list to make a newer list) in order to make this change 'stick'
house_4 = house_3 + ["garage", 15.45]
  # Check to see what I'm talking about...
print(house_2)
print(house_3)
print(house_4)

# In order to delete elements from a list, use the <del> command
del house_4[-4:-2]

# If you want to make a whole new copy of a list, make sure to use the <list()> command
    # Create list areas
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Change this command
    areas_copy = list(areas)

    # Change areas_copy
    areas_copy[0] = 5.0

    # Print areas
    print(areas)
    print(areas_copy)

#######################

# Quick pause to talk about **SLICING** 
  # Note that it's [inclusive : exclusive]

#######################

# Now we can talk about NumPy ***ARRAYS*** :
  # Note that we do need to import the numpy pkg (btw there are soooo many packages and sub-packages that we can load onto a Python shell)
import numpy as np

  # Let's make an array which denotes the heights (cm) of some baseball players on The Team this year (idk)
np_baseball = np.array([180, 215, 210, 210, 188, 176, 209, 200])

  # The fantastic thing about NumPy arrays (unlike plain ol' Python Lists) is that you can perform arithmetical operations directly onto the elements (so long as it is appropriate/applicable).
np.array([True, 1, 2]) + np.array([3, 4, False])
    # is the same as writing...
np.array([4, 3, 0]) + np.array([0, 2, 2])


  # Let's make a 2-D NumPy array of the baseball players' heights and weights
np_baseball_2D = = np.array([[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]])

    # NOTE that the shape notation ALWAYS goes: [row(s), column(s)]

# One more thing about the arithmetic operating on the numpy arrays...
  # Create numpy array: conversion. Say that the np_baseball_2D were actually in 'inches' and 'pounds' respectively. The conversion array is going to convert units of height and weight to metric
conversion = np.array([0.0254,0.453592)
  # Print out product of np_baseball_2D and conversion
print(np_baseball_2D * conversion)

  # Create np_height_in from np_baseball_2D
np_height_in = np_baseball_2D[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


# #### okay, just going to steal something straight from the DC lesson... just copy and paste the exercise (task objective AND correct code to answer)
      # Because the mean and median are so far apart, you decide to complain to the MLB. 
      # They find the error and send the corrected data over to you. 
      # It's again available as a 2D NumPy array np_baseball, with three columns.

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
