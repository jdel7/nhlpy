import requests

from .constants import BASE_URL


class Conference:

    """
    Shows only active conferences
    """

    def all(self):
        response = requests.get("%s/conferences" % (BASE_URL))
        self.data = response.json()
        del self.data["copyright"]
        return self.data

    """
    Shows specific conference and can show World Cup of Hockey
    """

    def info(self, id):
        self.id = id

        if self.id == 0:
            raise Exception("The conference ID cannot be 0")

        if self.id > 7:
            raise Exception("The conference ID cannot be an int greater than 7")

        if self.id < 0:
            raise Exception("The conference ID cannot be a negative int")

        response = requests.get("%s/conferences/%s" % (BASE_URL, self.id))
        self.data = response.json()
        del self.data["copyright"]
        return self.data
