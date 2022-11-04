# import doctest


class Time:
    def __init__(self, hour=0, minute=0, seconds=0):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour {hour} must be between {0 - 23}')

        self._hour = hour

    @property
    def minute(self):
        return self.minute

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Minute {minute} must be between {0 - 60}')
        self.minute = minute

    @property
    def second(self):
        return self.minute

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'Second = {second} must be between {0 - 60}')
        self.second = second

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return f'Time(hour={self.hour}, minute={self.minute}, ' + f'second={self.second})'

    def __str__(self):
        """Print Time in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' + (' AM' if self.hour < 12 else ' PM'))
