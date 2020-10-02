import sqlite3
from datetime import datetime
import random
import zlib

connection = sqlite3.connect("pfdb.db")
# print(connection.total_changes)
cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")
# cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
# cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)
# print("------")
# target_fish_name = "Jamie"
# rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = ?", (target_fish_name,),).fetchall()

# cursor.execute("ALTER TABLE PF_sources ADD sourcename TEXT;")

# rows = cursor.execute("SELECT submissionID, crc32, sourceID, datetime, storingDone, content FROM PF_submissions").fetchall()
# print(rows)

tstmp = datetime.timestamp(datetime.now())
cont = random.randrange(42, 1337, 3)
csum = hex(zlib.crc32(str.encode(str(cont))) & 0xffffff)
sauce = 3
subid = cursor.execute("SELECT submissionID from PF_submissions order by ROWID DESC limit 1").fetchone()[0] + 1


execstr = f"INSERT INTO PF_submissions VALUES({subid}, {csum}, {sauce}, {tstmp}, false, {cont})"
cursor.execute(execstr)
connection.commit()
