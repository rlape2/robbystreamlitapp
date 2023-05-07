import streamlit as st
import geemap.foliumap as leafmap 
#import ee 

st.set_page_config(layout = "wide")

m = leafmap.Map()
m.add_basemap("HYBRID")
m.to_streamlit()

dropdown = st.selectbox("Basemap", ['HYBRID', 'TERRAIN', 'SATELLITE'])
m.add_basemap(dropdown)