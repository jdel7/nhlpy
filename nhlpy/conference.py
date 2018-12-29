import requests

from .constants import BASE_URL


class Conference:
    """This class maps to the conference endpoint of the NHL's API.

    Provides information about the conferences in the NHL. The class does
    not take in any parameters when instantiated. After it is instantiated
    it does have two instance variables, ``id`` and ``data``.

    Usage::
    >>> from nhlpy import conference
    >>> c = conference.Conference()
    >>> c.info(1)
    >>> c.all()
    """

    def __init__(self):
        self.id = None
        self.data = None

    def all(self):
        """All available information from all available conferences.

        :returns: information about all conferences
        :rtype: dictionary
        """
        response = requests.get("%s/conferences" % (BASE_URL))
        self.data = response.json()
        del self.data["copyright"]

        return self.data

    def info(self, id):
        """Information from a specific conference ID.

        :param id: The ID of the conference
        :returns: information about that specific conference
        :rtype: dictionary
        """
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
