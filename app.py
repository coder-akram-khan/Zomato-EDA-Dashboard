
## Set Streamlit Page Configuration
import streamlit as st


# Set the page configuration
st.set_page_config(
    page_title="Zomato EDA Dashboard",
    page_icon="assets/logo.png",
    layout="wide"
)


# Load custom CSS

with open("assets/styles.css") as f:

    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title of the app with custom styling

st.markdown('<div class="title">Zomato EDA Dashboard 🍴</div>', unsafe_allow_html=True)
#st.title("Zomato EDA Dashboard 🍴")


st.sidebar.title("Filters")
st.markdown("An interactive dashboard to explore Zomato restaurant data.")



## Data Loading & Transformation

import pandas as pd

# Load data
country_data = pd.read_excel("dataset/Zomatodataset/Country-Code.xlsx")

zomato_data = pd.read_csv("dataset/Zomatodataset/zomato.csv", encoding='latin-1')

# Merge datasets
merged_data = zomato_data.merge(country_data, how="left", on="Country Code")

st.write("Sample Data", merged_data.head())

## Sidebar Filters

countries = merged_data["Country"].unique()
selected_country = st.sidebar.multiselect("Select Country", countries, default=countries)

cities = merged_data["City"].unique()
selected_city = st.sidebar.multiselect("Select City", cities, default=cities)

price_range = st.sidebar.slider("Price Range", 1, 4, (1, 4))
rating_range = st.sidebar.slider("Aggregate Rating Range", 0.0, 5.0, (0.0, 5.0))

## Data Filtering
# Filter data based on sidebar inputs
filtered_data = merged_data[
    (merged_data["Country"].isin(selected_country)) &
    (merged_data["City"].isin(selected_city)) &
    (merged_data["Price range"].between(price_range[0], price_range[1])) &
    (merged_data["Aggregate rating"].between(rating_range[0], rating_range[1]))
]



## Metrics Section
# Metrics
from streamlit_extras.metric_cards import style_metric_cards

# Metrics Section
st.markdown("## Metrics", unsafe_allow_html=True)

# Create columns for metrics
col1, col2, col3 = st.columns(3)

# Define metric values
total_restaurants = len(filtered_data)
average_rating = round(filtered_data["Aggregate rating"].mean(), 2)
total_votes = filtered_data['Votes'].sum()

# Display metrics with icons
with col1:
    st.metric(label="Total Restaurants", value=total_restaurants, delta="🔺10", delta_color="normal")
    
with col2:
    st.metric(label="Average Rating", value=average_rating, delta="🔻0.1", delta_color="inverse")
    
with col3:
    st.metric(label="Total Votes", value=total_votes, delta="🔺500", delta_color="normal")

# Style the metric cards
style_metric_cards(background_color="#071021", border_left_color="#cb202d")

# Optional: Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

## Charts & Visualizations
import plotly.express as px
import plotly.graph_objects as go

# Container for Charts
st.markdown("## Charts & Visualizations")



# Chart 1: Bar Chart - Top Cuisines by Popularity
st.markdown("### Top Cuisines by Popularity")
cuisine_data = filtered_data["Cuisines"].value_counts().reset_index()
cuisine_data.columns = ["Cuisine", "Count"]
fig1 = px.bar(cuisine_data.head(10), x="Cuisine", y="Count", title="Top 10 Popular Cuisines")
fig1.update_traces(marker=dict(color='rgba(0,123,255,0.8)', line=dict(color='rgba(0,0,0,0.5)', width=1)))
fig1.update_layout(title_font=dict(size=20), xaxis_title_font=dict(size=14), yaxis_title_font=dict(size=14))


# Chart 2: Pie Chart - Distribution of Table Booking
st.markdown("### Distribution of Table Booking Availability")
booking_data = filtered_data["Has Table booking"].value_counts().reset_index()
booking_data.columns = ["Booking", "Count"]
fig2 = px.pie(booking_data, names="Booking", values="Count", title="Table Booking Availability")
fig2 = px.pie(
    booking_data,
    names="Booking",
    values="Count",
    title="Table Booking Availability",
    hole=0.4  # Donut-style chart
)
fig2.update_traces(textinfo="percent+label")


custom_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

fig1.update_traces(marker_color=custom_palette)
fig2.update_traces(marker_colors=custom_palette)


# Organize first row charts
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Heatmap - Correlation of Numeric Features
st.markdown("### Correlation Heatmap")
numeric_cols = ["Average Cost for two", "Price range", "Aggregate rating", "Votes"]
corr = filtered_data[numeric_cols].corr()
fig3 = px.imshow(corr, text_auto=True, title="Heatmap of Numeric Correlations")

# Chart 4: World Map - Restaurant Locations
st.markdown("### World Map of Restaurant Locations")
fig4 = px.scatter_geo(
    filtered_data,
    lat="Latitude",
    lon="Longitude",
    hover_name="Restaurant Name",
    color="Aggregate rating",
    title="World Map of Restaurant Locations",
    projection="natural earth"
)

# Organize second row charts
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(fig3, use_container_width=True)
with col4:
    st.plotly_chart(fig4, use_container_width=True)

# Chart 5: Treemap - Cuisines by Popularity
st.markdown("### Cuisines Treemap")
fig5 = px.treemap(cuisine_data.head(20), path=["Cuisine"], values="Count", title="Cuisines Treemap")

# Chart 6: Barplot of Ratings
st.markdown("### Distribution of Ratings")
ratings =filtered_data.groupby(
    ['Aggregate rating', 'Rating color', 'Rating text']
    ).size().reset_index().rename(columns={0:'Rating Count'})
fig6 = px.bar(ratings, x="Aggregate rating", y="Rating Count", color='Rating color', title="Bar Plot of Ratings")
fig6.add_annotation(
    x=4.5, y=500,
    text="Highest Rating Count",
    showarrow=True,
    arrowhead=2,
    ax=-40, ay=-40
)


# Organize third row charts
col5, col6 = st.columns(2)
with col5:
    st.plotly_chart(fig5, use_container_width=True)
with col6:
    st.plotly_chart(fig6, use_container_width=True)

# Chart 7: Scatter Plot - Restaurant Locations
st.markdown("### Restaurant Locations (Latitude vs Longitude)")
fig7 = px.scatter(
    filtered_data,
    x="Longitude",
    y="Latitude",
    color="City",
    hover_name="Restaurant Name",
    title="Restaurant Locations",
)

# Full-width chart
st.plotly_chart(fig7, use_container_width=True)

# Count Plot - Number of Restaurants by Rating Text

st.markdown("### Count Plot: Number of Restaurants by Rating Text")

rating_count_data = filtered_data["Rating text"].value_counts().reset_index()

rating_count_data.columns = ["Rating Text", "Count"]


fig_count = px.bar(

    rating_count_data,

    x="Rating Text",

    y="Count",

    color="Rating Text",

    title="Number of Restaurants by Rating Text",

    text="Count",

    labels={"Count": "Number of Restaurants", "Rating Text": "Rating"}

)

fig_count.update_traces(textposition="outside")

fig_count.update_layout(title_font=dict(size=20), xaxis_title="", yaxis_title="Count")


# Sunburst Chart - Restaurants by Country and Rating

st.markdown("### Sunburst Chart: Restaurants by Country and Rating Text")

sunburst_data = filtered_data.groupby(["Country", "Rating text"]).size().reset_index(name="Count")


fig_sunburst = px.sunburst(

    sunburst_data,

    path=["Country", "Rating text"],

    values="Count",

    color="Country",

    title="Restaurants by Country and Rating Text"

)

fig_sunburst.update_layout(title_font=dict(size=20))


# Organize Count Plot and Sunburst in one row

col7, col8 = st.columns(2)


with col7:

    st.plotly_chart(fig_count, use_container_width=True)


with col8:

    st.plotly_chart(fig_sunburst, use_container_width=True)

st.write("Filtered Data", filtered_data.head())
## Download Button for Filtered Data
#  Download button
@st.cache_data
def convert_to_csv(data):
    return data.to_csv(index=False).encode("utf-8")

csv = convert_to_csv(filtered_data)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_zomato_data.csv",
    mime="text/csv"
)

st.markdown(
    """
    <footer style='text-align: center; font-size: small;'>
    Developed by <b>Akram Khan</b> | <a href="https://github.com/coder-akram-khan">GitHub</a> | <a href="https://www.linkedin.com/in/mr-akram-khan/">LinkedIn</a>
    </footer>
    """,
    unsafe_allow_html=True
)
