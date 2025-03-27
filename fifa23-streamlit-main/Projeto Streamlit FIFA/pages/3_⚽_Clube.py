import streamlit as st

df_data = st.session_state["key"] 

st.set_page_config(
    page_title="Clube",
    page_icon="⚽",
    layout="wide"
)

clubs = df_data["Club"].unique()
clubs = st.sidebar.selectbox("Clube", clubs)
club = df_data[(df_data["Club"] == clubs)].set_index("Name")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.image(club.iloc[0]["Club Logo"], width=80)

st.markdown(f"## {clubs}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.divider()
st.dataframe(club[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=club["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })