import os
import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('Her skriver AI-robotten dit jobopslag')

st.text('Denne model kan skrive jobannoncer på kommando.')
prompt_text0 = st.text_input(label="Hvad hedder stillingen? Eksempel: Redaktør til internt nyhedsbrev", value="Skriv stillingsbetegnelse her")
prompt_text1 = st.text_input(label="Hvilket firma ansætter? Eksempel: DTU", value="Skriv navnet på firmaet her")
prompt_text2 = st.text_input(label="Hvad er de vigtigste arbejdsopgaver og kompetencer, som stillingen kræver? Skriv gerne hele sætninger her, og gerne flere sætninger, så performer modellen bedre. Eksempel: DTU er i gang med at styrke sin organisatoriske kommunikation, og vi søger derfor en redaktør til at udvikle et nyhedsbrev til DTU’s interne målgrupper", value="Skriv et par sætninger om arbejdsopgaver og ansøgers forventede kompetencer her")
response = openai.Completion.create(model="curie:ft-qubit-2022-05-18-13-20-56", prompt=prompt_text0+", "+prompt_text1+". "+prompt_text2, temperature=0.7,
max_tokens=800,
top_p=1,
frequency_penalty=0,
presence_penalty=0)
st.text('Husk at trykke RETURN, når du har skrevet dit input')
st.text('Annonce:')
st.markdown(response["choices"][0]["text"])



