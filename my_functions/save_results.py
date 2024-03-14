import pandas as pd
import os


def save_results(mse, mae, r2, rmse, train_r2, model_name):
    # Check if the file exists
    file_exists = os.path.isfile('results.csv')

    # Create a DataFrame
    results = pd.DataFrame({'Model': model_name,
                            'Mean Squared Error': mse,
                            'Mean Absolute Error': mae,
                            'R²': r2,
                            'Root Mean Squared Error': rmse,
                            'Train R²': train_r2}, index=[0])

    # If the file exists, append the results. Otherwise, write the results and include the header.
    if file_exists:
        results.to_csv('results.csv', mode='a', header=False, index=False)
    else:
        results.to_csv('results.csv', mode='w', header=True, index=False)

    print('Results saved successfully to "results.csv".')
    print('Remember to drop duplicates if you run the same model multiple times.')
