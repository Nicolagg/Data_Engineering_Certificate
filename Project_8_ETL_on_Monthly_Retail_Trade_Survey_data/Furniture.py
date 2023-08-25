import pandas as pd
import mysql.connector
import yaml 
import matplotlib.pyplot as plt



Kind_of_Business = 'Furniture, home furn, electronics, and appliance stores'

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
                SELECT DATE_FORMAT(data.date, '%m-%Y') AS month_year , data.Value
                FROM data
                LEFT JOIN category
                ON data.IDcat = category.ID
                WHERE category.Kind_of_Business LIKE '%{Kind_of_Business}';
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
    
month1,sales1 = valueKind_of_Business_by_year(Kind_of_Business)

# Convert the 'month' list to datetime format
month1 = pd.to_datetime(month1, format='%m-%Y')


#creat the datafram
df = pd.DataFrame((sales1),columns =['sales cat1'], index=month1)
df.index.name='date'

#preper the data
dfRolling1 = df.rolling(12).mean()
dfRolling2 = df.rolling(24).mean()




# Create a subplot with 2 row and 2 columns
fig, axs = plt.subplots(2, 1, figsize=(20, 10))


# Add a general title to the figure
fig.suptitle(f'Sales Analysis \n{Kind_of_Business}', fontsize=16)

# Plot each numeric column against the SalePrice column
axs[0].plot(month1,sales1, label=Kind_of_Business)
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Value')
axs[0].set_title('Sales')
axs[0].legend()


axs[1].plot(month1,dfRolling1['sales cat1'],label='rolling 12')
axs[1].plot(month1,dfRolling2['sales cat1'],label='rolling 24')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('%')
axs[1].set_title('Rolling Time Windows')
axs[1].legend()


fig.tight_layout()

plt.show()
