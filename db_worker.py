import pymysql


class DBWorker:

    def __init__(self, username='root', password='root', db_name='widget_db', host='localhost'):
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

    def get_rows(self) -> tuple:
        """
        This function return
        :return: None
        """
        self.cursor.execute('SELECT * FROM user_widgets_table')
        return self.cursor.fetchall()

    def check_for_existing(self, filename, path):
        """
        This function check if row exist in database
        :param filename: name of py-file
        :param path: path to this file
        :return: None
        """
        rows = self.get_rows()
        exist = False
        for row in rows:
            if filename == row[1] and path == filename[2] and row[3] == 0:
                exist = True

        return exist

    def delete_row(self, filename: str):
        """
        This function set del = 1 where is filename
        :param filename: py-file name
        :return: None
        """
        self.cursor.execute(f'UPDATE user_widgets_table SET del=1 WHERE filename="{filename}"')
        self.connection.commit()
