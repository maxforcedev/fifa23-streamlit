import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Players",
    page_icon="🏠",
    layout="wide"
)

if 'key' not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    st.session_state['key'] = df_data

    df_data[df_data["club"]]

# Title
st.title("FIFA OFFICIAL DATASET! ⚽")

# Button
clicked = st.button("Ir aos documentos")
if clicked:    
    webbrowser.open_new("www.google.com")

# Text Home

st.markdown("""  
O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes.""")
st.markdown("""Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.""")

# Sidebar (Menu lateral))
st.sidebar.text("Desenvolvido por Luis Felipe ❤️")

