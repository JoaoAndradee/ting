from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    files = [
        {"nome_do_arquivo": "file1.txt", "qtd_linhas": 3},
        {"nome_do_arquivo": "file2.txt", "qtd_linhas": 8},
        {"nome_do_arquivo": "file3.txt", "qtd_linhas": 2},
        {"nome_do_arquivo": "file4.txt", "qtd_linhas": 7},
    ]

    for file in files:
        priority_queue.enqueue(file)

    assert priority_queue.dequeue() == {
        "nome_do_arquivo": "file1.txt",
        "qtd_linhas": 3
    }

    assert priority_queue.dequeue() == {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 2
    }

    with pytest.raises(IndexError):
        priority_queue.search(100)
