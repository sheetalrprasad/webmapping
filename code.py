import folium
import pandas as pd

map = folium.Map(location=[38.58,-99.09],zoom_start=5, titles = "Stamen Terrain")

df = pd.read_csv("Volcanoes.txt")
lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])

fg = folium.FeatureGroup(name="My Map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon("green")))
map.add_child(fg)

map.save("Map1.html")
