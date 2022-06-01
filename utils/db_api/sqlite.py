import sqlite3


class Database:
    def __init__(self, path_to_db="main2.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Sana varchar(12),
            Viloyat varchar(50),
            Tuman varchar(70),
            mahalla varchar(255),
            work_place varchar(255),
            telephone varchar(20),
            score int,
            status varchar(500),
            date varchar(50),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, sana: str=None, viloyat: str=None, tuman: str=None, mahalla: str=None,
                 work_place: str=None, telephone: str=None, score: int=None, status: str=None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        status = "0"
        score = "0"
        sql = """
        INSERT INTO Users(id, Name, Sana, Viloyat, Tuman, mahalla, work_place, telephone, score, status) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, sana, viloyat, tuman, mahalla, work_place, telephone, score, status),
                     commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_user_by_id(self, id):
        sql = """
        SELECT * FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_Name(self, id, new_name):
        sql = f"""
        UPDATE Users SET NAME=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_name, id,), commit=True)

    def update_user_sana(self, id, new_sana):
        sql = f"""
        UPDATE Users SET Sana=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_sana, id,), commit=True)

    def update_user_viloyat(self, id, new_viloyat):
        sql = f"""
        UPDATE Users SET Viloyat=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_viloyat, id,), commit=True)

    def update_user_tuman(self, id, new_tuman):
        sql = f"""
        UPDATE Users SET Tuman=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_tuman, id,), commit=True)

    def update_user_mahalla(self, id, new_mahalla):
        sql = f"""
        UPDATE Users SET mahalla=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_mahalla, id,), commit=True)

    def update_user_work_place(self, id, new_work_place):
        sql = f"""
        UPDATE Users SET work_place=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_work_place, id,), commit=True)

    def update_user_telephone(self, id, new_telephone):
        sql = f"""
        UPDATE Users SET telephone=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_telephone, id,), commit=True)


    def update_user_score(self, id, new_score):
        sql = f"""
        UPDATE Users SET score=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_score, id,), commit=True)

    def update_user_status(self, id, new_status):
        sql = f"""
        UPDATE Users SET status=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_status, id,), commit=True)

    def update_user_date(self, id, new_date):
        sql = f"""
        UPDATE Users SET date=? WHERE id=?
        """
        return self.execute(sql, parameters=(new_date, id,), commit=True)

    def dalete_user_by_id(self, id):
        sql = """
        DELETE FROM Users WHERE id=?
        """
        self.execute(sql, parameters=(id,), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def admin(self):
        sql = """
        update Users set status=0 where id=928883166;
        """
        self.execute(sql, commit=True)
