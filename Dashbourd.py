
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import funcs as func

def main():

    file_path = r"C:\rayanpoyesh_project\zamani\LLMES\table.xlsx"

    df_models = pd.read_excel(file_path, engine='openpyxl')
    st.markdown('llm evaluation ')
    
    if 'Draw' not in st.session_state:
        st.session_state.Draw = False

    placeholder = st.empty()

    fig_default = func.create_default_radar_chart()
    placeholder.plotly_chart(fig_default, use_container_width=True)

    edited_df, selected_features = func.display_features_and_update_data(df_models)
    func.update_draw(edited_df)

    try:
        if st.session_state.Draw:
            fig_updated = func.create_radar_chart(edited_df, selected_features)
        else:
            fig_updated = func.create_default_radar_chart()

        placeholder.plotly_chart(fig_updated, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")
