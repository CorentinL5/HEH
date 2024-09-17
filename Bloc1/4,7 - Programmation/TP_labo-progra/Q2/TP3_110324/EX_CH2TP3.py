class Timer:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def __str__(self):
        return f"{self.heures:02d}:{self.minutes:02d}:{self.secondes:02d}"

    def next_second(self):
        self.secondes += 1
        if self.secondes > 59:
            self.secondes = 0
            self.minutes += 1
            if self.minutes > 59:
                self.minutes = 0
                self.heures += 1
                if self.heures > 23:
                    self.heures = 0

    def prev_second(self):
        self.secondes -= 1
        if self.secondes < 0:
            self.secondes = 59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes = 59
                self.heures -= 1
                if self.heures < 0:
                    self.heures = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)