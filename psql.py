import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="ddpvc719dgt7in", user='hjnyzomiujedmc', password='5aa9fadeec66a3d3553ecb067a9d130657fd703703cbe9251fea443b442aaad4', host='ec2-176-34-211-0.eu-west-1.compute.amazonaws.com
', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP
);


#Closing the connection
conn.close()
Connection established to: (
   'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
)