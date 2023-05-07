import streamlit as st
import geemap.foliumap as leafmap 
#import ee 

st.set_page_config(layout = "wide")

col1, col2 = st.columns([4, 1])

options = list(leafmap.basemaps.keys())

with col2:
    dropdown = st.selectbox("Basemap", options)
    url = st.text_input("Enter URL")

m = leafmap.Map()
m.add_basemap("HYBRID")
m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name='Tile Layer', attribution=' ')

with col1:
    m.to_streamlit()

#dropdown = st.selectbox("Basemap", ['HYBRID', 'TERRAIN', 'SATELLITE'])
#m.add_basemap(dropdown)