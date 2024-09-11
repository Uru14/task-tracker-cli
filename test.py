import os
import pytest
from task_tracker import add_task, update_task, delete_task, mark_task, load_task

@pytest.fixture
def setup_and_teardown():
    test_file = 'task.json'
    if os.path.exists(test_file):
        os.remove(test_file)
    yield
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_task(setup_and_teardown):
    add_task("Test task")
    tasks = load_task()
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Test task"

def test_update_task(setup_and_teardown):
    add_task("Initial task")
    update_task(1, "Updated task")
    tasks = load_task()
    assert tasks[0]['description'] == "Updated task"

def test_delete_task(setup_and_teardown):
    add_task("Task to delete")
    delete_task(1)
    tasks = load_task()
    assert len(tasks) == 0

def test_mark_task(setup_and_teardown):
    add_task("Task to mark")
    mark_task(1, "done")
    tasks = load_task()
    assert tasks[0]['status'] == "done"
