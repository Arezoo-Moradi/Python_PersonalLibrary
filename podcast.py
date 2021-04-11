from Media import Media


class Podcast_episode(Media):
    podcast_shelf = []

    def __init__(self, title, speaker, publish_year, time, price, language, status=None,
                 listen_time=None, progress=0):
        '''
        :param title:
        :param speaker:
        :param publish_year:
        :param time:
        :param price:
        :param language:
        :param status:
        :param listen_time:
        :param progress:
        '''

        # inherent attribute from Media class and initialize
        Media.__init__(self, title, publish_year, price, language)

        self.speaker = speaker
        self.time = time
        self.listen_time = listen_time
        self.status = status
        self.progress = progress

        # append attribute of Podcast_episode class to podcast_shelf list
        Podcast_episode.podcast_shelf.append(self)

    ''' listen funcation: Show the time of podcast that listen '''
    def listen(self, time):
        self.listen_time = time
        self.progress = (self.listen_time * 100) / self.time
        if time < self.time:
            print(f"you have listen {time} more minutes from {self.title}."
                  f"There are {self.time-self.listen_time} minutes left")
        elif time == self.time:
            print(f'podcast: {self.title} is finished.')
        else:
            print("you can not listen more than Podcast's times")
        self.get_status()

    '''get_status funcation: Show the status of podcast'''
    def get_status(self):
        if self.listen_time == 0:
            self.status = "unlisten"
        elif self.listen_time == self.time:
            self.status = "finished"
        else:
            self.status = "listening"
        return self.status

    '''__str__ funcation: Show the information of podcast'''
    def __str__(self):
        return f"Title:{self.title}, Speaker:{self.speaker}, publish_year:{self.publish_year}," \
               f"Time:{self.time} , Language:{self.language} , Price:{self.price} "

    '''get_data funcation: get the information of podcast of input() from user'''
    def get_data(number_podcast):
        print("-------------------------please enter information of podcast :---------------------------")
        for i in range(number_podcast):
            title = input("please Enter title podcast: ")
            speaker = input("please Enter speaker podcast: ")
            publish_year = int(input("please Enter publish_year podcast:"))
            time = int(input("please Enter time podcast:"))
            language = input("please Enter language podcast:")
            price = float(input("please Enter price podcast: "))
            Podcast_episode(title, speaker, publish_year, time, price, language)
            print('-----------------------------next item ---------------------------------------------')