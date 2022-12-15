import sqlite3
'''
Author: Jesse Greenlee

This contains database access/update function. The caller will connect to the golfer_db (golfer table) 
by calling connect_database(). Then, the database accessible to insert/update/delete. Then caller must close
by calling close_database

'''

class Golfer_Database:
    def __init__(self):
        self.conn = None

    # if you call this, the caller must call close_database after the sql execution
    def connect_database(self):
        try:
            self.conn = sqlite3.connect('golfer_db.db')
            cur = self.conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS golfers (
                                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                        first_name TEXT,
                                                        last_name TEXT, 
                                                        driver INT, 
                                                        three_wood INT, 
                                                        hybrid INT, 
                                                        five_iron INT,
                                                        six_iron INT, 
                                                        seven_iron INT, 
                                                        eight_iron INT, 
                                                        nine_iron INT, 
                                                        p_wedge INT, 
                                                        s_wedge INT,
                                                        l_wedge INT
                                                        );
                                                    ''')
            return cur
        except Exception as e:
            print('Error thrown during display_table', e)
            return None

    # close the golfer database
    def close_database(self):
        if self.conn:
            self.conn.close()

    # add data to the golf table
    def insert(self, player):
        if player.f_name == '' and player.l_name == '':
            print('Empty data: No data is inserted')
            return
        cur = self.connect_database()
        sql = 'INSERT INTO golfers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(sql, (None, player.f_name, player.l_name, player.driver, player.three_wood, player.hybrid, player.five_iron, player.six_iron, player.seven_iron, player.eight_iron, player.nine_iron,  player.p_wedge, player.s_wedge, player.l_wedge ))
        self.conn.commit()

    def get_all_data(self):
        rows = []
        try:
            sql = 'SELECT * FROM golfers'
            cur = self.connect_database()
            cur.execute(sql)
            data = cur.fetchall()
            for d in data:
                rows.append(d)
        except Exception as e:
            print('Error thrown during display_table', e)
        # print(rows)
        return rows

    def update(self, player):
        if player.f_name != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET first_name = ?  WHERE id = ?'
            #sql = '''UPDATE golfers SET first_name = ?, last_name = ?, driver = ?, three_wood = ?, hybrid = ?, five_iron = ?, six_iron = ?, seven_iron = ?, eight_iron = ?, nine_iron = ?, p_wedge = ?, s_wedge = ?  WHERE id = ?'''
            cur.execute(sql, (player.f_name, player.golfer_id))
            #cur.execute(sql, (player.f_name, player.l_name, player.driver, player.three_wood, player.hybrid, player.five_iron, player.six_iron, player.seven_iron, player.eight_iron, player.nine_iron,  player.p_wedge, player.s_wedge, player.golfer_id))
            self.conn.commit()
        if player.l_name != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET last_name = ?  WHERE id = ?'
            cur.execute(sql, (player.l_name, player.golfer_id))
            self.conn.commit()
        if player.driver != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET driver = ?  WHERE id = ?'
            cur.execute(sql, (player.driver, player.golfer_id))
            self.conn.commit()
        if player.three_wood != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET three_wood = ?  WHERE id = ?'
            cur.execute(sql, (player.three_wood, player.golfer_id))
            self.conn.commit()
        if player.hybrid != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET hybrid = ?  WHERE id = ?'
            cur.execute(sql, (player.hybrid, player.golfer_id))
            self.conn.commit()
        if player.five_iron != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET five_iron = ?  WHERE id = ?'
            cur.execute(sql, (player.five_iron, player.golfer_id))
            self.conn.commit()
        if player.six_iron != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET six_iron = ?  WHERE id = ?'
            cur.execute(sql, (player.six_iron, player.golfer_id))
            self.conn.commit()
        if player.seven_iron != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET seven_iron = ?  WHERE id = ?'
            cur.execute(sql, (player.seven_iron, player.golfer_id))
            self.conn.commit()
        if player.eight_iron != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET eight_iron = ?  WHERE id = ?'
            cur.execute(sql, (player.eight_iron, player.golfer_id))
            self.conn.commit()
        if player.nine_iron != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET nine_iron = ?  WHERE id = ?'
            cur.execute(sql, (player.nine_iron, player.golfer_id))
            self.conn.commit()
        if player.p_wedge != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET p_wedge = ?  WHERE id = ?'
            cur.execute(sql, (player.p_wedge, player.golfer_id))
            self.conn.commit()
        if player.s_wedge != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET s_wedge = ?  WHERE id = ?'
            cur.execute(sql, (player.s_wedge, player.golfer_id))
            self.conn.commit()
        if player.l_wedge != '':
            cur = self.connect_database()
            sql = 'UPDATE golfers SET l_wedge = ?  WHERE id = ?'
            cur.execute(sql, (player.l_wedge, player.golfer_id))
            self.conn.commit()

    # Create a method of searching for a record
    def search(self, player):
        query_res = []
        if player == '':
            print('No record was searched for')
            return
        cur = self.connect_database()
        if player.isnumeric():
            sql = 'SELECT * FROM golfers WHERE id = ?'
            cur.execute(sql, (player))
            data = cur.fetchall()
            for d in data:
                query_res.append(d)
                print(query_res)
                return query_res
        else:
            sql = 'SELECT * FROM golfers WHERE first_name = ?'
            cur.execute(sql, [player])
            data = cur.fetchall()
            for d in data:
                query_res.append(d)
                print(query_res)
                return query_res

    # Create a method to remove a record
    def remove(self, player):
        cur = self.connect_database()
        sql = 'DELETE FROM golfers WHERE id = ?'
        cur.execute(sql, (player))
        self.conn.commit()

