import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

with open('wojewodztwa-medium.geojson') as f:
    geojson_data = json.load(f)

# Example data
data = {
    'id': [0, 1, 2],
    'value': [100, 200, 300]
}

# Create DataFrame
df = pd.DataFrame(data)

# Example GeoJSON data (replace with your own)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [19.4698, 50.9154]}, "properties": {"id": 0}},
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [19.4689, 50.9137]}, "properties": {"id": 1}},
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [19.7958, 50.8155]}, "properties": {"id": 2}}
    ]
}

# Create choropleth map using Plotly
fig = px.choropleth_mapbox(df, geojson=geojson_data, locations='id', color='value',
                           featureidkey="properties.id",
                           mapbox_style="carto-positron",
                           center={"lat": 50.9154, "lon": 19.4698},
                           zoom=5, opacity=0.7,
                           color_continuous_scale="Viridis",
                           labels={'value':'Value'}
                          )

# Update layout
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the figure
fig.show()
