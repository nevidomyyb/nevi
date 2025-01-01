import streamlit as st
from partials.base_page import BasePage

class WPPChatAnalysis(BasePage):
    
    def __init__(self, ):
        self.page_title = "Group chat data analysis"
        st.session_state['page'] = 'wpp chat analysis'
        super().__init__(page_title=self.page_title)
        
    def draw(self):
        st.markdown("###")
        
        
page = WPPChatAnalysis()
page.mount()
    