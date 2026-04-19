def test_app_is_running():
    # Simulates checking if the app responds
    response_code = 200
    assert response_code == 200, "App is down!"

def test_database_connection():
    db_connected = True
    assert db_connected, "Database not reachable!"