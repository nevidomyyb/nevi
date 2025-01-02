from streamlit_extras.grid import grid
from streamlit_extras.switch_page_button import switch_page
from partials.base_page import BasePage
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from utils.my_pages import pages
    
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
        _grid = grid([0.25, 0.25, 0.25, 0.25])
        # _grid = grid([1, 1, 1, 1])
        for idx, page in enumerate(self.pages):
            with _grid.container(border=True, height=380):
                with stylable_container(
                    key=f"stylable-contaier-grid-{idx}",
                    css_styles=["""
                        button {
                            color: black;
                        }
                        """,
                        """
                        {
                            # border: 1px solid rgba(49, 51, 63, 0.2);
                            # border-radius: 0.5rem;
                            # padding: calc(0.5em - 1px);
                            # background-color: #E6E6E6;
                            # height: 380px;
                        }
                        """
                        ]
                ):
                    _, col1, _ = st.columns([0.2, 2, 0.2])
                    
                    col1.image(page['image'], use_container_width=True)
                    col1.text(page['title'])
                    col1.text(page['description'])
                    buff1, col, buff = st.columns([1, 2, 1])
                    with buff:
                        if st.button(key=f"button-{idx}", label="Read", type='primary', use_container_width=True,):
                            switch_page(page['page'])
            

main = Main("Nevidomyy's blog")
main.mount()