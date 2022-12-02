import streamlit as st
import geemap.foliumap as geemap
import ee 

st.title("TN Land Use")

Map = geemap.Map()
Map.to_streamlit()


