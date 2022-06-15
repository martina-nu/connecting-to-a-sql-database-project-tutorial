

# 1) Connect to the database here using the SQLAlchemy's create_engine function

import psycopg2
import os 
from dotenv import load_dotenv, find_dotenv


# load_dotenv(find_dotenv())  
# conn = psycopg2.connect(database = os.getenv("database"),                                      
#                         user = os.getenv("user"),                                  
#                         password = os.getenv("password"),                                            
#                         host = os.getenv("host"),                                          
#                         port = os.getenv("port"))


# conn.close()

# # 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# load_dotenv(find_dotenv())  
# conn = psycopg2.connect(database = os.getenv("database"),                                      
#                         user = os.getenv("user"),                                  
#                         password = os.getenv("password"),                                            
#                         host = os.getenv("host"),                                          
#                         port = os.getenv("port"))


# cursor = conn.cursor()
# cursor.execute("CREATE TABLE Movies(id VARCHAR(2) PRIMARY KEY, title VARCHAR(30), rating INT);")
# conn.commit()
# conn.close()


# # 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# load_dotenv(find_dotenv())  
# conn = psycopg2.connect(database = os.getenv("database"),                                      
#                         user = os.getenv("user"),                                  
#                         password = os.getenv("password"),                                            
#                         host = os.getenv("host"),                                          
#                         port = os.getenv("port"))

# cursor = conn.cursor()
# cursor.execute("INSERT INTO Movies(id,title,rating) VALUES ('1','Toy Story 3',3), ('2','Harry Potter',5);")
# conn.commit()
# conn.close()

# # 4) Use pandas to print one of the tables as dataframes using read_sql function

import pandas as pd

load_dotenv(find_dotenv())  
conn = psycopg2.connect(database = os.getenv("database"),                                      
                        user = os.getenv("user"),                                  
                        password = os.getenv("password"),                                            
                        host = os.getenv("host"),                                          
                        port = os.getenv("port"))

df = pd.read_sql('SELECT * FROM Movies', conn)
conn.close()

print(df)

