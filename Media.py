class Media:
    def __init__(self, title, publish_year, price, language, author=None, status=None):
        '''
        :param title:
        :param publish_year:
        :param price:
        :param language:
        :param author:
        :param status:
        '''
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.price = price
        self.language = language

    '''__str__ funcation: Show the information of Media'''
    def __str__(self):
        return f"Title : {self.title}, Author : {self.author}, Publish_year : {self.publish_year}" \
               f"Price : {self.price} , Language : {self.language}"

    def get_data(self):
        pass



