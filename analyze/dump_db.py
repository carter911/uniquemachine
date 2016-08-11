#!/usr/bin/env python

import MySQLdb

db_name = "cross_browser"
table_name = "round_3_data"

db = MySQLdb.connect("localhost", "", "", db_name)
cursor = db.cursor()

cursor.execute("SELECT DISTINCT(user_id) FROM {}".format(table_name))
uids = [x for x, in cursor.fetchall()]
f = open("hashes.txt", "w")
for uid in uids:
  cursor.execute("SELECT browser, hashes FROM {} where user_id='{}' and gpu!='SwiftShader' and gpu!='Microsoft Basic Render Driver'".format(table_name, uid))
  data = cursor.fetchall()
  f.write("{}\n".format(len(data)))
  for browser, h in data:
    hashes = h.split("&")[:27]
    f.write(("{} " * (1 + len(hashes))).format(browser, *hashes))
    f.write("\n")

f.flush()
f.close()
db.close()
