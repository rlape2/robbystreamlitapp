import streamlit as st
import geemap.foliumap as leafmap 
#import ee 

st.set_page_config(layout = "wide")

col1, col2 = st.columns([7, 3])

options = list(leafmap.basemaps.keys())

with col2:
    dropdown = st.selectbox("Basemap", options)

    default_url = leafmap.basemaps[dropdown].tiles

    url = st.text_input("Enter URL", default_url)

m = leafmap.Map()
m.add_basemap("HYBRID")
m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name='Tile Layer', attribution=' ')

with col1:
    m.to_streamlit()

#dropdown = st.selectbox("Basemap", ['HYBRID', 'TERRAIN', 'SATELLITE'])
#m.add_basemap(dropdown)