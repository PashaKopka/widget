import pymysql

from widget.settings import DB_CONFIG


class DBWorker:

    def __init__(self,
                 username=DB_CONFIG['username'],
                 password=DB_CONFIG['password'],
                 db_name=DB_CONFIG['database_name'],
                 host=DB_CONFIG['host']
                 ):
        """
        Initializing database connection and cursor
        :param username: username of database
        :param password: password of database user
        :param db_name: name of your database
        :param host: host of database
        """
        self.username = username
        self.password = password
        self.db_name = db_name
        self.host = host

    def add_row(self, filename: str, path: str) -> None:
        """
        This function adding row in select table
        :param filename: name of py-file with Ui_Form
        :param path: path to py-file with Ui_Form file
        :return: None
        """
        if self.check_for_existing(filename, path):
            return
        query = 'INSERT INTO `user_widgets_table` (`filename`, `path`) VALUES (%s, %s)'
        self.__call_cursor(query, (filename, path))
        self.connection.commit()

    def get_rows(self) -> list:
        """
        This function return
        :return: None
        """
        self.__call_cursor('SELECT * FROM user_widgets_table')
        data = self.prepare_data(self.cursor.fetchall())
        return data

    def check_for_existing(self, filename: str, path: str) -> bool:
        """
        This function check if row exist in database
        :param filename: name of py-file
        :param path: path to this file
        :return: None
        """
        rows = self.get_rows()
        exist = False
        for row in rows:
            if filename == row['filename'] and path == row['path'] and row['del'] == 0:
                exist = True

        return exist

    def delete_row(self, filename: str) -> None:
        """
        This function set del = 1 where is filename
        :param filename: py-file name
        :return: None
        """
        self.__call_cursor(f'UPDATE user_widgets_table SET del=1 WHERE filename="{filename}"')

    def toggle_visibility(self, filename: str) -> None:
        """
        This function toggle visibility value in database (1/0)
        :param filename: py-file name
        :return: None
        """
        self.__call_cursor(f'SELECT visible FROM user_widgets_table WHERE filename="{filename}"')
        visibility = self.cursor.fetchall()[0][0]
        if visibility:
            self.__call_cursor(f'UPDATE user_widgets_table SET visible=0 WHERE filename="{filename}"')
        else:
            self.__call_cursor(f'UPDATE user_widgets_table SET visible=1 WHERE filename="{filename}"')

    def toggle_pinned_value(self, filename: str) -> None:
        self.__call_cursor(f'SELECT pinned FROM user_widgets_table WHERE filename="{filename}"')
        pinned = self.cursor.fetchall()[0][0]
        if pinned:
            self.__call_cursor(f'UPDATE user_widgets_table SET pinned=0 WHERE filename="{filename}"')
        else:
            self.__call_cursor(f'UPDATE user_widgets_table SET pinned=1 WHERE filename="{filename}"')

    def add_coordinate(self, filename: str, x, y) -> None:
        """
        This function update value of x and y coordinates of widget
        :param filename: py-file name
        :param x: coordinate of widget
        :param y: coordinate of widget
        :return: None
        """
        self.__call_cursor(
            f'UPDATE user_widgets_table SET x_coordinate={x}, y_coordinate={y} WHERE filename="{filename}"')

    def __call_cursor(self, query: str, data=()) -> None:
        """
        This function create cursor and execute query
        :param query: query
        :param data: if query is insert then must be data in tuple
        :return: None
        """
        self.connection = pymysql.connect(self.host, self.username, self.password, self.db_name)
        self.cursor = self.connection.cursor()
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    @staticmethod
    def prepare_data(rows: tuple) -> list:
        """
        This function prepare data of table
        :param rows: rows of table
        :return: data
        """
        data = []
        for row in rows:
            _row = {
                'id': row[0],
                'filename': row[1],
                'path': row[2],
                'x': row[3],
                'y': row[4],
                'params': row[5],
                'pinned': row[6],
                'visible': row[7],
                'del': row[8]
            }
            data.append(_row)

        return data
