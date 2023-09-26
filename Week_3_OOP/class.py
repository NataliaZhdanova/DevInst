from datetime import date

birth_date = input("What is your birth date (YYYY-MM-DD)? ")

birth = date.fromisoformat(birth_date)
today = date.today()
delta = today - birth
years = delta.days // 365
years_str = str(years)
year_last_num = int(years_str[-1])
candles = "i" * year_last_num

print(f'''
       ___{candles}___
      |{" "*((year_last_num // 2) - 3)}:H:a:p:p:y:{" "*((year_last_num // 2) - 2)}|
    __|____{"_"*(year_last_num - 3)}______|__
   |^^^^^^^^{"^"*(year_last_num - 3)}^^^^^^^^|
   |{" "*((year_last_num // 2) - 3)}:B:i:r:t:h:d:a:y:{" "*((year_last_num // 2) - 2)}|
   |       {" "*(year_last_num - 3)}         |
   ~~~~~~~{"~"*(year_last_num - 3)}~~~~~~~~~~~    
      
    ''')


if birth.year % 4 == 0 :
    print(f'''\n
       ___{"i"*years}___
      |{" "*((years // 2) - 3)}:H:a:p:p:y:{" "*((years // 2) - 2)}|
    __|____{"_"*(years - 4)}______|__
   |^^^^^^^^{"^"*(years - 4)}^^^^^^^^|
   |{" "*((years // 2) - 3)}:B:i:r:t:h:d:a:y:{" "*((years // 2) - 2)}|
   |       {" "*(years - 4)}         |
   ~~~~~~~{"~"*(years - 4)}~~~~~~~~~~~    
      
    ''')




# a = "agsgfaaailkfsdjglaUHJMMDDAA"
# max(a)
# min(a)
# a.count("a")
# sorted(a)


# b = "Hello, World!"  
# print(b[-5:-2])

# # You can also specify how many characters to skip: 

# print(b[0:-1:2])
# b.replace("H","M")
# print(b)





# import psycopg2
# import psycopg2.extras

# DB_NAME = "dvdrental"
# USER = "postgres"
# PASSWORD = "postgres"
# HOST = "localhost"
# PORT = "5432"

# try:
#     connection = psycopg2.connect(
#         dbname = DB_NAME,
#         user = USER,
#         password = PASSWORD,
#         host = HOST,
#         port = PORT
#     )
# except Exception as e:
#     print(f"Error: {e}")

# cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# # query = '''
# # CREATE TABLE new_table_01(
# #     id serial PRIMARY KEY,
# #     num integer NOT NULL
# # );
# # '''

# # cursor.execute(query) # executes the query
# # connection.commit() # makes changes in the db

# table_name = 'actor'
# query = f'''
# SELECT * FROM {table_name} LIMIT 10;
# '''

# cursor.execute(query)
# output = cursor.fetchall()

# print(output)


# # table_name = 'new_table3'
# # rows = select_all(table_name)
# # first_row = rows[0]

# # print(first_row['id']) # >> 1
# # print(first_row['num']) # >> 12312