import streamlit as st
from partials.base_page import BasePage

class WPPChatAnalysis(BasePage):
    
    def __init__(self, ):
        self.page_title = "WhatsApp chat analysis"
        st.session_state['page'] = 'wpp chat analysis'
        super().__init__(page_title=self.page_title)
        
    def draw(self):
        st.markdown("""
        ### How it started?
        ##### What was my objective ?            
        
        In the middle of 2024 I decided to change my career in technology. Currently (03/2025) I work with software development, more specifically with Python and its libraries and technologies, and I intend to work and study Data Science in general, with a focus on Machine Learning.

        From there I began to study the specifics of this area and realized that in addition to being something very technical, it is also a very theoretical area based on statistics and a lot of mathematics, I would even say that it is from a certain point of view, philosophical.
        But leaving the specifics aside, and focusing a little more on the technical side, this project was one of the ones I used to practice some of the things I saw in my undergraduate Probability and Statistics course.    
        
        
        The aim of the project was to create an application that would run a pipeline to clean and transform a text file that Whatsapp makes available from group conversations, and thereby generate some metrics and information, such as the average number of words sent by each member of the group, the word cloud and the most sent words or phrases.
        """)        
        
        st.markdown("""
        ### The progress of the project
        
        As I continued to work on the project, I realized that I needed to learn a few things in order to succeed. That's when the project took on an extra depth: NLP and N-grams.

        Right from the start, I knew that I would have to get to grips with NLP, since the whole project is based on text and peer-to-peer communication, and before this project I had no in-depth knowledge of this field. But I'll come back to that later.

        In addition, the information cleaning and extraction stage was not complicated, just Pandas/Polars to work with the raw data. As a result, I got the metrics I was looking for, the most used words, the most common n-grams for each member of the group, a word cloud and graphs to visualize this information, done in Streamlit.
        
        """)
        st.markdown("""
        ### Next steps
        
        Although I didn't delve into NLP, I had to use the concepts I'd learned about language processing and N-gram theory to be able to clean up properly for the next steps.

        My idea is to use the clean dataset (no meaningless words, and no formatting or spam errors) to apply a Clustering algorithm, and with that identify subgroups of members who have a similar language.
                    """)
        
        
page = WPPChatAnalysis()
page.mount()
    