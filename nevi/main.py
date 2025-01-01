import streamlit as st
from streamlit_extras.bottom_container import bottom
from partials.custom_sidebar import Sidebar
from partials.custom_bottom import Bottom

st.set_page_config(
    page_title="Nevidomyy's blog",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScFu4Gw8_z-p4d7njXvA8cT2KM2Qq7D7LDOZMjA13-sEFphgVR-A0tiG4gasGmGVStZck&usqp=CAU",
    layout='wide',
    initial_sidebar_state='expanded',
)

st.markdown("### Nevidomyy's blog")
st.markdown("###### I made this.")

Sidebar.draw()

Bottom.draw()
    
    

