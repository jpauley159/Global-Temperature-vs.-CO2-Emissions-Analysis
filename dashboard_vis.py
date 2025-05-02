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
merged_df.rename(columns={'co2': 'CO2_emissions', 'J-D': 'temp_anomaly'}, inplace=True)

# Sidebar
st.sidebar.title("Filters")
year_range = st.sidebar.slider("Select Year Range",
                               int(temp_df['Year'].min()),
                               int(temp_df['Year'].max()),
                               (1880, 2024))

# Filtered Data
filtered_df = merged_df[(merged_df['Year'] >= year_range[0]) & (merged_df['Year'] <= year_range[1])]

# Dashboard Title
st.title("🌍 Climate Dashboard")
st.markdown("### CO₂ Emissions and Temperature Trends")

# Combined Dual-Axis Plot
fig_combined = go.Figure()

# CO2 trace (primary y-axis)
fig_combined.add_trace(go.Scatter(
    x=filtered_df['Year'],
    y=filtered_df['CO2_emissions'],
    name="CO₂ Emissions (Mt)",
    mode='lines',
    line=dict(color='yellow')
))

# Temperature trace (secondary y-axis)
fig_combined.add_trace(go.Scatter(
    x=filtered_df['Year'],
    y=filtered_df['temp_anomaly'],
    name="Temperature Anomaly (°C)",
    mode='lines',
    line=dict(color='red'),
    yaxis="y2"
))

# Layout configuration
fig_combined.update_layout(
    title="Global CO₂ Emissions and Temperature Anomalies Over Time",
    xaxis=dict(title="Year"),
    yaxis=dict(
        title="CO₂ Emissions (Mt)",
        titlefont=dict(color="yellow"),
        tickfont=dict(color="yellow")
    ),
    yaxis2=dict(
        title="Temperature Anomaly (°C)",
        titlefont=dict(color="red"),
        tickfont=dict(color="red"),
        overlaying="y",
        side="right"
    ),
    legend=dict(x=0.01, y=0.99),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)

# Display dual-axis chart
st.plotly_chart(fig_combined)

# Scatterplot with regression
st.subheader("CO₂ vs Temperature Anomaly (J-D)")
fig_scatter = px.scatter(
    filtered_df,
    x="CO2_emissions",
    y="temp_anomaly",
    trendline="ols",
    trendline_color_override='red',
    labels={
        "CO2_emissions": "CO₂ Emissions (Mt)",
        "temp_anomaly": "Temperature Anomaly (°C)"
    },
    title="CO₂ vs Temperature (with Regression Line)",
    color_discrete_sequence=['orange']
)
fig_scatter.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)
st.plotly_chart(fig_scatter)
