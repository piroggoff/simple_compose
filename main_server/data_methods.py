import psycopg2
from dotenv import dotenv_values
import os
from pydantic import BaseModel

class User(BaseModel):
    id: int
    user: str
    password: str
    
connection_data = { #Dictionary with DB auth info (can be overrided with runtime values)
    #**os.environ
    **dotenv_values(".env.secret")
}

def database_request(request: str = None) -> list: #Database request with env variables
    with psycopg2.connect(**connection_data) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
        columns = [elem[0] for elem in cursor.fetchall()] #Converting list[tuple] into list[]
        cursor.execute(request)
        rows = [[elem for elem in row] for row in cursor.fetchall()] # Converting list[tuple] into list[list]'
    print([dict(zip(columns, row)) for row in rows])
    return [dict(zip(columns, row)) for row in rows]

def verify_logindata(login: str, password: str) -> bool:
    request = f"SELECT * FROM users as u WHERE u.login LIKE '{login}'"
    database_answer = database_request(request) 
    if len(database_answer) != 1: #Overflow or zero results 
        if len(database_answer) > 1: 
            print('Many identical users')
            for x in database_answer:
                print(x['id'])
        return False
    else:
        if any([elem['password'] == password for elem in database_answer]): 
            return True
        return False

#print(verify_logindata(login='Tarantino', password='skotina'))