import streamlit as st
from streamlit_extras.bottom_container import bottom

class Bottom:
    
    def draw_bottom(self, ):
        with bottom():
            st.write(":material/copyright: Nevidomyy's blog. Powered with Streamlit & Render")