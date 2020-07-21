class Time:

    def __init__(self, h=0, m=0, s=0):
        self._hours = self.hours = h
        self._minutes = self.minutes = m
        self._seconds = self.seconds = s

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, h):
        if h > 23 or h < 0:
            self._hours = 0
        else:
            self._hours = h

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, m):
        if m > 59:
            self._minutes = 0
            self._hours += 1
        elif m < 0:
            self._minutes = 0
        else:
            self._minutes = m

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, s):
        if s > 59:
            self._seconds = 0
            self._minutes += 1
        elif s < 0:
            self._seconds = 0
        else:
            self._seconds = s

    def set_hours(self, h):
        self.hours += h
        return self.__str__()

    def set_minutes(self, m):
        self.minutes += m
        return self.__str__()

    def set_seconds(self, s):
        self.seconds += s
        return self.__str__()

    def change_time(self, h=0, m=0, s=0):
        self.seconds += s
        self.minutes += m
        self.hours += h
        return self.__str__()

    def __repr__(self):
        return f'Time({self.hours}, {self.minutes}, {self.seconds})'

    def __str__(self):
        return f'Time is {self.hours}:{self.minutes}:{self.seconds}'




