class Book:
    bookshelf = []

    def __init__(self, title, author, publish_year, pages, language, price, read_pages, status=None):
        """
        :param title:
        :param author:
        :param publish_year:
        :param pages:
        :param language:
        :param price:
        :param read_pages:
        :param status:
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_pages = read_pages
        self.status = status
        Book.bookshelf.append(self)

    ''' read funcation: Show the number of books that read '''
    def read(self):
        if self.read_pages < self.pages:
            print(f"you have read {self.read_pages} more pages from {self.title}."
                  f"There are {self.pages-self.read_pages} pages left")
        elif self.read_pages == self.pages:
            print(f'{self.title} is finished.')
        else:
            print("you can not read more than books pages")

    '''__str__ funcation: Show the information of books'''
    def __str__(self):
        return f" Title : {self.title}, Author : {self.author}, Publish_year : {self.publish_year}," \
               f" Pages : {self.pages} , Language : {self.language} , Price : {self.price} "

    '''get_status funcation: Show the status of book'''
    def get_status(self):
        if self.read_pages == 0:
            self.status = "unread"
        elif self.read_pages == self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status


'''get_data funcation: get the information of books of input() from user'''
def get_data(number_books):
    print("----------------------------please enter information of book:---------------------------------")
    for i in range(number_books):
        title = input("please Enter title book:")
        author = input("please Enter author book:")
        publish_year = int(input("please Enter publish_year book:"))
        pages = int(input("please Enter pages book:"))
        read_pages = int(input("please Enter the read pages of book:"))
        language = input("please Enter language book:")
        price = float(input("please Enter price book:"))
        print("---------------------------------------next item--------------------------------------------")
        book = Book(title, author, publish_year, pages, language, price, read_pages)


number_books = int(input('please enter the number of books:'))
get_data(number_books)
print("-----------------------print information of book in bookshelf--------------------------------")
Print_bookshelf = [print(i) for i in Book.bookshelf]
book_shelf = Book.bookshelf
"----------------------------------------------------------------------------------------------------"
print('--------------------------------Output of read Funcation--------------------------------------')
for item in range(len(book_shelf)):
    book_shelf[item].read()
print('--------------------------------Output of status Funcation------------------------------------')
for item in range(len(book_shelf)):
    print(f'{item}:', book_shelf[item].get_status())