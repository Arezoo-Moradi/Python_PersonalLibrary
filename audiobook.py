from podcast import Podcast_episode
from Book2 import Book


class Audiobook(Podcast_episode, Book):
    audiobook_shelf = []

    def __init__(self, title, author, speaker, publish_year, pages, time, price, book_language
                 , audio_language, status=None):
        '''
        :param title:
        :param author:
        :param speaker:
        :param publish_year:
        :param pages:
        :param time:
        :param price:
        :param book_language:
        :param audio_language:
        :param status:
        '''
        # inherent attribute from book class and initialize
        Podcast_episode.__init__(self, title, speaker, publish_year, time, price,
                                 language=None)
        # inherent attribute from book class and initialize
        Book.__init__(self, title, author, publish_year, pages, price, language=None)
        self.audio_language = audio_language
        self.book_language = book_language

        # append attribute of Audiobook class to audiobook_shelf list
        Audiobook.audiobook_shelf.append(self)

    def __str__(self):
        return f" Title:{self.title}, Speaker:{self.speaker}, Author:{self.author}," \
               f"Publish_year:{self.publish_year} ,Pages:{self.pages}," \
               f" Book language:{self.book_language}" \
               f" Audio language:{self.audio_language} ,Time:{self.time} , " \
               f"Price:{self.price} "


    def get_data(number_audiobook):
        print("------------------------please enter information of audiobook:-----------------------")
        for i in range(number_audiobook):
            title = input("please Enter title audiobook:")
            speaker = input("please Enter speaker audiobook:")
            author = input("please Enter author audiobook: ")
            publish_year = int(input("please Enter publish_year audiobook:"))
            pages = int(input("please Enter pages audiobook:"))
            book_language = input("please Enter book_language audiobook:")
            audio_language = input("please Enter audio_language audiobook:")
            time = int(input("please Enter time audiobook:"))
            price = float(input("please Enter price audiobook:"))
            Audiobook(title, author, speaker, publish_year, pages, time, price,
                      book_language, audio_language)
            print('--------------------------------next item ---------------------------------------')

