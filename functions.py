import pandas as pd

def make_bipolar(cell):
    if cell == 'Division 1':
        return 1
    return -1

def prepare_data(df, div):
    df_mean = df.groupby('team_name').mean(numeric_only=True)
    df_mean.columns = [col + ' mean' for col in df_mean.columns]
    df_stdev = df.groupby('team_name').std(numeric_only=True)
    df_stdev.columns = [col + ' stdev' for col in df_stdev.columns]
    new_df = df_mean.join(df_stdev)
    new_df = new_df.join(div['level'])
    new_df['level'] = new_df['level'].apply(make_bipolar)
    return new_df

def get_results(prediction, actual):
    data = {
        'Prediction': prediction,
        'Actual': actual
    }
    results = pd.DataFrame(data)
    num_correct = len(results[results['Prediction'] == results['Actual']])
    total = len(results)
    accuracy = round(num_correct/total * 100, 2)
    print(f"Accuracy: {accuracy}%")
    return results
