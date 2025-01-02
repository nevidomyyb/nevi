import streamlit as st
from partials.base_page import BasePage

class WPPChatAnalysis(BasePage):
    
    def __init__(self, ):
        self.page_title = "WhatsApp chat analysis"
        st.session_state['page'] = 'wpp chat analysis'
        super().__init__(page_title=self.page_title)
        
    def draw(self):
        st.markdown("###")
        st.markdown("###### How it started, what was my objective ?")
        
        
        
page = WPPChatAnalysis()
page.mount()
    