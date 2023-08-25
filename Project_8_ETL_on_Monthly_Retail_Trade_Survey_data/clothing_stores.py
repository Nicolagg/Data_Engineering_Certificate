cat1 = 'Men_s clothing stores'
cat2 = 'Women_s clothing stores'


import pandas as pd
import mysql.connector
import yaml 
import matplotlib.pyplot as plt

# define the name of the new database
newDb = 'mrts'

def valueKind_of_Business_DF(Kind_of_Business):
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
    WHERE category.Kind_of_Business LIKE '{Kind_of_Business}';
    """)
    cursor.execute(query)
    
    #creat the datafram with the result from the query
    df = pd.DataFrame(data=cursor.fetchall(), index=None)
    df.columns = ['date', 'sales']
    df['date'] = pd.to_datetime(df['date'], format='%m-%Y')
    df.set_index('date', inplace = True)
    
    # Close the cursor and connection to the database
    cursor.close()
    cnx.close()
    return df
    
df1 = valueKind_of_Business_DF(cat1)
df2 = valueKind_of_Business_DF(cat2)


df_combined = df1.join(df2, lsuffix=' Men_s', rsuffix=' Women_s')


# Replace missing values with the one-year moving average
rolling_mean  = df_combined.rolling(window=4, min_periods=1).mean()  # calulat the mean
df_combined.fillna(rolling_mean, inplace=True)  # Replace missing values with the moving average


#creat a new column with man an women's sale
df_combined['sales Men_s and Women'] = df_combined['sales Men_s'] + df_combined['sales Women_s']




#creat the datafram grouped by year
df_combined_Year = df_combined.groupby(pd.Grouper(freq='1Y')).agg({'sales Men_s and Women':'sum',
                                                                    'sales Men_s':'sum',
                                                                    'sales Women_s':'sum'})

#percentage of the market taken by women 
df_combined_Year['Women_p'] = (df_combined_Year['sales Women_s'] / df_combined_Year['sales Men_s and Women']) * 100


#calcul the percentage change
dfpercent  = df_combined_Year.pct_change()




#calcul the difference between men % and Women %
dfpercent['diff'] = dfpercent['sales Men_s'] - dfpercent['sales Women_s']


# Create a subplot with 2 row and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(20, 10))


# Add a general title to the figure
fig.suptitle(f'Sales Analysis of clothing stores', fontsize=16)

# Plot each numeric column against the SalePrice column
axs[0,0].plot(df_combined_Year.index,df_combined_Year['sales Women_s'], label='Women_s')
axs[0,0].plot(df_combined_Year.index,df_combined_Year['sales Men_s'], label='Men_s')
axs[0,0].set_xlabel('Year')
axs[0,0].set_ylabel('Value')
axs[0,0].set_title('Sales')
axs[0,0].legend()


axs[0,1].plot(dfpercent.index,dfpercent['sales Women_s'], label='Women_s')
axs[0,1].plot(dfpercent.index,dfpercent['sales Men_s'], label='Men_s')
axs[0,1].plot(dfpercent.index,dfpercent['sales Men_s and Women'], label='Men_s and Women')
axs[0,1].set_xlabel('Year')
axs[0,1].set_ylabel('%')
axs[0,1].set_title('Sales in percentage change')
axs[0,1].legend()




axs[1,0].plot(dfpercent.index,dfpercent['diff'], label='man and women variation')
axs[1,0].set_xlabel('Year')
axs[1,0].set_ylabel('%')
axs[1,0].set_title('variation in percentage change between man and woman')
axs[1,0].legend()

axs[1,1].plot(df_combined_Year.index,df_combined_Year['Women_p'], label='man and women variation')
axs[1,1].set_xlabel('Year')
axs[1,1].set_ylabel('%')
axs[1,1].set_title('Percentage of the sale taken by women ')
axs[1,1].legend()


fig.tight_layout()

plt.show()
