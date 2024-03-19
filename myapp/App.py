import streamlit as st
import joblib
import pandas as pd

def app():
    st.set_page_config(page_title="Fishcatch", page_icon="🐟")

    col1, col2 = st.columns(2)

    with col1:
        st.title('Fishcatch')

    with col2:
        st.markdown(
            """
            <div style="text-align: center">
                <img src="https://imgur.com/h7ppyOC.png" width="140">
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.write('Predicting the width of a fish based on its features.')

    st.markdown(
        '''
        by [joaoalexarruda](https://github.com/joaoalexarruda)
        '''
    )
    
    
    loaded_model = joblib.load('linear_regression_model.pkl')

    st.divider()

    st.write('### Make a prediction:')

    df = pd.read_csv('../datasets/fishcatch/fishcatch.csv')

    length1_min = df['Length1'].min()
    length1_max = df['Length1'].max()
    length2_min = df['Length2'].min()
    length2_max = df['Length2'].max()
    length3_min = df['Length3'].min()
    length3_max = df['Length3'].max()
    height_min = df['Height'].min()
    height_max = df['Height'].max()

    length1 = st.number_input(
        'Length1', min_value=length1_min, max_value=length1_max, value=length1_min)
    length2 = st.number_input(
        'Length2', min_value=length2_min, max_value=length2_max, value=length2_min)
    length3 = st.number_input(
        'Length3', min_value=length3_min, max_value=length3_max, value=length3_min)
    height = st.number_input(
        'Height', min_value=height_min, max_value=height_max, value=height_min)

    if st.button('Predict'):
        prediction = loaded_model.predict(
            [[length1, length2, length3, height]])
        st.write(f'Predicted Width: {prediction[0]:.2f}')


app()
