import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS FiftyStateCoin ( '
          'id PRIMARY KEY AUTOINCREMENT, '
          'state VARCHAR(15), '
          'dateIssued INT(15), '
          'description VARCHAR(100), '
          'image VARCHAR(100)'
          )
