import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load data
co2_df = pd.read_csv('cleaned_owid_co2_data.csv')
temp_df = pd.read_csv('GLB.Ts+dSST.csv')

# Clean temperature data
temp_df.replace("***", pd.NA, inplace=True)
for col in temp_df.columns[1:]:
    temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')



# Merge yearly global averages with CO2 data (global only)
global_df = co2_df[co2_df['country'] == 'World']
merged_df = pd.merge(global_df, temp_df[['Year', 'J-D']], on='Year', how='inner')

# Sidebar
st.sidebar.title("Filters")
year_range = st.sidebar.slider("Select Year Range", 
                               int(temp_df['Year'].min()), 
                               int(temp_df['Year'].max()), 
                               (1880, 2024))

# Filtered Data
filtered_co2 = global_df[
    (global_df['Year'] >= year_range[0]) & 
    (global_df['Year'] <= year_range[1])
].dropna(subset=['Year', 'co2'])

filtered_temp = temp_df[(temp_df['Year'] >= year_range[0]) & (temp_df['Year'] <= year_range[1])]
filtered_merged = merged_df[(merged_df['Year'] >= year_range[0]) & (merged_df['Year'] <= year_range[1])]

# Dashboard
st.title("🌍 Climate Dashboard")
st.markdown("CO₂ Emissions and Temperature Trends")


# Create figure and predefine yaxis2 in layout
fig_combined = go.Figure(layout=dict(
    yaxis=dict(title="CO₂ Emissions (Mt)", titlefont=dict(color="white"), tickfont=dict(color="white")),
    yaxis2=dict(
        title="Temperature Anomaly (°C)",
        titlefont=dict(color="white"),
        tickfont=dict(color="white"),
        overlaying="y",
        side="right"
    )
))

# CO2 Line (primary y-axis)
fig_combined.add_trace(go.Scatter(
    x=filtered_co2['Year'], 
    y=filtered_co2['co2'], 
    name="CO₂ Emissions (Mt)",
    mode='lines',
    line=dict(color='yellow')
))

# Temperature Anomaly Line (secondary y-axis)
fig_combined.add_trace(go.Scatter(
    x=filtered_temp['Year'], 
    y=filtered_temp['J-D'], 
    name="Temperature Anomaly (°C)",
    mode='lines',
    line=dict(color='red'),
    yaxis="y2"
))

# Update other layout elements
fig_combined.update_layout(
    title="Global CO₂ Emissions and Temperature Anomalies Over Time",
    xaxis=dict(title="Year"),
    legend=dict(x=0.01, y=0.99),
    template="plotly_white"
)

st.plotly_chart(fig_combined)

# Scatter: CO2 vs Temperature Anomaly
st.subheader("CO₂ vs Temperature Anomaly (J-D)")
fig3 = px.scatter(
    filtered_merged,
    x="co2",
    y="J-D",
    trendline="ols",
    trendline_color_override='red',
    labels={"co2": "CO₂ Emissions (Mt)", "J-D": "Temperature Anomaly (°C)"},
    title="CO₂ vs Temperature (with Regression Line)",
    color_discrete_sequence=['yellow']  # Set dots to blue
)
st.plotly_chart(fig3)
