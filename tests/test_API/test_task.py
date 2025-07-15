from urllib import response
from app.entities import tasks
'''Tests response from the API Only'''


def test_task_retrival(client, dummy_data):
    response = client.get("/tasks/")
    
    assert response.status_code == 200


def test_one_task_retrival(client, dummy_data):
    response = client.get(f"/tasks/{dummy_data.id}")
    
    assert response.status_code == 200


def test_task_creation(client):
    response = client.post(
        "/tasks/",
        json={
        "title": "Test Task",
        "description": "This is a test task"
    })

    assert response.status_code == 201


def test_task_update(client, dummy_data):
    response = client.patch(
        f"/tasks/{dummy_data.id}",
        json={
        "title": "Updated Task",
        "completed": True
    })
    
    assert response.status_code == 200    


def test_task_deletion(client, dummy_data):
    response = client.delete(f"/tasks/{dummy_data.id}")
    
    assert response.status_code == 200

