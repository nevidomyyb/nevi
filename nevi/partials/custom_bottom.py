import streamlit as st
from streamlit_extras.bottom_container import bottom

class Bottom:
    
    @staticmethod
    def draw():
        with bottom():
            buff, col, buff1 = st.columns([1, 5, 1])
            buff1.write("Constructed with Streamlit and ❤️")