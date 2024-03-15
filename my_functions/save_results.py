import pandas as pd
import os


def save_results(mse, mae, r2, rmse, train_r2, model_name, confirm=True):
    """Saves the results of the model to a csv file.

    Args:
        mse (_type_): mean squared error
        mae (_type_): mean absolute error
        r2 (_type_): r-squared
        rmse (_type_): root mean squared error
        train_r2 (_type_): r-squared for the train set
        model_name (_type_): name of the model
    """

    # Check if the file exists
    file_exists = os.path.isfile('results.csv')
    # Create a dataframe with the results
    results = pd.DataFrame({'Model': model_name,
                            'Mean Squared Error': mse,
                            'Mean Absolute Error': mae,
                            'R²': r2,
                            'Root Mean Squared Error': rmse,
                            'Train R²': train_r2}, index=[0])

    # Save the results to a csv file
    if file_exists:
        results.to_csv('results.csv', mode='a', header=False, index=False)
    else:
        results.to_csv('results.csv', mode='w', header=True, index=False)
    results = pd.read_csv('results.csv').drop_duplicates()
    results.to_csv('results.csv', mode='w', header=True, index=False)
    # Confirm the results were saved
    if confirm:
        print('Results saved successfully to "results.csv".')
