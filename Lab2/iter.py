import os

class DirectoryIterator:
    def __init__(self, directory):
        self._counter = 0
        self._directory = directory
        self._data = os.listdir(os.path.join('dataset', directory))
        self._limit = len(self._data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._counter < self._limit:
            next_path = os.path.join(self._directory, self._data[self._counter])
            self._counter += 1
            return next_path
        else:
            raise StopIteration

    # Методы для доступа к полям
    def get_counter(self):
        return self._counter

    def get_directory(self):
        return self._directory

    def get_data(self):
        return self._data

    def get_limit(self):
        return self._limit

if __name__ == "__main__":
    cat_iterator = DirectoryIterator('cat')
    dog_iterator = DirectoryIterator('dog')

    for _ in range(4):
        print(next(cat_iterator))

    for _ in range(3):
        print(next(dog_iterator))