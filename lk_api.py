import slumber

class ApiWrapper(object):
    def __init__(self, login, pwd):
        self.api = slumber.API("http://produtos-globocom.leankit.com/kanban/api/",
                                auth=(login, pwd))
        self.board = self.api.boards("113658644").get()['ReplyData'][0]

    def get_board_tags(self):
        tags = self.board['AvailableTags']
        return tags.split(',')

    def get_card_type(self):
        return self.board['CardTypes']

