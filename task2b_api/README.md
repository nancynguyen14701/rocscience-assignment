# Task 2B – API Validation for Invalid Login

## 1. Endpoint Discovery

Since the API documentation is unavailable, I would inspect the login request using **DevTools → Network → Fetch/XHR**.

| Item         | Value                                                  |
| ------------ | ------------------------------------------------------ |
| HTTP Method  | `POST`                                                 |
| Endpoint     | `https://auth.rocscience.com/u/login?state=stateValue` |
| Content-Type | `application/x-www-form-urlencoded`                    |

---

## 2. Example Request Payload

```text
state=stateValue
username=autotest@example.com
password=WrongPassword123!
```

---

## 3. Failure Validation

Verify that:

- The HTTP status code indicates authentication failure (e.g. `401 Unauthorized` or `400 Bad Request` or the application's other expected failure status)
- The response body contains an appropriate error code or message (e.g. `"Invalid username or password"`)
- No authentication token (e.g. JWT or access token) is returned
- No authenticated session or authentication cookie is created
- The response schema matches the expected error format, if defined (i.e. the response contains the expected fields and data types)
---

## 4. Example (Python)

See `test_invalid_login.py`.

Run:

```bash
cd api
pytest
```

---

## Scope

This example demonstrates API validation for **invalid credentials**. A complete test suite would also include additional negative scenarios (e.g. empty credentials, malformed requests, and locked accounts).
