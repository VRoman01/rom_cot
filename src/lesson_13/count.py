
class Count:

    __COUNTER = 0

    def __init__(self):
        Count.__COUNTER += 1

    @classmethod
    def get_counter(cls):
        print(Count.__COUNTER)



if __name__ == '__main__':
    Count()
    Count()
    Count()
    Count.get_counter()
