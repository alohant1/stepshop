class Exam:
    def __init__(self):
        self.__readyness = True

    def ready(self):
        return self.__readyness


e = Exam()
print(e.ready())
