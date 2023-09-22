sent_input = input("Enter the longest sentence you can without the letter 'a': \n")
sent_length = int()
while 'quit' not in sent_input:    
    if 'a' not in sent_input :
        sent_input_check = sent_input
        if sent_length < len(sent_input_check) :
            sent_length = len(sent_input_check)
            print("Congrats! Your sentence is longer than the previous one!")
            sent_input = input("Enter the longest sentence you can without the letter 'a', or type 'quit': \n")
            
        else :
            print("Oops! Your sentence is not longer than the previous one!")
            sent_input = input("Enter the longest sentence you can without the letter 'a', or type 'quit': \n")

    else :
        print("No letter 'a', remember?")
        sent_input = input("Enter the longest sentence you can without the letter 'a', or type 'quit': \n")



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