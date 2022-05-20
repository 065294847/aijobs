import os
import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('GPT-3')

st.text('Denne model kan skrive jobannoncer på kommando.')
prompt_text = st.text_input(label="Skriv din prompt her, af formen Stilling, Arbejdsplads, kort beskrivelse", value="Input")
response = openai.Completion.create(model="curie:ft-qubit-2022-05-18-13-20-56", prompt=prompt_text, max_tokens=200)
#st.text('Remaining phrase:')
#st.text(response["choices"][0]["text"])



