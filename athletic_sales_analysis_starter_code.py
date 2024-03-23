#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Import Libraries and Dependencies
import pandas as pd


# ### 1. Combine and Clean the Data
# #### Import CSVs

# In[30]:


# Read the CSV files into DataFrames.
df_2020 = pd.read_csv("Resources/athletic_sales_2020.csv")
df_2021 = pd.read_csv("Resources/athletic_sales_2021.csv")


# In[31]:


# Display the 2020 sales DataFrame
df_2020


# In[32]:


# Display the 2021 sales DataFrame
df_2021


# #### Check the data types of each DataFrame

# In[33]:


# Check the 2020 sales data types.
df_2020.dtypes


# In[34]:


# Check the 2021 sales data types.
df_2021.dtypes


# #### Combine the sales data by rows.

# In[35]:


# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.
combine_df = pd.concat([df_2020, df_2021], axis=0).reset_index()
combine_df


# In[36]:


# Check if any values are null.
combine_df.isnull().sum()


# In[37]:


# Check the data type of each column
combine_df.dtypes


# In[38]:


# Convert the "invoice_date" to a datetime datatype
combine_df["invoice_date"] = pd.to_datetime(combine_df["invoice_date"])


# In[39]:


# Confirm that the "invoice_date" data type has been changed.
combine_df.dtypes


# ### 2. Determine which Region Sold the Most Products

# #### Using `groupby`

# In[21]:


# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".
top_5_products = combine_df.groupby(["region", "state", "city"])[["units_sold"]].sum().sort_values("units_sold", ascending = False)

top_5_products.rename(columns = {"units_sold":'Total_Products_Sold'}, inplace = True)

# Show the top 5 results.
 
top_5_products.head(5)


# #### Using `pivot_table`

# In[56]:


# Show the number products sold for region, state, and city.
top_5_sold_pivot = pd.pivot_table(combine_df, index = ["region", "state", "city"], values="units_sold", aggfunc="sum")  
top_5_sold_pivot


top_5_sold_pivot.rename(columns={"units_sold":"Total_Products_Sold"}).sort_values("Total_Products_Sold", ascending = False).head(5)
# Rename the "units_sold" column to "Total_Products_Sold"
# Show the top 5 results.




# ### 3. Determine which Region had the Most Sales

# #### Using `groupby`

# In[24]:


# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.

top_5_sales = combine_df.groupby(["region", "state", "city"])[["total_sales"]].sum().\
sort_values("total_sales", ascending = False)

top_5_sales.rename(columns = {"total_sales":'Total Sales'}, inplace = True)

# Show the top 5 results.
 
top_5_sales.head(5)


# In[51]:


#### Using `pivot_table`


# In[61]:


# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"
# Show the top 5 results.
# Show the top 5 results.

combine_df_pivot = pd.pivot_table(combine_df, index=["region", "state", "city"], values="total_sales", aggfunc="sum")
combine_df_pivot
combine_df_pivot.rename(columns={"total_sales":'Total Sales'}).sort_values('Total Sales',ascending = False).head(5)


# 

# ### 4. Determine which Retailer had the Most Sales

# #### Using `groupby`

# In[67]:


# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"
top_5_sales_retailer = combine_df.groupby(["retailer","region", "state", "city"])[["total_sales"]].sum().\
sort_values("total_sales", ascending = False)
top_5_sales_retailer 
top_5_sales.rename(columns={"total_sales":"Total_Sales"}).head(5)
# Show the top 5 results.



# #### Using `pivot_table`

# In[68]:


# Show the total sales for the products sold for each retailer, region, state, and city.


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.

combine_df_pivot_retailer = pd.pivot_table(combine_df, index=["region", "state", "city","retailer"], values="total_sales", aggfunc="sum")
combine_df_pivot_retailer
combine_df_pivot_retailer.rename(columns={"total_sales":'Total Sales'}).sort_values('Total Sales',ascending = False).head(5)


# ### 5. Determine which Retailer Sold the Most Women's Athletic Footwear

# In[71]:


# Filter the sales data to get the women's athletic footwear sales data.
filter_df = combine_df.loc[(combine_df["product"] =="Women's Athletic Footwear")]
filter_df.head(5) 


# #### Using `groupby`

# In[73]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"

# Show the top 5 results.
filter_df_top_5 = filter_df.groupby(["retailer","region", "state", "city"])[["units_sold"]].sum().\
sort_values("units_sold", ascending = False)
filter_df_top_5 
filter_df_top_5.rename(columns={"units_sold":"Womens_Footwear_Units_Sold"}).head(5)


# #### Using `pivot_table`

# In[74]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.


# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"

# Show the top 5 results.

filter_df_top_5_pivot = pd.pivot_table(filter_df, index = ["retailer","region", "state", "city"], values="units_sold", aggfunc="sum")  
filter_df_top_5_pivot


filter_df_top_5_pivot.rename(columns={"units_sold":"Womens_Footwear_Units_Sold"}).sort_values("Womens_Footwear_Units_Sold", ascending = False).head(5)



# ### 5. Determine the Day with the Most Women's Athletic Footwear Sales

# In[76]:


# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the table.
filter_df_top_5_pivot = pd.pivot_table(filter_df, index = ["invoice_date"], values="total_sales", aggfunc="sum")  
filter_df_top_5_pivot


filter_df_top_5_pivot.rename(columns={"total_sales":"Total Sales"}).sort_values("Total Sales", ascending = False).head(5)



# In[82]:


# Resample the pivot table into daily bins, and get the total sales for each day.

daily_sales = filter_df_top_5_pivot.resample('D').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".




# daily_sales = pivot_table.resample('D').sum()

# Sort the resampled DataFrame in descending order to see the daily sales
daily_sales = daily_sales.sort_values(by='total_sales', ascending=False)

# Display the daily sales
daily_sales


# ### 6.  Determine the Week with the Most Women's Athletic Footwear Sales

# In[85]:


# Resample the pivot table into weekly bins, and get the total sales for each week.
weekly_sales = filter_df_top_5_pivot.resample('W').sum()
weekly_sales = weekly_sales.sort_values(by='total_sales', ascending=False)
# Sort the resampled pivot table in ascending order on "Total Sales".
weekly_sales


# In[ ]:




