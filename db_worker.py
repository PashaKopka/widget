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
        self.connection = pymysql.connect(host, username, password, db_name)
        self.cursor = self.connection.cursor()

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
        self.cursor.execute(query, (filename, path))
        self.connection.commit()

    def get_rows(self) -> list:
        """
        This function return
        :return: None
        """
        self.cursor.execute('SELECT * FROM user_widgets_table')
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
            if filename == row['filename'] and path == filename[2] and row['del'] == 0:
                exist = True

        return exist

    def delete_row(self, filename: str) -> None:
        """
        This function set del = 1 where is filename
        :param filename: py-file name
        :return: None
        """
        self.cursor.execute(f'UPDATE user_widgets_table SET del=1 WHERE filename="{filename}"')
        self.connection.commit()

    def toggle_visibility(self, filename: str) -> None:
        self.cursor.execute(f'SELECT visible FROM user_widgets_table WHERE filename="{filename}"')
        visibility = self.cursor.fetchall()[0][0]
        if visibility:
            self.cursor.execute(f'UPDATE user_widgets_table SET visible=0 WHERE filename="{filename}"')
        else:
            self.cursor.execute(f'UPDATE user_widgets_table SET visible=1 WHERE filename="{filename}"')
        self.connection.commit()

    def add_coordinate(self, filename: str, x, y) -> None:
        self.cursor.execute(
            f'UPDATE user_widgets_table SET x_coordinate={x}, y_coordinate={y} WHERE filename="{filename}"')
        self.connection.commit()

    @staticmethod
    def prepare_data(rows: tuple) -> list:
        data = []
        for row in rows:
            _row = {
                'id': row[0],
                'filename': row[1],
                'path': row[2],
                'x': row[3],
                'y': row[4],
                'visible': row[5],
                'del': row[6]
            }
            data.append(_row)

        return data
