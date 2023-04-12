from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._row = list()

    def __len__(self):
        return len(self._row)

    def enqueue(self, value):
        self._row.append(value)

    def dequeue(self):
        return self._row.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._row):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._row[index]
