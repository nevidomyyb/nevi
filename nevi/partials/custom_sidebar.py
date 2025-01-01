import streamlit as st


class Sidebar:
    
    @staticmethod
    def create_link(destination: str, icon: str, text: str, col):
        col.html(
            f"""
            <a href="{destination}" class="custom-link" target="_blank">
                <img src="{icon}" alt="{text}"/> {text}
            </a>
            """
        )
    
    def draw_sidebar(self, ):
        
        with st.sidebar:
            buff, col, _ = st.columns([1, 70, 1])
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
            col.image('./nevi/media/me.png', "Pedro Cunha, Nevidomyy", width=250)
            col.markdown("#")
            col.html(
                """<img src="https://img.icons8.com/?size=24&id=85781&format=png&color=000000"> Alagoas, Brazil"""
            )
            Sidebar.create_link("https://github.com/nevidomyyb", "https://img.icons8.com/material-outlined/24/github.png", "GitHub", col)
            Sidebar.create_link("https://x.com/nevidomyyb", "https://img.icons8.com/?size=24&id=de4vjQ6J061l&format=png&color=000000", "X/Twitter", col )
            Sidebar.create_link("https://www.linkedin.com/in/pedro-cunha-nev/", "https://img.icons8.com/?size=24&id=85044&format=png&color=000000", "Linkedin", col)
            Sidebar.create_link("www.youtube.com/@pedrocunha5807", "https://img.icons8.com/?size=24&id=85064&format=png&color=000000", "Youtube", col)