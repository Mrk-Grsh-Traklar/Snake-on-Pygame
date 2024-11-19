from imp import * 

class DataBase:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name+".db")

    def create_trashtable(self, trashtable_name):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {trashtable_name}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                Category TEXT,
                name TEXT,
                cost INTEGER,
                nalichie INTEGER)
            """)
        
    def create_Profiletable(self, Profiletable_name):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {Profiletable_name}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                Category TEXT,
                name TEXT,
                cost INTEGER,
                nalichie INTEGER)
            """)
        
    def create_carttable(self, carttable_name):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {carttable_name}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                Category TEXT,
                name TEXT,
                cost INTEGER,
                nalichie INTEGER)
            """)

    def insert_data(self, table_name , *params):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"INSERT INTO {table_name} (Category, name, cost, nalichie) VALUES (?, ?, ?, ?)", params)
        self.con.commit()

    def select_data(self, table_name):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"SELECT name, cost FROM {table_name} ")
        items = self.con.fetchone()