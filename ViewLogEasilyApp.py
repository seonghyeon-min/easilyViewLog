import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import altair as alt
from streamlit_quill import st_quill


    
alt.themes.enable("dark")
def set_page_config() :
    st.set_page_config(
        page_title="View Log",
        page_icon="🔥",
        layout='wide',
        initial_sidebar_state="expanded"
    )

def main() : 
    set_page_config()
    """
    # View Logger
    
    This app shows off viewing Log easily with Streamlit.
    
    If you want to try this, you'll first need to install some packages
    
    ```
    pip install requirement.txt
    ```
    
    ## Basic example
    Show how to use this Application. Just write logs down text area. 
    
    before you put down some logs, you need to check line by line.
    """

    st.header('')
    content = st_quill()

    try : 
        LogsLst = content.split('\n')
        Logtodataframe = []
        
        
        for log in LogsLst :
            Logtodataframe.append(log.split(' ', maxsplit=8))
        
        df = pd.DataFrame(Logtodataframe, columns=['datetime', 'b', 'module1', 'module2', 'e', 'Context_Name', 'Message_Id', 'data', 'data2'])
        df = df.drop(columns=['b', 'e'])
        
        """
        then, you can see the dataframe like below
        """
        st.dataframe(df, use_container_width=True)
        
        """
        also, after fitering some columns, you can see the filterd data
        """
        col1, col2 = st.columns(2)
        
        with col1 :
            context_options = st.multiselect(
                "Filter Context",
                df['Context_Name'].unique(),
                df['Context_Name'].unique()[0]
            )
        
        with col2 :
            df_q = df.query("Context_Name in @context_options")
            
            message_options = st.multiselect(
                "Filter MessageId",
                df_q['Message_Id'].unique(),
                df_q['Message_Id'].unique()[0]
            )
        
        str_expr = "(Context_Name in @context_options) and (Message_Id in @message_options)"
        df_q = df.query(str_expr)
        # st.dataframe(df_q, use_container_width=True)
        
        st.json(df_q.to_json(orient='records'))
        st.divider()
        
        

    except Exception as err :
        st.warning('please input the log text or take care the Error message.')
        st.warning(f'{err}')


    
if __name__ == '__main__' :
    main()
