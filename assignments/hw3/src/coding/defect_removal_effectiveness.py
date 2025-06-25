# filename: defect_removal_effectiveness.py
import pandas as pd

# Create the matrix using the provided data
data = {
    'R': [52, 0, 0, 0, 0, 0, 0, 0],
    'A': [18, 31, 0, 0, 0, 0, 0, 0],
    'I0': [17, 17, 78, 0, 0, 0, 0, 0],
    'I1': [36, 19, 55, 189, 0, 0, 0, 0],
    'UT': [12, 43, 8, 156, 27, 0, 0, 0],
    'IT': [17, 23, 26, 45, 0, 3, 0, 0],
    'ST': [24, 39, 57, 41, 0, 0, 2, 0],
    'F': [2, 4, 3, 5, 0, 0, 0, 5]
}
matrix = pd.DataFrame(data, index=['R', 'A', 'I0', 'I1', 'UT', 'IT', 'ST', 'F'])

# Calculate the defect removal effectiveness (DRE) for each phase
dre = {}
phases = list(matrix.index)
for i, phase in enumerate(phases):
    detected = matrix.loc[phase, phase]
    escaped = matrix.loc[phase, phases[i + 1:]].sum() if i < len(phases) - 1 else 0
    dre[phase] = detected / (detected + escaped) if (detected + escaped) > 0 else None

# Print the results
print(pd.Series(dre))