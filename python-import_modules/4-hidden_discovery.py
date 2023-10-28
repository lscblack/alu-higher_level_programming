#!/usr/bin/python3

import sys

# Prevent the program from being executed when imported
if __name__ != "__main__":
    sys.exit(0)

# Load the compiled module
try:
    import imp
    hidden_4 = imp.load_source("hidden_4", "hidden_4.pyc")
except ImportError:
    print("Failed to load hidden_4.pyc")
    sys.exit(1)

# Get all the names defined in the module
names = dir(hidden_4)

# Filter out the names starting with __
filtered_names = [name for name in names if not name.startswith("__")]

# Sort the filtered names in alphabetical order
sorted_names = sorted(filtered_names)

# Print each name on a new line
for name in sorted_names:
    print(name)
