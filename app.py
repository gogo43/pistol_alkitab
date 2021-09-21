from numpy import array
import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import neattext.functions as nfx


import matplotlib.pyplot as plt
import altair as alt
import random

@st.cache
def load_bible(data):
    df = pd.read_csv(data)
    return df

def load_bible2(data):
    df2 = pd.read_csv(data)
    return df2
def main():
    st.title("Pistol Air Alkitab")
    menu = ['Home','Multiverse','Search','About']
    
    df = load_bible('data/tb3.csv')
    df2 = load_bible2('data/tb2.csv')

    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'Home':
        st.subheader("Single Verse Alkitab")
        #st.dataframe(df)
        kitab_list = df['kitab'].unique().tolist()
        kitab_name = st.sidebar.selectbox('Kitab',kitab_list)
        pasal = st.sidebar.number_input('Pasal',1)
        ayat = st.sidebar.number_input('Ayat',1)
        bible_df = df[df['kitab']== kitab_name]
        #st.dataframe(bible_df)
        try:
            selected_passage = bible_df[(bible_df['pasal'] == pasal) & (bible_df['ayat'] == ayat)]
            #st.write(selected_passage)
            passage_detail ="{} Pasal:: {} Ayat:: {}".format(kitab_name,pasal,ayat)
            st.info(passage_detail)
            passage = "{}".format(selected_passage['firman'].values[0])
            st.write(passage)
        except:
            st.warning('Book is out of range')
        
        ## ------------random Ayat ---------------##

        #st.success('Satu Ayat Setiap Hari')
        #pasal_list = range(10)
        #ayat_list = range(20)
        #ps_list = random.choice(pasal_list)
        #ay_list =random.choice(ayat_list)
        #random_kitab_name = random.choice(kitab_list)
        #st.write("Kitab:{} Pasal:{} Ayat:{}".format(random_kitab_name,ps_list,ay_list))
        #rand_kitab_df = df[df['kitab'] == random_kitab_name]
        #try:
            #randomly_selected_passage = rand_kitab_df[(rand_kitab_df ['pasal'] == ps_list) & (rand_kitab_df ['ayat'] == ay_list)]
            #mytext=randomly_selected_passage['firman'].values[0]
        #except:
            #randomly_selected_passage = rand_kitab_df[(rand_kitab_df ['pasal'] == 1) & (rand_kitab_df ['ayat'] == 1)]
            #mytext=randomly_selected_passage['firman'].values[0]
        #sst.write(mytext)

    elif choice =='Search':
        st.subheader("Search Alkitab")
       
        #-------------topic search--------------##
        search_term = st.text_input('Search name in alkitab')
        with st.expander ('View result'):
                retreived_df=df[df['firman'].str.contains(search_term)]
                st.dataframe(retreived_df[['kitab','pasal','ayat','firman']])
                          

    elif choice =='Multiverse':
        st.subheader("Multi Verse Alkitab")
        kitab_list = df2['kitab'].unique().tolist()
        kitab_name = st.sidebar.selectbox('Kitab',kitab_list)
        pasal = st.sidebar.number_input('Pasal',1)
        bible_df = df2[(df2['kitab']== kitab_name) & (df2['pasal'] == pasal)]
        ayat_list=  df2['ayat'].unique().tolist()
        ayat =st.sidebar.multiselect('Ayat',ayat_list,default=1)
        #st.write(ayat)
        selected_passage = bible_df.iloc[ayat]
        #st.write(selected_passage)
        passage_detail ="{} Pasal:{} Ayat:{}".format(kitab_name,pasal,ayat)
        st.info(passage_detail)
        #st.dataframe(selected_passage)
        
        
        st.info('Details')
        for i, row in selected_passage.iterrows():
            st.write(row['firman'])
    

    else :
        st.subheader('Create by Pistolair')
        st.text('pistol.air32@gmail.com')


if __name__ == '__main__' :
    main()
