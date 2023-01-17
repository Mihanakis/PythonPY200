from typing import Union
import doctest


class MusicAlbum:
    """
    Класс формирует альбом с характеристиками: артист, стиль, количество песен.
    # >>> MusicAlbum('Artist', 'Style', 10).get_artist()
    'Artist'
    """

    def __init__(self, artist: Union[str], album_style: Union[str], song_number: Union[int]) -> None:
        self.artist = artist
        self.album_style = album_style
        self.song_number = song_number

    def get_artist(self) -> str:
        """
        Метод возвращает исполнителя.
        :return: Исполнитель альбома.
        """
        return self.artist

    def get_album_style(self) -> str:
        """
        Метод возвращает стиль альбома.
        :return: Стиль альбома.
        """
        return self.album_style

    def set_album_style(self, style: Union[str]) -> str:
        """
        Метод изменяет параметр класса "стиль альбома".
        :param style: Задаваемый параметр "стиль альбома".
        :return: Изменённое значение параметра "стиль альбома".
        """
        self.album_style = style
        return self.album_style

    def get_memory_album(self) -> int:
        """
        Метод возвращает количество памяти которе занимает музыкальный альбом.
        :return: Количество памяти которое занимает альбом, Мб.
        """
        return self.song_number * 8


class Disography:
    """
    Класс работает с музыкальной коллекией из класса альбомов.
    """

    def __init__(self, data: Union[list]) -> None:
        self.data = data

    def get_memory_discograpy(self) -> int:
        """
        Метод возвращает суммарное количество памяти, которое занимает музыкальная коллекция
        :return: Количество памяти которое занимает музыкальная коллекция, Мб
        """
        memory = 0
        for d in self.data:
            memory += d.get_memory_album()
        return memory

    def sort_by_artist(self) -> list:
        """
        Метод сортирует список музыкальных исполнителей
        :return: Сортированный список музыкальных исполнителей
        """
        artist_data = []
        for n in self.data:
            artist_data.append(n.get_artist())
        return sorted(artist_data)

    def get_by_style(self, style) -> list:
        """
        Метод возвращает список исполнителей по заданному ключу - стилю
        :param style: Ключ для возвращения исполнителя по совпадению
        :return: Список исполнителей
        """
        artist_style_data = []
        for s in self.data:
            if style == s.get_album_style():
                artist_style_data.append(s.get_artist())
        if artist_style_data == []:
            raise ValueError(f"Исполнителя со стилем '{style}' нет")
        return artist_style_data


class Storage:
    def __init__(self, memory: Union[int, float], data: Union[list]):
        self.memory = memory
        self.data = data

    def choice_storage(self):
        """
        Метод возвращает носитель, на который поместится данная музыкальная коллекция
        :return:
        """
        return "CD" if self.memory <= 700 else "HDD"

    def cd_write(self):
        cd_data, mem = [], 0
        for w in self.data:
            mem += w.get_memory_album()
            if mem > 700:
                break
            cd_data.append(w.get_artist())
        return cd_data


if __name__ == "__main__":
    meteora = MusicAlbum('Linkin Park', 'Alternative', 12)  # Cписок входных данных в виде альбомов
    californication = MusicAlbum('Red Hot Chili Peppers', 'Alternative', 15)
    love_metal = MusicAlbum('HIM', 'Metal', 11)
    bury_the_hatchet = MusicAlbum('The Cranberries', 'Alternative', 13)
    sams_town = MusicAlbum('The Killers', 'Indie-rock', 13)
    hopes_and_fears = MusicAlbum('Keane', 'Pop-rock', 16)
    mezmerize = MusicAlbum('System of A Down', 'Alternative', 10)
    let_the_bad_times_roll = MusicAlbum('The Offspring', 'Punk-rock', 12)

    colletion = [meteora,
                 californication,
                 love_metal,
                 bury_the_hatchet,
                 sams_town,
                 hopes_and_fears,
                 mezmerize,
                 let_the_bad_times_roll]

    discography = Disography(colletion)
    discography_memory = Storage(discography.get_memory_discograpy(), colletion)

    print("Тесты методов класса 'MusicAlbum':")
    print(meteora.get_artist(), meteora.get_album_style(), meteora.get_memory_album(), sep=' | ')
    print("Меняем название стиля альбома 'Alternative' на 'Nu metal'")
    meteora.set_album_style("Nu metal")
    print(meteora.get_artist(), meteora.get_album_style(), meteora.get_memory_album(), sep=' | ')
    print("-------------------------------")
    print("Тесты методов класса 'Disography':")
    print(f"Коллекция музыки составляет {discography.get_memory_discograpy()} Мб")
    print("Исполнители коллекции музыки:", ", ".join(discography.sort_by_artist()))
    print("Из них в стиле 'Alternative':", ", ".join(discography.get_by_style('Alternative')))
    print("-------------------------------")
    print("Тесты методов класса 'Storage':")
    print(f"Для хранения этой коллекции подошёл бы: {discography_memory.choice_storage()}")
    print("На CD-диск удалось бы записать исполнителей:", ", ".join(discography_memory.cd_write()))
