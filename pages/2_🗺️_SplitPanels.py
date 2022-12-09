import streamlit as st
import geemap.foliumap as geemap
import ee 

st.title("County Split Panel Maps")

Map = geemap.Map()

counties = ee.FeatureCollection("TIGER/2018/Counties")
knox = counties.filter(ee.Filter.eq('NAME', 'Knox'))
knoxtn = knox.filter(ee.Filter.eq('STATEFP', '47'))
style = {'fillColor': '00000000'}

nlcd_2001 = ee.Image('USGS/NLCD_RELEASES/2019_REL/NLCD/2001').select('landcover')
nlcd_2019 = ee.Image('USGS/NLCD_RELEASES/2019_REL/NLCD/2019').select('landcover')

left_layer = geemap.ee_tile_layer(nlcd_2001.clip(knoxtn), {}, 'NLCD 2001')
right_layer = geemap.ee_tile_layer(nlcd_2019.clip(knoxtn), {}, 'NLCD 2019')

Map.split_map(left_layer, right_layer)

Map.addLayer(knoxtn)
Map.center_object(knoxtn)
Map.add_legend(builtin_legend='NLCD')
Map

Map.to_streamlit()