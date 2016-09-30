import string

class Human(object):

    def __init__(self):
        self.name = ("first", "last")
        self.age = 'MILLISECONDS'
        self.gender = 0 #gender must be of type binary
        self.employed = False
        self.job = ("position", "duration", "salary")
        self.health = '+/-'
        self.country_of_origin = ("string.capwords()")
        self.country_of_residence = ("string.capwords()")
        self.feeling = 'user.monitor(email)'
        self.email = "required"

        self.life_expectancy = "health * (country_of_origin+country_of_residence)"
        self.average_happiness = "feeling + employed*job[2]"
        self.expected_searches = 0
