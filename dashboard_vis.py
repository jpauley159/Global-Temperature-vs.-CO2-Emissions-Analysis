import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load CO₂ data
co2_df = pd.read_csv("cleaned_owid_co2_data.csv")
global_df = co2_df[co2_df['country'] == 'World']

# Load and clean temperature data
temp_df = pd.read_csv("GLB.Ts+dSST.csv")
temp_df.replace("***", pd.NA, inplace=True)

# Convert all columns (except 'Year') to numeric
for col in temp_df.columns[1:]:
    temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')

# Sidebar filters
st.sidebar.title("Filters")
year_range = st.sidebar.slider("Select Year Range", 
                               int(global_df['Year'].min()), 
                               int(global_df['Year'].max()), 
                               (1980, 2020))

# Filter and clean data
filtered_co2 = global_df[
    (global_df['Year'] >= year_range[0]) & 
    (global_df['Year'] <= year_range[1])
].dropna(subset=['Year', 'co2'])

filtered_temp = temp_df[
    (temp_df['Year'] >= year_range[0]) & 
    (temp_df['Year'] <= year_range[1])
].dropna(subset=['Year', 'J-D'])

# Create figure
fig_combined = go.Figure()

# CO2 Emissions Line
fig_combined.add_trace(go.Scatter(
    x=filtered_co2['Year'],
    y=filtered_co2['co2'],
    name="CO₂ Emissions (Mt)",
    mode='lines',
    line=dict(color='yellow')
))

# Temperature Anomaly Line
fig_combined.add_trace(go.Scatter(
    x=filtered_temp['Year'],
    y=filtered_temp['J-D'],
    name="Temperature Anomaly (°C)",
    mode='lines',
    line=dict(color='red'),
    yaxis='y2'
))

# Layout
fig_combined.update_layout(
    title="Global CO₂ Emissions and Temperature Anomalies Over Time",
    xaxis=dict(title="Year"),
    yaxis=dict(
        title=dict(text="CO₂ Emissions (Mt)", font=dict(color="white")),
        tickfont=dict(color="white")
    ),
    yaxis2=dict(
        title=dict(text="Temperature Anomaly (°C)", font=dict(color="white")),
        tickfont=dict(color="white"),
        overlaying="y",
        side="right"
    ),
    legend=dict(x=0.01, y=0.99),
    template="plotly_white"
)

# Show in app
st.plotly_chart(fig_combined)
