import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('''CREATE TABLE FiftyStateCoin ( number  PRIMARY KEY ,  state Int , state String(50),YearIssued  Int(4) , discripption String , image String  ) ''')


 