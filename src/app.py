

# 1) Connect to the database here using the SQLAlchemy's create_engine function

import psycopg2 

# conn = psycopg2.connect(database= 'dbbrcaul824pb1', 
#                         user = 'mpwokhuooltjif',
#                         password= 'ba9d873587309936d8b576da5a5ec7b424fb919400fb3d839a80383e9e00fb98',
#                         host = 'ec2-52-72-56-59.compute-1.amazonaws.com',
#                         port = 5432)

# conn.close()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# conn = psycopg2.connect(database= 'dbbrcaul824pb1', 
#                         user = 'mpwokhuooltjif',
#                         password= 'ba9d873587309936d8b576da5a5ec7b424fb919400fb3d839a80383e9e00fb98',
#                         host = 'ec2-52-72-56-59.compute-1.amazonaws.com',
#                         port = 5432)

# cursor = conn.cursor()
# cursor.execute("CREATE TABLE Movies(id VARCHAR(2) PRIMARY KEY, title VARCHAR(30), rating INT);")
# conn.commit()
# conn.close()


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# conn = psycopg2.connect(database= 'dbbrcaul824pb1', 
#                         user = 'mpwokhuooltjif',
#                         password= 'ba9d873587309936d8b576da5a5ec7b424fb919400fb3d839a80383e9e00fb98',
#                         host = 'ec2-52-72-56-59.compute-1.amazonaws.com',
#                         port = 5432)

# cursor = conn.cursor()
# cursor.execute("INSERT INTO Movies(id,title,rating) VALUES ('1','Toy Story 3',3), ('2','Harry Potter',5);")
# conn.commit()
# conn.close()

# 4) Use pandas to print one of the tables as dataframes using read_sql function
import pandas as pd

conn = psycopg2.connect(database= 'dbbrcaul824pb1', 
                        user = 'mpwokhuooltjif',
                        password= 'ba9d873587309936d8b576da5a5ec7b424fb919400fb3d839a80383e9e00fb98',
                        host = 'ec2-52-72-56-59.compute-1.amazonaws.com',
                        port = 5432)

df = pd.read_sql('SELECT * FROM Movies', conn)
conn.close()

print(df)

