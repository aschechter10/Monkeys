import sqlite3
#Make users table
db = sqlite3.connect("/var/www/FlaskApp/FlaskApp/story.db") #open db if file exists, otherwise create db
c = db.cursor()
try: c.execute("CREATE TABLE users(username TEXT, password TEXT, story_ids TEXT)")
except: pass
db.commit()
db.close()
