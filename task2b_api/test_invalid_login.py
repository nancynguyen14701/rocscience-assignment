import requests

BASE_URL = "https://auth.rocscience.com"


def test_invalid_login_via_api():
    login_url = f"{BASE_URL}/u/login"
    params = {"state": "state"}

    payload = {"username": "autotest@example.com", "password": "WrongPassword123!"}
    response = requests.post(login_url, params=params, data=payload, allow_redirects=False)

    print(f"Status: {response.status_code}")
    print(f"Location: {response.headers.get('Location', 'N/A')}")

    assert response.status_code == 400, (
        f"Expected 400 Bad Request, got {response.status_code}"
    )

    print("PASSED: Invalid login correctly rejected")


if __name__ == "__main__":
    print("=== Testing invalid login via API ===")
    test_invalid_login_via_api()

    print("\nAll API tests passed.")
