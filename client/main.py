import urllib.request
import psycopg2
import json

with urllib.request.urlopen("http://localhost:1234/index.html") as fp:
    encodedContent = fp.read()
    decodedContent = encodedContent.decode("utf8")
    print(decodedContent)

with open("database_auth.json", "r") as json_db:
    print("Database login info added.")
    data = json.load(json_db)
    json_db.close()


print("Doing a request to the database.")
with psycopg2.connect(**data) as connection:
    main_cur = connection.cursor()
    main_cur.execute("SELECT * FROM phones;")
    rows = main_cur.fetchall()
    for row in rows:
        print(row)