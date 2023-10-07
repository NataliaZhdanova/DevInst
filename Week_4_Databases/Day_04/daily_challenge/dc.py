# Using this REST Countries API, create the functionality which will write 10 random countries to your database.

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'devinst'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()

# Get data from the Countries API
def get_country_data() :
    import requests
    address = "https://restcountries.com/v3.1/all"
    response = requests.get(address)
    if response.status_code == 200 :
        return response.json()
    else :
        print("Failed to get data from the API.")

# Select 10 random countries
def get_rand_countries(country_data) :
    import random
    return random.sample(country_data, 10)

# Create a table for countries
def create_table(table_name: str): 
    query = f'CREATE TABLE {table_name}(country_id SERIAL PRIMARY KEY, name VARCHAR(255), capital VARCHAR(255), flag TEXT, subregion VARCHAR(255), population INT);'
    cursor.execute(query)
    connection.commit()

# Save countries to the DB
def save(countries):
    for country in countries:
        name = country['name']['common']
        capital = country['capital'][0] if 'capital' in country else "N/A"
        flag = country['flags']['png'] if 'flags' in country else "N/A"
        subregion = country['subregion'] if 'subregion' in country else "N/A"
        population = country['population'] if 'population' in country else 0
        query = f"INSERT INTO countries (name, capital, flag, subregion, population) VALUES ('{name}', '{capital}', '{flag}', '{subregion}', {population});"
        cursor.execute(query)
        connection.commit()

if __name__ == "__main__":

    country_data = get_country_data()
    countries = get_rand_countries(country_data)
#    print(countries)
#    create_table("countries")
    save(countries)
    connection.close()
