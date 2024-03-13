import matplotlib.pyplot as plt


def plot_regression(y_test, y_pred, title: str, regression_type: str = 'Linear'):
    """Plots the actual width vs predicted width using a scatter plot.

    Args:
        y_test (array): y_test got from train_test_split.
        y_pred (array): y_pred got from the model.
        title (str): Title of the plot.
        regression_type (str, optional): Type of regression. Defaults to 'Linear'.
    """

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(y_test, y_pred, color='blue', label='Predicted Width')
    ax.plot(y_test, y_test, color='red', label='Actual Width')
    ax.set_xlabel('Actual Width')
    ax.set_ylabel('Predicted Width')
    ax.set_title(f'{regression_type} Regression: {title}')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    plt.show()
