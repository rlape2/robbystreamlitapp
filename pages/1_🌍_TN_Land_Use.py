import streamlit as st
import geemap.foliumap as geemap
import ee 

st.title("TN Land Use")

 

col1, col2 = st.columns([2, 1])

counties = ee.FeatureCollection('TIGER/2018/Counties')
feat = counties.filter(ee.Filter.eq('STATEFP', '47'))
style = {'fillColor': '00000000'}

options = feat.aggregate_array('NAMELSAD').getInfo()
options.sort()

default_county = "Knox County"

options.remove(default_county)
options.insert(0, default_county)
options.insert(1, "Williamson County")
options.insert(2, "Maury County")

default_index = options.index("Knox County")

with col2:

    county = st.selectbox("Select a county", options, default_index )



Map = geemap.Map()

dataset = ee.Image('USGS/NLCD_RELEASES/2019_REL/NLCD/2019')
landcover = dataset.select('landcover')
TN = landcover.clipToCollection(feat)

fc = feat.filter(ee.Filter.eq('NAMELSAD', county))
selection = TN.clipToCollection(fc)
Map.centerObject(fc)
Map.addLayer(selection, {}, 'selected county')







# fc1 = TN.clipToCollection(feat)
# dataset = fc1.clipToCollection(fc)
# Map.centerObject(fc)


Map.addLayer(feat.style(**style), {}, "Counties", False)
Map.add_legend(title='NLCD Land Cover', builtin_legend='NLCD')

with col1:
    Map.to_streamlit()


