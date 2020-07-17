import folium
import pandas as pd


df = pd.read_csv('worldVolcanoes.txt',delimiter=';')
lat = list(df['Latitude'])
lon = list(df['Longitude'])
elev = list(df['Elev'])
name = list(df['Volcano Name'])

html = """
Volcano name: <br>
<a href= "https://www.google.com/search?q=%s volcano" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[44.0,-23.7],zoom_start=3, titles = 'Stamen Terrain')


def color_producer(elev):
    if elev < 1000:
        return'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

fg_p = folium.FeatureGroup(name='Population')
fg_p.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
                            style_function=
                            lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))


map.add_child(fg_p)


fg_v = folium.FeatureGroup(name='Volcanoes')
for lt,ln,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name,name,el),width=200,height=100)
    fg_v.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(iframe),radius=5, weight=1,fill=True,fill_opacity=1,color='black',fill_color=color_producer(el)))

map.add_child(fg_v)

map.add_child(folium.LayerControl())

map.save('WorldMap.html')
