import pandas as pd
import mysql.connector
import yaml 
import matplotlib.pyplot as plt



cat1 = 'Sporting goods stores'
cat2 = 'Hobby, toy, and game stores'
cat3 = 'Book stores'

# define the name of the new database
newDb = 'mrts'

def valueKind_of_Business_by_year(Kind_of_Business):
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
    # Close the cursor and connection to the database
    cursor.close()
    cnx.close()
    return month, sales
    
month1,sales1 = valueKind_of_Business_by_year(cat1)
month2,sales2 = valueKind_of_Business_by_year(cat2)
month3,sales3 = valueKind_of_Business_by_year(cat3)



print(len(month3))


# Convert the 'month' list to datetime format
month1 = pd.to_datetime(month1, format='%m-%Y')

#creat the datafram
df = pd.DataFrame(list(zip(sales1, sales2, sales3)),columns =['sales cat1', 'sales cat2', 'sales cat3'], index=month1)
df.index.name='date'

# Prepare data

#creat the datafram grouped by year
dfYear = df.groupby(pd.Grouper(freq='1Y')).agg({'sales cat1':'sum',
                                              'sales cat2':'sum',
                                              'sales cat3':'sum'})

# creat df with data between 2010 and 2021

df_filtered = df[ (df.index.year > 2010) & (df.index.year <= 2021)]

# creat df with data for 2020
df_filtered2 = df[ (df.index.year > 2019) & (df.index.year <= 2021)]


# Create a subplot with 1 row and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(20, 10))

# Add a general title to the figure
fig.suptitle(f'Sales Analysis', fontsize=16)

# Plot each numeric column against the SalePrice column
axs[0,0].plot(month1,df['sales cat1'],label=cat1)
axs[0,0].plot(month1,df['sales cat2'],label=cat2)
axs[0,0].plot(month1,df['sales cat3'],label=cat3)
axs[0,0].set_xlabel('month')
axs[0,0].set_ylabel('sales')
axs[0,0].set_title('Sales monthly value')
axs[0,0].legend()

axs[0,1].plot(dfYear.index,dfYear['sales cat1'], label=cat1)
axs[0,1].plot(dfYear.index,dfYear['sales cat2'], label=cat2)
axs[0,1].plot(dfYear.index,dfYear['sales cat3'], label=cat3)

axs[0,1].set_xlabel('year')
axs[0,1].set_ylabel('Value')
axs[0,1].set_title('Sales yearly value')
axs[0,1].legend()


# Plot each numeric column against the SalePrice column
axs[1,0].plot(df_filtered.index,df_filtered['sales cat1'],label=cat1)
axs[1,0].plot(df_filtered.index,df_filtered['sales cat2'],label=cat2)
axs[1,0].plot(df_filtered.index,df_filtered['sales cat3'],label=cat3)
axs[1,0].set_xlabel('month')
axs[1,0].set_ylabel('sales')
axs[1,0].set_title('Sales between 2010 and 2021')
axs[1,0].legend()

# Plot each numeric column against the SalePrice column
axs[1,1].plot(df_filtered2.index,df_filtered2['sales cat1'],label=cat1)
axs[1,1].plot(df_filtered2.index,df_filtered2['sales cat2'],label=cat2)
axs[1,1].plot(df_filtered2.index,df_filtered2['sales cat3'],label=cat3)
axs[1,1].set_xlabel('month')
axs[1,1].set_ylabel('sales')
axs[1,1].set_title('Sales in 2020')
axs[1,1].legend()

fig.tight_layout()

plt.show()
