import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS studentreg(
            id Integer Primary Key,
            studentnumber VARCHAR,
            name VARCHAR,
            sex VARCHAR,
            yearlevel VARCHAR,
            sports VARCHAR
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, studentnumber, name, sex, yearlevel, sports):
        self.cur.execute("insert into studentreg values (NULL,?,?,?,?,?)",
                         (studentnumber, name, sex, yearlevel, sports))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from studentreg")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from studentreg where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, studentnumber, name, sex, yearlevel, sports):
        self.cur.execute(
            "update studentreg set studentnumber=?, name=?, sex=?, yearlevel=?, sports=? where id=?",
            (studentnumber, name, sex, yearlevel, sports, id))
        self.con.commit()

    def search(self, studentnumber, name, sex, yearlevel, sports):
        self.cur.execute("SELECT * FROM studentreg WHERE studentnumber=? OR name=? OR sex=? OR yearlevel=? OR sports =?",
                         (studentnumber, name, sex, yearlevel, sports))
        rows = self.cur.fetchall()
        self.con.commit()
        return rows
