import os
import psycopg2
from dotenv import dotenv_values, load_dotenv
from pydantic import BaseModel
from logger_hand import logger

class User(BaseModel):
    id: int = None 
    name: str
    password: str

load_dotenv('.env.secret')

db_ip = 'postgres_database'
db_port = 5432
db_name = os.getenv('PG_DBNAME')
db_username = os.getenv('PG_USERNAME')
db_userpass = os.getenv('PG_USERPASS')

print(db_username)

#**connection_data
def database_request(request: str = None) -> list: # Database request with env variables
    with psycopg2.connect(host=db_ip, port=db_port, database=db_name, user=db_username, password=db_userpass) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
        columns = [elem[0] for elem in cursor.fetchall()] # Converting list[tuple] into list[]
        if request:
            cursor.execute(request)
            rows = [[elem for elem in row] for row in cursor.fetchall()] # Converting list[tuple] into list[list]'
            return [dict(zip(columns, row)) for row in rows] # Compared column to row result
    logger.info('DB request has been executed')
    return columns

def verify_logindata(userdata: User) -> bool:
    request = f"SELECT * FROM users as u WHERE u.login LIKE '{userdata.name}'"
    database_answer = database_request(request) 
    if len(database_answer) != 1: # Overflow or zero results 
        if len(database_answer) > 1: 
            logger.error('Too many identical users')
            for x in database_answer:
                logger.debug(x['id'])
        return False
    else:
        if any([elem['password'] == userdata.password for elem in database_answer]): 
            return True
        return False