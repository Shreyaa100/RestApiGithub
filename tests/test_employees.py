def test_employee_requires_auth(client):
    """
    Employees API should require JWT authentication
    """
    response = client.get("/api/v1/employees")
    assert response.status_code == 401