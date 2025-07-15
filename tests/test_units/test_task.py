from app.entities import tasks
from app.dependencies import tasks
from app.schemas import CreateTask, UpdateTask

'''Tests response from the database Only'''

tsk = CreateTask(
    title="Dream with easy",
    description="Dreams gets easier with time."
)


def test_task_create(session):
    data = tasks.create_new_task(task=tsk, db=session)
    
    assert hasattr(data, "id")
    assert data.title == tsk.title
    assert data.description == tsk.description
    assert data.completed == False


def test_one_task_retrival(session, dummy_data):
    data = tasks.retrieve_task(task_id=dummy_data.id, db=session)
    
    assert data.title == dummy_data.title
    assert data.description == dummy_data.description
    assert data.completed == False


def test_task_retrival_all(session, dummy_data):
    data = tasks.retrieve_all_task(db=session)
    
    assert isinstance(data, list)
    assert len(data) > 0


def test_task_update(session, dummy_data):
    data_update = UpdateTask(completed=True)
    updated_data = tasks.update_task(
        task_id=dummy_data.id, update= data_update, db=session
    )
    
    assert updated_data.title == dummy_data.title
    assert updated_data.completed == True
    assert dummy_data.completed == updated_data.completed


def test_task_delete(session, dummy_data):
    response = tasks.delete_task(task_id=dummy_data.id, db=session)
    # Check if the task is actually deleted
    assert tasks.retrieve_task(task_id=response.id, db=session) is None
