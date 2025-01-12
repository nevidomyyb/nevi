from streamlit_extras.grid import grid
from streamlit_extras.switch_page_button import switch_page
from partials.base_page import BasePage
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from utils.my_pages import pages
from math import ceil
    
class Main(BasePage):
    
    def __init__(self, page_title):
        self.page_title = page_title
        self.initial_sidebar_state = 'expanded'
        self.pages = pages

        st.session_state['page'] = 'main'
        super().__init__(page_title, initial_sidebar_state=self.initial_sidebar_state)
    
    def draw(self, ):
        st.markdown("**I did/am doing several things. <br>And in the meantime I update the blog**", unsafe_allow_html=True)
        self.draw_blogs_grid()
        
    def draw_blogs_grid(self, ):
        
        n_rows = ceil(len(self.pages) / 4)
        page_idx = 0
        for row in range(n_rows):
            cols = st.columns(4)
            for col in cols:
                if page_idx < len(self.pages):
                    page = self.pages[page_idx]
                    with col.container(height=410):
                        with stylable_container(
                            key=f"abc{page_idx}",
                            css_styles=[
                                """
                                    button {
                                        color: black;
                                    }
                                """,
                            ]
                        ):
                            st.image(page['image'], use_container_width=True)
                            st.write(page['title'])
                            st.write(page['description'])
                            buff, buff, col = st.columns([1, 2, 1])
                            if col.button(f"Read", key=f"button-{page_idx}", type='primary'):
                                switch_page(page['page'])
                    page_idx+=1
            

main = Main("Nevidomyy's blog")
main.mount()