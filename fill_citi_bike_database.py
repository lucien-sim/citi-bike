
# coding: utf-8

# # Initialize and populate citi_bike SQL database

# In[1]:


import pandas as pd
import os
import pickle
data_path = './data'


# # 1. Create the database, create a table to hold data
# * DATABASE NAME: 'citi_bike'
# * TABLE NAME: 'dock_counts'

# In[2]:


# Connect to database with sqlalchemy package. 
import mysql.connector
import sqlalchemy
from external_variables import sql_un,sql_pwd
database_username = sql_un
database_password = sql_pwd
database_ip       = 'localhost'
conn_alchemy      = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}'.
                                             format(database_username, database_password, 
                                                    database_ip)).connect()

# Create database, create table. If database already exists, means we've already created it. 
# Instead of raising an error, we'll switch into database and move on. 
trans = conn_alchemy.begin()
try:
    r1=conn_alchemy.execute("CREATE DATABASE citi_bike")
    r2=conn_alchemy.execute("USE citi_bike")
    r3=conn_alchemy.execute("""
                            CREATE TABLE dock_counts
                            (
                                row_id INT NOT NULL AUTO_INCREMENT,
                                dock_id INT NOT NULL,
                                date_time DATETIME NOT NULL,
                                avail_bikes INT,
                                avail_docks INT,
                                tot_docks INT,
                                in_service INT,
                                status_key INT,
                                PRIMARY KEY (row_id)
                            );
                            """)
    trans.commit()
    
except:
    r2=conn_alchemy.execute("USE citi_bike")
    trans.commit()
    
    


# # 2. Fill the database with station count data
# The cell below accomplishes two important tasks: 
# * Add data to the dock_counts table in the citi_bike database, using pandas to_sql function. For each dock/time for which data is available, I save:  
#     * dock_id: ID's the CitiBike dock station
#     * date_time: timestamp--derived from info in the count .csv files using the function: 'create_timestamp_citibike'
#     * avail_bikes: number of bikes available at the dock station
#     * avail_docks: number of docks available at the dock station
#     * tot_docks: total number of docks at the dock station
#     * in_service: indicates whether the dock station is in service (1 = yes)
#     * status_key: not sure what this means so I saved it
# * Store information on all the docks in dock_dict. In dock_dict, keys are str(dock_id), entries are separate dicts that hold the full name, latitude, and longitude of each dock. I'll need all this information for mapping, but don't want to store it millions of times in the database. 

# In[3]:


def create_timestamp_citibike(orig_date,orig_hr,orig_min,pm): 
    # Year, month, day
    year = int(orig_date[0:2])+2000
    month = int(orig_date[3:5])
    day = int(orig_date[6:8])
    # Hour, minute, second
    if pm == 1 and orig_hr != 12: 
        hour = orig_hr+12
    elif pm == 0 and orig_hr == 12: 
        hour = 0
    else: 
        hour = orig_hr
    minute = orig_min
    second = 0
    return pd.Timestamp(year=year,month=month,day=day,hour=hour,minute=minute,second=second)

count_fnames = sorted(os.listdir(os.path.join(data_path,'dock_counts')))
dock_dict = {}
dtypes = {'dock_id': int, 'dock_name': str, 'date': str, 'hour': int, 'minute': int, 'pm': int, 
          'avail_bikes': int, 'avail_docks': int, 'tot_docks': int, '_lat': float, 
          '_long': float, 'in_service': int, 'status_key': int}

for fname in count_fnames: 
    
    fpathname = os.path.join(data_path,'dock_counts',fname)
    
    # Skip 2015 -> there are issues with these files; I'll come back to them later. 
    if fpathname[-11:-7] != '2018':
        continue
        
    print(fpathname)
    
    # Read dock counts from csv in chunks
    for monthly_data in pd.read_csv(fpathname,sep='\t',dtype=dtypes,usecols=list(range(0,13)),chunksize=10**4):
    
        # Create single timestamp column
        monthly_data['date_time'] = [create_timestamp_citibike(row['date'],row['hour'],row['minute'],row['pm']) for _,row in monthly_data.iterrows()]

        # Add any new docks to dock_dict
        unique_docks = monthly_data['dock_id'].unique()
        for dock in unique_docks: 
            if str(dock) not in dock_dict.keys():
                row = monthly_data.loc[monthly_data['dock_id'] == dock].iloc[0,:]
                dock_dict[str(row['dock_id'])] = {'dock_name': row['dock_name'], 'lat': row['_lat'], 'lon': row['_long']}

        # Keep only needed columns
        col_names = ['dock_id','date_time','avail_bikes','avail_docks','tot_docks','in_service','status_key']
        monthly_data = monthly_data[col_names]

        # Add to SQL database table...
        try: 
            monthly_data.to_sql(name='dock_counts',con=conn_alchemy,if_exists='append',index=False)
        except: 
            print('Issue adding dock_count data to database table.')
            raise
        
    # Save dock_dict after completing each file -> in case the system crashes. 
    from general_functions import save_pkl
    save_pkl(os.path.join(data_path,'dock_dict.pkl'),dock_dict)
        
# Close database connection. 
conn_alchemy.close()


# In[13]:


# Separately create dictionary of dock_id -> dock_name, lat, lon. 

#count_fnames = os.listdir(os.path.join(data_path,'dock_counts'))
#dock_dict = {}
#use_cols = ['dock_id','dock_name','_lat','_long']
#dtypes = str #{'dock_id': int, 'dock_name': str, '_lat': float, '_long': float}
#
#for fname in count_fnames[12:]: 
#    
#    fpathname = os.path.join(data_path,'dock_counts',fname)
#    
#    year = print(fpathname[-11:-7])
#    if year == '2015':
#        continue
#    
#    print(fpathname)
#    
#    # Read dock counts from csv in chunks
#    for monthly_data in pd.read_csv(fpathname,sep='\t',dtype=dtypes,usecols=use_cols,chunksize=10**4):
#        
#        # Add any new docks to dock_dict
#        unique_docks = monthly_data['dock_id'].unique()
#        for dock in unique_docks: 
#            if str(dock) not in dock_dict.keys():
#                row = monthly_data.loc[monthly_data['dock_id'] == dock].iloc[0,:]
#                dock_dict[str(row['dock_id'])] = {'dock_name': row['dock_name'], 'lat': row['_lat'], 'lon': row['_long']}
#                
#    # Save dock_dict after completing each file -> in case the system crashes. 
#    from general_functions import save_pkl
#    save_pkl(os.path.join(data_path,'dock_dict.pkl'),dock_dict)

