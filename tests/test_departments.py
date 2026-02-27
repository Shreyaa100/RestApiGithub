def test_departments_requires_auth(client):
    """
    Departments API should require JWT authentication
    """
    response = client.get("/api/v1/departments")
    assert response.status_code == 401