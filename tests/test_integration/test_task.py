from app.entities import tasks
'''
    Testing both API and the data 
    Returned from the database
'''


def test_task_retrival_all(client, dummy_data):
    response = client.get("/tasks/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_task_retrival_by_id(client, dummy_data):
    response = client.get(f"/tasks/{dummy_data.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == dummy_data.id
    assert data["title"] == dummy_data.title
    assert data["description"] == dummy_data.description
    

def test_task_creation(client):
    response = client.post(
        "/tasks/",
        json={
        "title": "Test Task",
        "description": "This is a test task",
    })
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"


def test_task_update(client, dummy_data):
    response = client.patch(
        f"/tasks/{dummy_data.id}",
        json={
        "title": "Updated Task",
        "completed": True
    })
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == "Updated Task"
    assert data["completed"] == True
    assert dummy_data.title != data["title"]
    assert dummy_data.completed != data["completed"]


def test_task_deletion(client, dummy_data):
    response = client.delete(f"/tasks/{dummy_data.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": f"Task '{dummy_data.title}' deleted successfully"}
