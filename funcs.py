import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def exel2(df_models):
    name_list =[]
    for _,row in df_models.iterrows() :
        name_list.append(row.to_dict())
    
    
    for s in range(len(name_list)) :
    
        del name_list[s]['selected']
        del name_list[s]['Model']

    print(name_list)
    
    return name_list





# تابع برای ایجاد نمودار رادار پیش‌فرض
def create_default_radar_chart():
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[0],
        theta=[''],
        fill='toself',
        line=dict(color='blue'),
        name='Default Model'
    ))

    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        polar=dict(
            radialaxis=dict(visible=True)
        ),
        
        margin=dict(l=10, r=10, t=10, b=10),  # تنظیم حاشیه‌ها
        autosize=True,
    )




    return fig





def create_radar_chart(data_frame, features):
    selected_rows = data_frame[data_frame['selected']]

    fig = go.Figure()
    if not selected_rows.empty:
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'pink', 'cyan', 'magenta']

        for idx, row in selected_rows.iterrows():
            model = row['Model']
            data_for_chart = {feature: row.get(feature, 0) for feature in features}

            df_plot = pd.DataFrame(dict(
                r=[data_for_chart.get(f, 0) for f in features],
                theta=features
            ))

            fig.add_trace(go.Scatterpolar(
                r=df_plot['r'],
                theta=df_plot['theta'],
                fill='toself',
                marker=dict(color='red', size=8),
                line=dict(color=colors[idx % len(colors)]),
                name=model
            ))
    else:
        fig = create_default_radar_chart()

    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        polar=dict(
            radialaxis=dict(visible=True)
        ),
        showlegend=True,
        margin=dict(l=10, r=10, t=10, b=10),  # تنظیم حاشیه‌ها
        autosize=True

        



    )








    return fig





def display_features_and_update_data(df_models):

    # نمایش DataFrame برای انتخاب ویژگی‌ها
    st.write("Select Features:")
    features_df = pd.DataFrame(exel2(df_models))
    features = features_df.columns.tolist()
    checkbox_df = pd.DataFrame(columns=features)

    checkbox_df.loc[0] = [False] * len(features)
    
    edited_checkbox_df = st.data_editor(checkbox_df, use_container_width=True)

    # به‌روز رسانی ویژگی‌های انتخاب‌شده
    selected_features = [features[i] for i in range(len(features)) if edited_checkbox_df.iloc[0, i]]

    # نمایش DataFrame برای انتخاب مدل
    st.write("Select Models:")
    model_selection = st.data_editor(df_models, use_container_width=True)
    
    # اضافه کردن ستون 'selected' به DataFrame مدل‌ها
    if 'selected' not in df_models.columns:
        df_models['selected'] = False

    # به روز رسانی وضعیت انتخاب بر اساس مدل‌های انتخاب‌شده
    selected_models = model_selection[model_selection['selected']]
    
    # فیلتر کردن مدل‌های انتخاب‌شده
    if not selected_models.empty:
        df_models_selected = df_models[df_models['Model'].isin(selected_models['Model'])]
        df_models_selected['selected'] = True
    else:
        df_models_selected = df_models.copy()
        df_models_selected['selected'] = False
    
    return df_models_selected, selected_features





def update_draw(df):
    st.session_state.Draw = df['selected'].any()




def create_radar_chart2(data_frame, features):
    selected_rows = data_frame[data_frame['selected']]

    fig = go.Figure()
    if not selected_rows.empty:
        colors = colors = ['rgba(0, 0, 255, 0.5)', 'rgba(255, 0, 0, 0.5)', 'rgba(0, 255, 0, 0.5)',
                  'rgba(255, 165, 0, 0.5)', 'rgba(128, 0, 128, 0.5)', 'rgba(255, 192, 203, 0.5)',
                  'rgba(0, 255, 255, 0.5)', 'rgba(255, 0, 255, 0.5)']


        for idx, row in selected_rows.iterrows():
            model = row['Model']
            data_for_chart = {feature: row.get(feature, 0) for feature in features}

            df_plot = pd.DataFrame(dict(
                r=[data_for_chart.get(f, 0) for f in features],
                theta=features
            ))

            fig.add_trace(go.Scatterpolar(
                r=df_plot['r'],
                theta=df_plot['theta'],
                fill='toself',
                marker=dict(color='red', size=8),
                line=dict(color=colors[idx % len(colors)]),  # تنظیم شفافیت خطوط
                name=model
            ))
    else:
        fig = create_default_radar_chart()

    fig.update_layout(
        paper_bgcolor='lightgrey',
        plot_bgcolor='white',
        polar=dict(
            radialaxis=dict(visible=True)
        ),
        showlegend=True
    )
    return fig
