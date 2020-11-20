import pymysql


class DBWorker:

    def __init__(self, name='root', password='root', db_name='widget_db', host='localhost'):
        self.connection = pymysql.connect(host, name, password, db_name)
        self.cursor = self.connection.cursor()

    def add_row(self, filename, path) -> None:
        query = 'INSERT INTO `user_widgets_table` (`filename`, `path`) VALUES (%s, %s)'
        self.cursor.execute(query, (filename, path))
        self.connection.commit()

    def get_rows(self):
        self.cursor.execute("SELECT * FROM user_widgets_table")
        return self.cursor.fetchall()
