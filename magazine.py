from Book2 import Book


class Magazine(Book):

    magazine_shelf = []

    def __init__(self, title, author, publish_year, pages, price, language, issue,
                 pages_read=None, status=None):
        '''
        :param title:
        :param author:
        :param publish_year:
        :param pages:
        :param price:
        :param language:
        :param issue:
        :param pages_read:
        :param status:
        '''

        # inherent attribute from book class and initialize
        Book.__init__(self, title, author, publish_year, pages, price, language)
        self.issue = issue

        # append attribute of magazine class to magazine_shelf list
        Magazine.magazine_shelf.append(self)

    def __str__(self):
        # inherent of __str__ funcation of book class
        self.__str__()
        return f' Issue : {self.issue}'

    '''get_data funcation: get the information of magazine of input() from user'''
    def get_data(number_magazine):
        print("-------------------------please enter information of magazine:-------------------------")
        for i in range(number_magazine):
            title = input("please Enter title magazine: ")
            author = input("please Enter author magazine: ")
            publish_year = int(input("please Enter publish_year magazine:"))
            pages = int(input("please Enter pages magazine:"))
            language = input("please Enter language magazine:")
            price = float(input("please Enter price magazine: "))
            issue = int(input("please Enter issue magazine:"))
            Magazine(title, author, publish_year, pages, price, language, issue)
            print('-----------------------------next item --------------------------------------------')






