import streamlit as st


def app():
    st.set_page_config(page_title="Fishcatch", page_icon="🐟")

    col1, col2 = st.columns(2)

    with col1:
        st.title('Fishcatch: Predicting the width of a fish based on its features.')

    with col2:
        st.image('https://imgur.com/23DiEOf.png', width=140)

    st.markdown(
        '''
        ## A simple app to predict the width of a fish based on its features.
        by [joaoalexarruda](https://github.com/joaoalexarruda)
        '''
    )

    st.divider()


app()
