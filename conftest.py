import pytest

@pytest.fixture(scope="function")
def login_url():
    return "http://localhost:3000/"


    
 