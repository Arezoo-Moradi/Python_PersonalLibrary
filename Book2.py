from Media import Media
class Book(Media):
    bookshelf = []

    def __init__(self, title, author, publish_year, pages, price, language,
                 pages_read=None, status=None, progress=0):
        '''

        :param title:
        :param author:
        :param publish_year:
        :param pages:
        :param price:
        :param language:
        :param pages_read:
        :param status:
        :param progress:
        '''

        # inherent attribute from Media class and initialize
        Media.__init__(self, title, author, publish_year, price, language)

        self.pages = pages
        self.pages_read = pages_read
        self.status = status
        self.progress = progress

        # append attribute of Book class to bookshelf list
        Book.bookshelf.append(self)

    ''' read funcation: Show the number of books that read '''
    def read(self, pages):
        self.pages_read = pages
        self.progress = (self.pages_read * 100) / self.pages
        if pages < self.pages:
            print(f"you have read {pages} more pages from {self.title}."
                  f"There are {self.pages-self.pages_read} pages left")
        elif pages == self.pages:
            print(f'book: {self.title} is finished.')
        else:
            print("you can not read more than books pages")
        self.get_status()

    '''get_status funcation: Show the status of book'''
    def get_status(self):
        if self.pages_read == 0:
            self.status = "unread"
        elif self.pages_read == self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status

    '''get_data funcation: get the information of books of input() from user'''
    def get_data(number_books):
        print("--------------------------please enter information of book:----------------------------")
        for i in range(number_books):
            title = input("please Enter title book:")
            author = input("please Enter author book:")
            publish_year = int(input("please Enter publish_year book:"))
            pages = int(input("please Enter pages book:"))
            language = input("please Enter language book:")
            price = float(input("please Enter price book: "))
            book = Book(title, author, publish_year, pages, language, price)
            print('-----------------------------next item --------------------------------------------')

