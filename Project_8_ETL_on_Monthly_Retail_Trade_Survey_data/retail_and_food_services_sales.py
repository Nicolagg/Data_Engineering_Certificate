import pandas as pd
import yaml 
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import matplotlib as mpl

# define the name of the new database
newDb = 'mrts'


# define category to import
Kind_of_Business = 'Retail and food services sales, total'


with open('connection.yaml', 'r') as f:
    connection = yaml.safe_load(f)
    
    
# establish a connection to the MySQL database
cnx = mysql.connector.connect(**connection, database = newDb)    

# create a cursor object to execute SQL queries
cursor = cnx.cursor()


query = (f"""
SELECT date_format(data.date, '%m-%Y') as month, data.Value   
FROM data
LEFT JOIN category 
ON data.IDcat = category.ID 
WHERE category.Kind_of_Business = '{Kind_of_Business}';
""")
         
cursor.execute(query)


month = []
sales = []

         
         
         
for row in cursor.fetchall():
    month.append(row[0])
    sales.append(row[1])
    


query2 = (f"""
SELECT YEAR(data.date) as Year, SUM(data.Value) as Total_Value 
FROM data
LEFT JOIN category
ON data.IDcat = category.ID
WHERE category.Kind_of_Business = '{Kind_of_Business}'
GROUP BY YEAR(data.date);
""")

cursor.execute(query2)

# Close the cursor and connection to the database

Year = []
Ysales = []     
         
         
for row in cursor.fetchall():
    Year.append(row[0])
    Ysales.append(row[1])

cursor.close()
cnx.close()


# Create a subplot with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Add a general title to the figure
fig.suptitle(f'Sales Analysis for : {Kind_of_Business}', fontsize=16)

# Plot each numeric column against the SalePrice column

axs[0].plot(month, sales)
axs[0].set_xlabel('month')
axs[0].set_ylabel('sales')
axs[0].set_title('month vs. sales')

axs[1].plot(Year, Ysales)
axs[1].set_xlabel('year')
axs[1].set_ylabel('sale')
axs[1].set_title('Year vs. sale')
plt.show()


# Convert the 'month' list to datetime format
month = pd.to_datetime(month, format='%m-%Y')

# Create the DataFrame with the 'date' column as index
df = pd.DataFrame({'sales': sales}, index=month, columns=['sales'])
# Prepare data

#############################################
# the code below was copied and adapted from
# Selva Prabhakaran (February 13, 2019). Seasonal Plot of a Time Series. machinelearningplus.com https://www.machinelearningplus.com/time-series/time-series-analysis-python/


# Prepare data
df['year'] = [d.year for d in df.index]
df['month'] = [d.strftime('%b') for d in df.index]
years = df['year'].unique()

# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# Draw Plot
plt.figure(figsize=(16,16), dpi= 80)
for i, y in enumerate(years):
    if i > 0:        
        plt.plot('month', 'sales', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'sales'][-1:].values[0], y, fontsize=12, color=mycolors[i])

# Decoration

plt.title(f'{Kind_of_Business}', fontsize=20)
plt.show()

##############################################################