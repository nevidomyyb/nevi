import streamlit as st

class Sidebar:
    
    @staticmethod
    def draw():
        with st.sidebar:
            _, col, _ = st.columns([1, 70, 1])
            col.image('./nevi/media/me.png', "Pedro Cunha, Nevidomyy", width=250)
            col.markdown("#")
            col.html(
                """<img src="https://img.icons8.com/?size=24&id=85781&format=png&color=000000"> Alagoas, Brazil"""
            )
            col.html(
                """
                <style>
                    .custom-link {
                        text-decoration: none;
                        color: black;
                    }
                    .custom-link:hover {
                        text-decoration: underline; 
                        color: black; 
                    }
                </style>
                """,
                
            )
            col.html(
                """
                <a href="https://github.com/nevidomyyb" class="custom-link" target="_blank">
                    <img src="https://img.icons8.com/material-outlined/24/github.png" alt="GitHub"/> GitHub
                </a>
                """,
            )
            
            col.html(
                """
                <a href="https://x.com/nevidomyyb" class="custom-link" target="_blank">
                    <img src="https://img.icons8.com/?size=24&id=de4vjQ6J061l&format=png&color=000000" alt="X"/> X/Twitter
                </a>
                """,
            )