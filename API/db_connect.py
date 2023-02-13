import sqlite3
import os

# https://docs.sqlalchemy.org/en/20/


class DB:
    db_url: str

    def __init__(self, db_url: str): # här är tanken att denna ska leda till vår databas.  
        self.db_url = db_url                                                                       
        if not os.path.exists(self.db_url):
            self.__set_up_db()  

    # def __set_up_db(self):
    #     conn = sqlite3.connect(self.db_url)
    #     with open(
    #         "C:\Users\Bananberg\Desktop\Python_ass\API/Agents.db", "r"
    #     ) as file:
    #         script = file.read()
    #         conn.executescript(script)
    #         conn.commit()
    #     conn.close()


    def __call_db(self, query):                                                         
            connection = sqlite3.connect(self.db_url)                                              
            cursor = connection.cursor()                                         
            res = cursor.execute(query)           
            data = res.fetchall()                                
            cursor.close                                    
            connection.commit()                                                                         
            connection.close()                                                                  
            return data              


