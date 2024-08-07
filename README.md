<h1 align="center">
	Type of Retinoids in Skincare Analysis
</h1>

<h3 align="center">
	<img src="https://github.com/DOCUVESTA/retinoids-skincare-analysis/blob/b8efb6d619d66c985561b37f0d3433b24eaa746a/assets/header_retinoid.png"/>
</h3>


## Overview
As a skincare enthusiast, I wasn't surprised in the recent surge in demand for skincare products with retinoids. Retinoids are vitamin-A derivative compounds that are known to be effective treatments for a wide range of skin problems, including acne. In this repository, I perform an analysis on skincare products that contain different type of retinoids. The objective of this analysis is to provide consumers with a foundation of knowledge on the benefits, side effects and characteristics of various retinoids, allowing the users to select the best option for their individual skincare needs. Additionally, the analysis will examine any market gaps for product types and retinoid ingredients that could be worth exploring for brands that wish to develop retinoid skincare.

<br>

## Repository Contents
### Folder: data
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>skincare_products_clean.csv</td>
        <td>source data</td>
    </tr>
    <tr>
        <td>brand.csv</td>
        <td>reference table for brands and country of origin</td>
    </tr>
    <tr>
        <td>df_retinoid.csv</td>
        <td>final cleaned dataframe</td>
    </tr>
</table>

<br>

### Jupyter Notebook: retinoids_skincare_data_transformation.ipynb
- Jupyter notebook with annotations detailing each stage of preprocessing skincare data
- Data exploration process
- Matplotlib, Seaborn and Plotly visualizations

<br>

### Notion: retinoid in skincare analysis public web page
A document with base knowledge on retinoids, along with insights and opportunities for product development derived from analysis.
</details>
<details closed>
<summary>Preview</summary>
<br>
	
![Report](https://github.com/DOCUVESTA/retinoids-skincare-analysis/blob/b8efb6d619d66c985561b37f0d3433b24eaa746a/assets/preview_report_retinoid.png)	
</details>

<p>
  <a href="https://docuvesta.notion.site/Retinoid-in-Skincare-Analysis-b971020483814374badacd4bba8764a3?pvs=4"><img src="https://img.shields.io/badge/Access-webpage-blue?style=for-the-badge&color=%230094AE"></a>
</p>

<br>

### Streamlit: app.py
A user-friendly and interactive dashboard with product information from the skincare dataset.
</details>
<details closed>
<summary>Features</summary>
<br>
<ul>
  <li>Filter Selectors:
    <ul>
      <li>Retinoid(s)</li>
      <li>Product Type(s) </li>
    </ul>
  </li>
  <li>View the following information based on your selected filters:
    <ul>
      <li>Number of products</li>
      <li>Highest priced product</li>
      <li>Lowest priced product</li>
    </ul>
  <li>Product information chart (hover over points in chart to display product information)
    <ul>
      <li>Brand name</li>
      <li>Product type</li>
      <li>Price in USD</li>
      <li>Full product name</li>
      <li>Country of origin of brand</li>
    </ul>
</details>
</details>
<details closed>
<summary>Preview</summary>
<br>
    
![Dashboard](https://github.com/DOCUVESTA/retinoids-skincare-analysis/blob/b8efb6d619d66c985561b37f0d3433b24eaa746a/assets/Dashboard.png)

</details>
<p>
  <a href="https://retinoid-skincare-dashboard.streamlit.app"><img src="https://img.shields.io/badge/Access-dashboard-blue?style=for-the-badge"></a>
</p>
