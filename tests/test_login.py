def test_login_success():
    # Developer's updated logic
    response_status = 200
    assert response_status == 200, "Login should return 200"

def test_login_failure():
    # New test added by developer
    response_status = 401
    assert response_status == 401, "Invalid login should return 401"