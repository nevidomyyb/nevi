from partials.custom_sidebar import Sidebar
from streamlit_extras.grid import grid
from streamlit_extras.switch_page_button import switch_page
from partials.base_page import BasePage
import streamlit as st
    
class Main(BasePage):
    
    def __init__(self, page_title):
        self.page_title = page_title
        self.initial_sidebar_state = 'expanded'
        self.pages = [
            {
                "title": "Group Chat Data Analysis", "image": "https://placehold.co/300x200", "description": "Lorem ipsum, lorem ipsum, lorem ipsum, lorem ipsum, lorem ipsum.", "page": "wpp chat analysis"
            },
        ]
        st.session_state['page'] = 'main'
        super().__init__(page_title, initial_sidebar_state=self.initial_sidebar_state)
    
    def draw(self, ):
        st.markdown("**I did/am doing several things. <br>And in the meantime I update the blog**", unsafe_allow_html=True)
        self.draw_blogs_grid()
        
    def draw_blogs_grid(self, ):
        _grid = grid([0.25, 0.25, 0.25, 0.25])
        for i in self.pages:
            with _grid.container():
                st.image(i['image'])
                st.text(i['title'])
                st.text(i['description'])
                if st.button("Read"):
                    switch_page(i['page'])
        

main = Main("Nevidomyy's blog")
main.mount()