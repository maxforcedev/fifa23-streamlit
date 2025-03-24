import streamlit as st

df_data = st.session_state["key"] 


st.set_page_config(
    page_title="Players",
    page_icon="👦",
    layout="wide"
)

clubs = df_data["Club"].unique()
clubs = st.sidebar.selectbox("Clube", clubs)

df_players = df_data[(df_data["Club"] == clubs)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[(df_data["Name"] == player)].iloc[0]

player_photo = st.image(player_stats["Photo"],width=80) 
player_name = st.title(player_stats["Name"])
player_club = st.markdown("Clube: " + player_stats["Club"])
player_position = st.markdown("Posição: " +  player_stats["Position"])

col1, col2, col3 = st.columns(3)
player_age = col1.markdown("Idade: " +  str(player_stats["Age"]))
player_height = col2.markdown("Altura: "+ str(player_stats["Height(cm.)"] / 100))
player_weight = col3.markdown("Peso: " +  str(player_stats["Weight(lbs.)"]))
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")