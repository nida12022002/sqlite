from multiprocessing import connection
import sqlite3


connection = sqlite3.connect('test.db')

c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS FILMS(MOVIE_NAME TEXT NOT NULL,
   ACTOR TEXT NOT NULL,
   ACTRESS TEXT NOT NULL,
   RELEASE_DATE INT NOT NULL,
   DIRECTOR TEXT NOT NULL)""")

#c.execute("INSERT INTO FILMS VALUES('PUSHPA:THE RISE', 'ALLU ARJUN', 'RASHMIKA MANDANNA', '17-12-2021', 'SUKUMAR')")
c.execute("INSERT INTO FILMS VALUES('BAHUBALI 1', 'PRABHAS', 'TAMANNAAH', '10-07-2015', 'S.S.RAJAMOLI')")
c.execute("SELECT * FROM FILMS")
print(c.fetchall())
connection.commit()

connection.close()