def test_salaries_requires_auth(client):
    """
    Salaries API should require JWT authentication
    """
    response = client.get("/api/v1/salaries/employee/123")
    assert response.status_code == 401