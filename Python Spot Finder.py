import pandas as pd

def calculate_consistency(file_path):
    #Pastes Pandas DataFrame
    df = pd.read_csv(file_path)

    #Distance Calculation
    distance_columns = ['Distance X', 'Distance Y']

    #Standard Deviation
    df['Consistency'] = df[distance_columns].std(axis=1)

    #Finds Most Consistent Thing? I think
    most_consistent_row = df.loc[df['Consistency'].idxmin()]

    # Print the results
    print("Most consistent spot to shoot from:")
    print(most_consistent_row)

#Data File Path
calculate_consistency('your_file_path.csv')
