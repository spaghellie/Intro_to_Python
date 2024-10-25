# Alright, so we've looked at Lists and Arrays... yet another useful strcuture is the oh-so-handy *Dictionary* !

# Dictionaries are a much more intuitive and convenient way to map list elements to list elements
# (rather than extracting elements from multiple different lists using their respective indices and whatnot... that's just a hassle!)

# Dictionaries are made up of key:value pairs.
# (You can think of it either like, "matching a value to the appropriate key"
# OR "assigning a key to its respective value.")
# Noooooote that any one key is always going to be ~unique~ ...
# and that keys are immutable objects
# ("immutable" = the content of the object cannot be changed after they're created) --> a list **cannot** be used as a key!

###############

# **Previously**, the method of finding corresponding values within two lists was inefficient...
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

###############

# **HOWEVER**, a far more convenient approach is utilizing a dictionary...
# Definition of europe dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

###############

# Adding to dictionaries (or changing values in dictionaries)...
  # Original definition of world dictionary
world = {'afghanistan':30.55, "albania":2.77, "algeria":39.21}

  # Printing out world
print(world)

  # Printing out a specific entry, given its key
world['albania']

  # Add the principality of Sealand
world['sealand'] = 0.000027
print(world)
# NOTE that this same syntax would be used to update key:value pairs

# hey let's just make sure that Sealand is actually in the dictionary:
'sealand' in world

###############

  # Removing from dictionaries...
del(world['sealand'])

print(world)

###############

# Dictionary values can be more dictionaries!

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
europe['france']['capital']

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
