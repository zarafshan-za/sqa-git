def test_login_success():
    # SQA Engineer A's version (on main)
    response_status = 200
    assert response_status == 200, "Login should return 200"

def test_logout():
    # Engineer A also added this
    is_logged_out = True
    assert is_logged_out, "Logout failed"