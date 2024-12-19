import folium
import json
from branca.colormap import LinearColormap

# Load your GeoJSON file
with open('wojewodztwa-medium.geojson') as f:
    geojson_data = json.load(f)

# Example values assigned to each feature (replace with your own)
values = {
    1: 3.7,    # śląskie
    2: 5.9,    # opolskie
    3: 2.9,    # wielkopolskie
    4: 6.7,    # zachodniopomorskie
    5: 7.8,    # świętokrzyskie
    6: 7.3,    # kujawsko-pomorskie
    7: 7.0,    # podlaskie
    8: 4.5,    # dolnośląskie
    9: 8.8,    # podkarpackie
    10: 4.4,   # małopolskie
    11: 4.6,   # pomorskie
    12: 8.6,   # warmińsko-mazurskie
    13: 5.5,   # łódzkie
    14: 4.3,   # mazowieckie
    15: 8.0,   # lubelskie
    16: 4.4    # lubuskie
}

# Normalize values to range between 0 and 1
min_value = min(values.values())
max_value = max(values.values())
normalized_values = {k: (v - min_value) / (max_value - min_value) for k, v in values.items()}

# Create a color map
color_map = LinearColormap(['yellow', 'orange', 'red'], index=[0, 0.5, 1], vmin=0, vmax=1, caption='Stopa bezrobocia w Polsce')

# Create a map centered at a certain location
mymap = folium.Map(location=[52.198, 19.2824], zoom_start=12)  # Set tiles to None

# Add GeoJSON data to the map with custom styling for choropleth
folium.GeoJson(
    geojson_data,
    style_function=lambda feature: {
        'fillColor': color_map(normalized_values.get(feature['properties']['id'], 0)),
        'color': 'black',
        'fillOpacity': 0.7,
        'weight': 1
    }
).add_to(mymap)

# Add the color map legend to the map
color_map.add_to(mymap)

# Save the map to an HTML file
mymap.save("map_MAP.html")
