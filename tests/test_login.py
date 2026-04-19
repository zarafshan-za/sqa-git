def test_login_success():
    # SQA Engineer B's version - different assertion
    response_status = 200
    assert response_status == 201, "Login should return 201"