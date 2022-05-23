import os
import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('GPT-3')

st.text('Denne model kan skrive jobannoncer på kommando.')
prompt_text0 = st.text_input(label="Hvad hedder stillingen? /n Eksempel: Redaktør til internt nyhedsbrev", value="Input")
prompt_text1 = st.text_input(label="Hvilket firma ansætter? Eksempel: DTU", value="Input")
prompt_text2 = st.text_input(label="Hvad er de vigtigste arbejdsopgaver og kompetencer, som stillingen kræver? Skriv gerne hele sætninger her, og gerne flere sætninger, så performer modellen bedre. Eksempel: DTU er i gang med at styrke sin organisatoriske kommunikation, og vi søger derfor en redaktør til at udvikle et nyhedsbrev til DTU’s interne målgrupper", value="Input")
response = openai.Completion.create(model="curie:ft-qubit-2022-05-18-13-20-56", prompt=prompt_text0+", "+prompt_text1+". "+prompt_text2, temperature=0.7,
max_tokens=400,
top_p=1,
frequency_penalty=0,
presence_penalty=0)
st.text('Annonce:')
st.markdown(response["choices"][0]["text"])



