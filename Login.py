import streamlit as st
import os
import pandas as pd

import random
import streamlit as st
import time
i=0
# تعریف CSS برای بزرگ‌تر کردن دکمه‌ها
button_css = """
<style>

    textarea {
        font-size: 1.5rem !important;
    }
    input {
        font-size: 1.5rem !important;

    }
    .stButton button {
        font-size: 20px;
        padding: 20px 200px;
        margin-bottom: 1px;  /* فاصله بین دکمه‌ها */
        margin-left: 100px;   /* مایل کردن به سمت راست */
    }
    .stButton:first-child button {
        margin-top: 50px;  /* فاصله قبل از اولین دکمه */
    }
</style>
"""



button_css2 = """
<style>

    textarea {
        font-size: 1.5rem !important;
    }
    input {
        font-size: 1.5rem !important;

    }
    .stButton button {
        font-size: 20px;
        padding: 20px 100px;
        margin-bottom: 5px;  /* فاصله بین دکمه‌ها */
        margin-left: 1px;   /* مایل کردن به سمت راست */
    }

</style>
"""








def reseted():
    for key in st.session_state.keys():
        
        del st.session_state[key]
    st.session_state.checkbox_status =False
    # st.session_state.disabled = True
    st.session_state['ok'] = True    
    st.experimental_rerun()
    





if 'checkbox_status' not in st.session_state:
    st.session_state.checkbox_status = True
    # st.session_state.disabled = False
    st.session_state['ok'] = False
# main_box=st.checkbox('Start' ,key ='Start' ,value=st.session_state.checkbox_status ,disabled=st.session_state.disabled)      
if st.session_state.checkbox_status:
    st.session_state['main'] = True

else :
    st.session_state['main'] = False     



if st.session_state['main'] :
# نمایش CSS در اپلیکیشن
    st.markdown(button_css, unsafe_allow_html=True)

    # cols = st.columns(2)

    # # sine = st.button(" ثبت نام  ", key='Sine')
    # # log = st.button(" ورود ", key='Log')






    # if sine :
    #     st.session_state['Sine Up']=True

    # if 'Sine Up' in st.session_state and st.session_state['Sine Up']:


    #     fullname = st.text_input('fullname : ',key='name',placeholder='نام و نام خانوادگی خود را وارد کنید ')
    #     Email = st.text_input('Email : ',key='Email',placeholder='ایمیل خود را وارد کنید ')
    #     phone = st.text_input('phone : ',key='phone',placeholder='شماره تلفن خود را وارد کیند ')



    #     if st.button('ثبت نام ' , key = 'Submit1') :
                
    #                 if Email and fullname and phone :
                        
                        
                        
    #                     print('ok2')
    #                     # -------------> ثبت در دیتابیس
    #                     st.write(f"شخص به نام ونام خانوادگی {fullname}")
    #                     st.write(f"و ایمیل {Email}")
    #                     st.write(f"و شماره تلفن {phone} ثبت شد ")
    #                     print(f"شخص به نام ونام خانوادگی {fullname}  و ایمیل {Email} و شماره تلفن {phone} ثبت شد ")
    #                     time.sleep(5)
    #                     i+=1
    #                     reseted()


                # except :
                #     st.error('1. از صحت ایمیل خود اطمینان حاصل کنید ')
                #     st.error('2. اتصال خود را چک کنید  ')

        
        # if 'V_code' in st.session_state :
        #             E2 = st.text_input('code : ',key='code',placeholder='کد ارسال شده رو وارد کنید ')
        #             if st.button('تایید ',key = 'Submit2') :
        #                 if E2 ==str(st.session_state['V_code']) :
        #                     st.success('تایید شد  ')
        #                     reseted()
                            # st.session_state.clear()

                            
                            



    st.session_state['Log In']=True

    if 'Log In' in st.session_state and st.session_state['Log In']:
        admin_list = ['admin' , 'ADMIN' , 'Admin']
        Email = st.text_input('Username : ',key='sine_Email',placeholder='ایمیل خود را وارد کنید ')
        password = st.text_input('Password : ',key='pass',placeholder='پسورد خود را وارد کنید')
        if st.button(' ورود ' , key = 'Submit3') :
            if Email in admin_list and password in admin_list :
                st.success("با موفقیت وارد شدید :) ")
                time.sleep(2)
                reseted()

            else :
                st.write('رمز عبور اشتباه است')    
            
            
            

if st.session_state['ok']:
        
        import Dashbourd as Dash

        Dash.main()
        # st.markdown(button_css2, unsafe_allow_html=True)   
        # data = np.random.randn(10, 5)
        # columns = [f'Column {i+1}' for i in range(5)]
        # df = pd.DataFrame(data, columns=columns)
        # # st.session_state['main'] =False 
        # colX = st.columns(3)
        # if colX[0].button('X' ,key='xx'):
        #         st.session_state['xxx'] = True
        #         if st.session_state['xxx']:
                    
        #             data = np.random.randn(10, 5)
        #             columns = [f'Column {i+1}' for i in range(5)]
        #             df = pd.DataFrame(data, columns=columns)

                    
        #             st.table(df) 
                         
        # if  colX[1].button('Y' ,key='yy') :
        #         st.table(df) 
        # if colX[2].button('Z' ,key='zz') :
        #         # st.table(df) 
        
        
        
        #         data = [['Model A', 100, 20],
        #                 ['Model B', 150, 25],
        #                 ['Model C', 200, 30]]
        #         df = pd.DataFrame(data, columns=['models' , 'Average' , 'Score'])
        #         # st.write("جدول با قابلیت اسکرول:")
        #         st.table(df)

        #         import plotly.express as px
        #         import pandas as pd
        #         df = pd.DataFrame(dict(
        #             r=[1, 5, 2, 2, 3],
        #             theta=['processing cost','mechanical properties','chemical stability',
        #                 'thermal stability', 'device integration']))
        #         fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        #         st.plotly_chart(fig, use_container_width=True)
                
                
