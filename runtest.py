import pytest

# Define the order of test modules to run
test_modules = [
    "orderplace.py"
]

if __name__ == "__main__":
    # Run the tests in the specified order
    for module in test_modules:
        pytest.main([f"./{module}"])