import Book2
import magazine
import podcast
import audiobook

SHELF = []

'''my_sort funcation: Sorts all shelf items based on progress
                       and print their {media type,name,progress}'''
def my_sort(list):
    list = sorted(list, key=lambda x: x.progress,reverse=True)
    for i in list:
        print(type(i).__name__, i.title, i.progress)
    print('---------------------------------------------------------------------------------')


NAME = input("Please Enter your name:")
print("---------------*****----------------- Welcome:", NAME)
while True:
    print("1. Add a Book / Magazine / Podcast / Aoudio Book")
    print("2. Show my book shelves")
    print('3. Add read pages or time listen')
    print('4. sort my book shelf')
    print('5. Exit')
    print('----------------------------------------------------------------------------------')
    print('---------------please choose a number between 1,2,3,4,5---------------------------')
    choise = input('Enter the number:')

    if choise == '1':
        print("-------------------1.Book ,2.Magazine, 3.Podcast, 4.Audio book-------------------")
        print('--------------------please choose a number between 1,2,3,4-----------------------')
        print('---------------------------------------------------------------------------------')

        choise1 = input('Enter the number:')
        """--------------------------------------------------------------------------------------"""
        if choise1 == '1':
            num = int(input('Enter the number of book:'))
            Book2.Book.get_data(num)
            SHELF.extend(Book2.Book.bookshelf)
        elif choise1 == '2':
            num = int(input('Enter the number of magazine:'))
            magazine.Magazine.get_data(num)
            SHELF.extend(magazine.Magazine.magazine_shelf)
        elif choise1 == '3':
            num = int(input('Enter the number of podcast:'))
            podcast.Podcast_episode.get_data(num)
            SHELF.extend(podcast.Podcast_episode.podcast_shelf)
        elif choise1 == '4':
            num = int(input('Enter the number of Audio Book:'))
            audiobook.Audiobook.get_data(num)
            SHELF.extend(audiobook.Audiobook.audiobook_shelf)
        else:
            print('Error: your choose is wrong!!')
        continue
        """-----------------------------------------------------------------------------------------"""
    elif choise == '2':
        print('-----------------------Print the media_type and the title-----------------------------')
        for i in SHELF:
            media_type = type(i).__name__
            print(f'media_type : {media_type} , Name: {i.title}')
            continue
        print('--------------------------------------------------------------------------------------')

    elif choise == '3':
        print("----------------------- choose a number between 1,2,3,4 -------------------------------")
        print("----------------------- 1.Book, 2.Magazine, 3.Podcast, 4.Audio book -------------------")
        """--------------------------------------------------------------------------------------------"""

        choise1 = input('Enter a number:')
        if choise1 == '1':
            Name = input('which book do you want?')
            page = int(input('Enter page of book:'))
            obj = next(element for element in SHELF if element.title == Name)
            Book2.Book.read(obj, page)
        elif choise1 == '2':
            Name = input('which magazine do you want?')
            page = int(input('Enter the page of magazine:'))
            obj = next(element for element in SHELF if element.title == Name)
            magazine.Magazine.read(obj, page)
        elif choise1 == '3':
            Name = input('which podcast do you want?')
            time = int(input('Enter the time of podcast:'))
            obj = next(element for element in SHELF if element.title == Name)
            podcast.Podcast_episode.listen(obj, time)
        elif choise1 == '4':
            Name = input('which audiobook do you want?')
            time = int(input('Enter the time of audiobook:'))
            obj = next(element for element in SHELF if element.title == Name)
            audiobook.Audiobook.listen(obj, time)
        else:
            print('Error: your choose is wrong!!')
        """-------------------------------------------------------------------------------------------"""
    elif choise == '4':
        my_sort(SHELF)
        continue
        """-------------------------------------------------------------------------------------------"""
    else:
        break
