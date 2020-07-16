import folium
map = folium.Map(location=[38.58,-99.09],zoom_start=6, titles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I'm a Marker",icon=folium.Icon("green")))
fg.add_child(folium.Marker(location=[37.2,-97.1],popup="Hi I'm a Marker",icon=folium.Icon("green")))

map.add_child(fg)

map.save("Map1.html")
