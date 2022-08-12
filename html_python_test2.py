# import
import streamlit as st
# APP
# set title and subtitle
st.title("SummarizeLink")
st.markdown("Paste any article link below and click on the 'Summarize' button.")
st.markdown("*Note:* We truncate the text incase the article is lengthy! 🖖")
# create the input text box and setting panel
link = st.text_area('Paste your link here...', "https://towardsdatascience.com/a-guide-to-the-knowledge-graphs-bfb5c40272f1", height=50)
button = st.button("Summarize")
min_length = st.sidebar.slider('Min summary length', min_value=10, max_value=100, value=50, step=10)
max_length = st.sidebar.slider('Max summary length', min_value=30, max_value=700, value=100, step=10)
num_beams = st.sidebar.slider('Beam length', min_value=1, max_value=10, value=5, step=1)