import numpy as np

passage = " simulate cell 1 and cell 2 such that they are \
nearby to each other wish a distance of 2 mm"

unique_token = set()

action_sequence = {}

tokens = passage.split()

for token in tokens:
    unique_token.add(token)
    