import streamlit as st
from partials.custom_bottom import Bottom
from partials.custom_sidebar import Sidebar
from streamlit_extras.switch_page_button import switch_page
    
class BasePage(Bottom, Sidebar):
    
    def __init__(self, page_title: str, initial_sidebar_state: str= 'collapsed'):
        st.set_page_config(
            page_title=page_title,
            page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScFu4Gw8_z-p4d7njXvA8cT2KM2Qq7D7LDOZMjA13-sEFphgVR-A0tiG4gasGmGVStZck&usqp=CAU",
            layout='wide',
            initial_sidebar_state=initial_sidebar_state,
        )
        st.markdown("""
            <style>

            .block-container
            {
                padding-top: 1%;
                padding-bottom: 0rem;
                margin-top: 1rem;
            }

            </style>
            """, unsafe_allow_html=True)
    
    def draw(self, ):
        ...
    
    def mount(self, ):
        self.draw_sidebar()
        if st.session_state['page'] != "main":
            if st.button(label="", icon=":material/home:", type='tertiary'):
                switch_page('main')
            st.header(self.page_title)
        else:
            st.header(self.page_title)
       
        self.draw()
        self.draw_bottom()
        
        
    