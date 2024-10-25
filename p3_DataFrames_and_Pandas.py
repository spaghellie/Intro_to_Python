# Lists, Arrays, and Dictionaries are all fine and dandy (they each serve they're own purpose; have a time and a place to use them)...
# But what about (very likely, real-world) situations in which we want to handle data structures containing different /types/ of variables?
# --> ENTER: the Pandas package :)

# *** Pandas DataFrame: A high-level data structure for storing tabular data, where rows represent observations and columns represent variables. ***

# Here are some examples of the power of DataFrames and Pandas as a whole...

###############

# Always need to import the pandas pkg!
import pandas as pd

###############

# ### Creating a DataFrame ('DF') from a dictionary:
dict = {
    'country':['Brazil','Russia','India','China','South Africa'],
    'capital':['Brasilia','Moscow','New Delhi','Beijing','Pretoria'],
    'area':[8.516, 17.10, 3.286, 9.597, 1.221],
    'population':[200.4, 143.5, 1252, 1357, 52.98]
}
    # NOTE that the *Keys* are the column labels of our 'table'
    # ... and that the *Values* are the data, column by column

# Use the DataFrame command (as a pandas extension) on the dictionary
brics = pd.DataFrame(dict)

print(brics)

print()
# NOTICE that that^ just automatically assigned numeric index values to each row of the table...
# We can change the names of all the indices, though:
brics.index = ['BR','RU','IN','CH','SA']
print(brics)

###############

# ### Creating DFs from CSV files
# The commands are going to look something like this:
      # < brics = pd.read_csv("path/to/brics.csv", index_col=0) >
# NOTE that you HAVE to have quotes around the file within this command!
# Also note that the index_col part will help Python to assign the first elements/keys as the indices

###############

# ### Example (another one):

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country':names,
    'drives_right':dr,
    'cars_per_cap':cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

print()

# NOTICE that that prints out a table/DataFrame that automatically assigned indices 0 thru 6.
# Let's say that we want to relabel the index rows to be abbreviations of the country names...

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

###############

# ### Indexing & selecting data from DFs

# ### Column access:
    # Say that we have some DF, < brics > , from a CSV file.
    # The command, < brics['country'] > would create a /series/ out of the 'country' column of the original DF, brics.
  # However... the command, < brics[['country']] > would would more appropriately create a sub-DF out of the original instead.
  # Note that < brics[['country', 'capital']] > would create a sub-DF with 2 columns now.

# ### Row access:
    # (Hey, remember that slicing in python is only inclusive of the first value, exclusive of the 2nd)
    # A command like `brics[1:4]` would create a sub-DF that has all columns of the original DF, but only rows from indices 1, 2, and 3.

# Unfortunately, this Square-Brackets-Approach has limited functionality...

###############

# ENTER: loc (label-based) & iloc (integer-position-based) functions

# ### Remember, Square-Brackets:
    # Single [] returns a Pandas series
    # Double [[]] return a Pandas DataFrame
cars['country'] # Series
cars[['country']] # DataFrame

# ### loc and iloc
    # loc is label-based
    # iloc is index-based
cars.loc['RU'] # Row for Russia using label
cars.iloc[4] # Row for Russia using index

# Using that^ to combine rows and columns
cars.loc[['RU','MOR'], ['country','drives_right']]
