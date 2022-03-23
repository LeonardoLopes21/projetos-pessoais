import folium
import pandas

data = pandas.read_csv('wonders.txt')
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
wonders = list(data["NAME"])
country = list(data["COUNTRY"])

def color_producer(longy):
    if longy > 0:
        return "darkred"
    else:
        return "darkgreen"


map = folium.Map(location=[48.20867044043768, 16.374412884980337], zoom_start=5, tiles="Stamen Toner")

fgw = folium.FeatureGroup(name = "World Wonders")

for lt, ln, wn, cn in zip(lat, lon, wonders, country):
    fgw.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=f"<b>{wn}</b>, <i>{cn}</i>", fill_color = color_producer(ln), color =color_producer(ln), fill_opacity = 0.65))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green'
 if x['properties']['POP2005'] < 10000000 else 'yellow' if x['properties'] ['POP2005'] < 250000000 else 'orange' if x['properties'] ['POP2005'] < 1000000000 else 'red'}))

map.add_child(fgw)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
