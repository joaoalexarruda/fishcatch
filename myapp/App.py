import streamlit as st


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

    st.divider()


app()
