import pandas as pd

def calculate_consistency(file_path):
    df = pd.read_excel(file_path)
    
    relevant_columns = ['Distance X (in)', 'Distance Y (in)', 'Shooter Angle', 'Shooter Voltage', 'Shooter Current']
    
    df['Consistency'] = df[relevant_columns].std(axis=1)
    
    most_consistent_row = df.loc[df['Consistency'].idxmin()]
    
    print(most_consistent_row)

# Replace this with your excel file
calculate_consistency('/Users/trent/Documents/Tmacs Shooter Test.xlsx')
