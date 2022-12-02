# id | name | description | price | photo | memory | color |brand | call_back | url
 
from db import conn, cursor

def create_table_product():
    query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            description TEXT,
            price INT,
            photo VARCHAR,
            memory VARCHAR,
            color VARCHAR,
            brand VARCHAR,
            call_back VARCHAR,
            url VARCHAR);"""
    cursor.execute(query=query)
    conn.commit()
    
def insert_product(name: str, 
                  description: str, 
                  price: int, 
                  photo: str, 
                  memory: str,
                  color: str, 
                  brand: str, 
                  call_back: str,
                  url: str):
    query = f"""
        INSERT INTO products (
            name, description, price, photo, memory, color, brand, call_back, url
        )VALUES (
            '{name}', '{description}', {price}, '{photo}', '{memory}', '{color}', '{brand}', '{call_back}', '{url}'
        );"""
    cursor.execute(query=query)
    conn.commit()


