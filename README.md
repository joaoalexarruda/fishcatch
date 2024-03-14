# Fishcatch

by [joaoalexarruda](https://github.com/joaoalexarruda)

This repository contains the 'fishcatch' dataset. The dataset is part of an assignment for the post graduation course ['Data Science and Digital Transformation'](https://www.ipportalegre.pt/pt/oferta-formativa/pos-graduacao-data-science-and-digital-transformation) at the Instituto Politécnico de Portalegre (IPP).

The goal is to apply machine learning techniques to the dataset and to evaluate the results. In this case, regression techniques such as linear and polynomial regression will be used to predict the width of the fish based on the other variables.

## Notebooks

The notebooks are organized in the following way:

- [n0](./notebooks/n0_exploratory_analysis.ipynb): Exploratory Data Analysis
- [n1](./notebooks/n1_linear_regression_1.ipynb): Linear Regression with all numeric variables
- [n2](./notebooks/n2_linear_regression_2.ipynb): Linear Regression without non-linear variables
- [n3](./notebooks/n3_polynomial_regression.ipynb): Polynomial Regression
- [n4](./notebooks/n4_linear_and_polynomial_regression.ipynb): Linear and Polynomial Regression
- [n5](./notebooks/n5_comparison_conclusion.ipynb): Conclusion

## Description of the dataset

159 fishes of 7 species are caught and measured. Altogether there are 7 variables.  All the fishes are caught from the same lake (Laengelmavesi) near Tampere in Finland.

More information about the dataset can be found in the [original source](https://jse.amstat.org/datasets/fishcatch.txt).

On the original dataset, there was a variable called 'Sex' which was removed from this dataset.

## Assignment requirements

The assignment requires the tasks described in the [pdf](./task-description/ADAA_23.24_TrabalhoPrático.pdf) file.

## Dependencies

Run the following command on a python environment to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Streamlit App

There is a simple web app that uses the trained model to predict the width of a fish based on the other variables. It's still under development and can be found in the [myapp](./myapp) folder.
