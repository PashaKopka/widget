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
        query = 'INSERT INTO `user_widgets_table` (`filename`, `path`) VALUES (%s, %s)'
        self.cursor.execute(query, (filename, path))
        self.connection.commit()

    def get_rows(self) -> tuple:
        """
        This function return
        :return:
        """
        self.cursor.execute("SELECT * FROM user_widgets_table")
        return self.cursor.fetchall()
