from sqlite3 import connect
from random import randrange
from zlib import crc32
from datetime import datetime


con = connect("pfdb.db")
cursor = con.cursor()

newID = cursor.execute("SELECT submissionID FROM PF_submissions order by ROWID DESC limit 1").fetchone()[0] + 1
content = randrange(11, 234235)
crc = crc32(str.encode(str(content)))
stamp = datetime.timestamp(datetime.now())

execstring = f'INSERT INTO PF_submissions VALUES({newID}, {crc}, 3, {stamp}, false, {content})'

print(cursor.execute("SELECT * FROM PF_submissions").fetchall())
cursor.execute(execstring)
con.commit()
print(cursor.execute("SELECT * FROM PF_submissions").fetchall())
