import folium
import pandas as pd

map = folium.Map(location=[38.58,-99.09],zoom_start=5, titles = "Stamen Terrain")

df = pd.read_csv("Volcanoes.txt")
volcano_loc=[]
for i,row in df.iterrows():
    volcano_loc.append([row['LAT'],row['LON']])

fg = folium.FeatureGroup(name="My Map")
for cor in volcano_loc:
    fg.add_child(folium.Marker(location=cor,popup=str(cor),icon=folium.Icon("green")))
map.add_child(fg)

map.save("Map1.html")
