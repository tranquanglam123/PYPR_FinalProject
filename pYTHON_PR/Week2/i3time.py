class Time():
    
    def __init__(self, hour, minute, second):
        """
        Initialize a Time instance giving the hour, minute and second.
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def total_seconds(self):
        """
        Compute the total number of seconds since the start of the day.
        """
        return 3600 * self.hour + 60 * self.minute + self.second
    
    def __str__(self):
        """
        Create a string representation of this time.
        """
        s = ''
        if self.hour < 10:
            s += '0'
        s += str(self.hour)
        s += ':'
        if self.minute < 10:
            s += '0'
        s += str(self.minute)
        s += ':'
        if self.second < 10:
            s += '0'
        s += str(self.second)
        return s
my_time = Time(9, 5, 7)
my_seconds = my_time.total_seconds()
print(my_seconds)
print(my_time)
