import os
from os import system
from widget import settings


class UiCompiler:

    def __init__(self, filename, path):
        system(f'{settings.MAIN_DIRECTORY[:-7]}\\venv\\Scripts\\activate')
        system(f'pyuic5 {path} -o {settings.MAIN_DIRECTORY}\\ui\\user_ui\\{filename}.py')

        self.__out_file_path = f'{settings.MAIN_DIRECTORY}\\ui\\user_ui\\{filename}.py'
        self.delete_ui_file(path)

    @staticmethod
    def delete_ui_file(path):
        os.remove(path)

    @property
    def out_file_path(self):
        """
        property of py-file path
        :return: py-file path
        """
        return self.__out_file_path
