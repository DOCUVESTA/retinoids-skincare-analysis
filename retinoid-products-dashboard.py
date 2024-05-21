# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# configure web app
st.set_page_config(page_title="Retinoid Product Information",
                   page_icon=":lotion_bottle:",
                   layout="wide"
                   )


# create dataframe from csv file
path = '/Users/micheleescano/Desktop/Python/Projects/Project 1/csv/df_retinoid.csv'
df_retinoid = pd.read_csv(path)


# sidebar configuration
st.sidebar.header("Please Filter Here")
retinoids = st.sidebar.multiselect(
    "Select retinoid:",
    options=df_retinoid['retinoids'].unique(),
    default="Retinyl Palmitate"
   
)

product_type = st.sidebar.multiselect(
    "Select product type:",
    options=df_retinoid['product_type'].unique(),
    default=df_retinoid['product_type'].unique()
)

df_selection = df_retinoid.query(
    "retinoids == @retinoids & product_type == @product_type "
    
)

# main page configuration
st.title(":lotion_bottle: Retinoid Products Dashboard")

st.markdown("---")

# KPIs variables
product_count = df_selection.shape[0]
highest_price = df_selection['price'].max()
formatted_highest_price = "{:.2f}".format(highest_price)
lowest_price = df_selection['price'].min()
formatted_lowest_price = "{:.2f}".format(lowest_price)


# KPIs columm configuration
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Number of Products:")
    st.subheader(f"{product_count}")

with middle_column:
    st.subheader("Highest Priced Product:")
    st.subheader(f"US $ {formatted_highest_price}")
    
    
with right_column:
    st.subheader("Lowest Priced Product:")
    st.subheader(f"US ${formatted_lowest_price}")
    
st.markdown("---")


# CHARTS
# plotly subplots
fig = px.scatter(df_selection, 
                 x='brand', 
                 y='price', 
                 hover_name='brand',
                 hover_data={'product_name':True,
                             'price': ':.2f', 
                             'country_of_origin':True,
                             'product_type':True,
                             'category': False, 
                             'brand':False},
                 color = "product_type",
                 facet_col="category",
                 category_orders={"category": ["Luxury", "Affordable"]},
                 labels=dict(brand="Brand", price="Price (USD)"),
                 color_discrete_map={
                    "Serum": "#E8D4D1",
                    "Eye Care": "#F6CAAC",
                    "Mask": "#FF3D3D",
                    "Peel": "#F59870",
                    "Moisturiser": "#FFF0E5",
                    "Toner": "#CE3F4E",
                    "Cleanser": "#B23A59",
                    "Oil": "#7B2940",
                    "Balm": "#B44F8D",
                    "Exfoliator": "#A67397",
                    "Body Wash": "#704004"
                     }
                )

# update inside of plot
fig.update_traces(
    marker=dict(
        size=12, 
        symbol="circle", 
        line=dict(
            width=1,
        )
    ),
    selector=dict(mode="markers"),
)


# update title and design of plot
fig.update_layout(title="Product Information: Luxury vs Affordable <br><sup>Hover over points to display product info</sup>",
                  hovermode=None,
                  paper_bgcolor='#FFFFFF')


# update x-axis
fig.update_xaxes(
    tickangle=-45,
    mirror=True,
    ticks='outside',
    showline=False,
    linecolor='black'
)

# customize legend
fig.update_layout(legend=dict(bordercolor="#E3E9F3", borderwidth=1),
                  legend_tracegroupgap=10, legend_title_text='Product Type'
                 )

# layout size
fig.update_layout(height=500, width=980)

# remove "Category = " from plot subtitle
fig.for_each_annotation(lambda a: a.update(text=a.text.replace("category=", "")))

# show plot
st.plotly_chart(fig)
