from dataclasses import dataclass
import os


if os.name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str

    @property
    def extension(self) -> str:
        return self.name.rsplit('.', 1)[-1][0:]

    def ls(self) -> str:
        return self.dir + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, folder: str):
        super().__init__()
        self.folder = folder
        self.append(self.folder + PATH_SEP)

    def add_element(self, obj: File):
        self.append(obj.ls())

    def ls(self) -> str:
        directory = '\n'.join(self)
        return directory


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())


file = File('AI.exe', "C:\Games\Alien Isolation")
file2 = File('poster.jpg', "C:\wallpapers")
new_folder = Folder("C:\download\Books\Fantastic")
new_folder.add_element(file)

ls(file2, new_folder)

# Результат:

# C:\wallpapers\poster.jpg
# C:\Games\Alien Isolation\AI.exe
# C:\download\Books\Fantastic\
