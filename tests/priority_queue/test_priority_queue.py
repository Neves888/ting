from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    file_one = {
        "nome_do_arquivo": "teste1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [""],
        }
    file_two = {
        "nome_do_arquivo": "teste2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [""],
        }
    file_three = {
        "nome_do_arquivo": "teste3.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": [""],
        }

    priority = PriorityQueue()

    priority.enqueue(file_one)
    priority.enqueue(file_two)
    priority.enqueue(file_three)

    assert len(priority) == 3
    assert priority.search(0) == file_one
    # assert priority.search(1) == file_two
    # assert priority.search(2) == file_three
    with pytest.raises(IndexError):
        priority.search(5)
    assert priority.dequeue() == file_one
