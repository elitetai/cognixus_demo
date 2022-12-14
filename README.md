# cognixus_demo

## Setup Instructions

1. Docker installation

    https://docs.docker.com/engine/install/

1. Confirm on docker's and docker-compose's installations

    ```bash
    docker --version
    docker-compose --version
    ```

1. Clone the repository by running 

    ```bash
    git clone https://github.com/elitetai/cognixus_demo.git
    ```

1. Change the current working directory
     ```bash
    cd cognixus_demo
    ```

1. Docker setup
    
    - Start services with docker compose under detached mode
    ```bash
    docker-compose up -d --build
    ```

    - Execute docker with interactive `bash` command 
    ```bash
    docker exec -it cognixus_todo_list /bin/bash
    ```

    - Run database migration
    ``` bash
    python3 manage.py migrate
    ```

--- 
## Google Authentication

- Obtain `access_token` to obtain the authencation token by login using Google. Copy and paste it onto your web browser.

    ```
    https://accounts.google.com/o/oauth2/auth?client_id=836191007258-7k4lkmkrvcn10optddih6l040qm5tish.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:8000/&scope=profile&email&response_type=code&include_granted_scopes=true&access_type=offline&state=state_parameter_passthrough_value
    ```

- You will obtain a `curl` command on the web display. Copy and paste it into the terminal.

- Once the command has been executed, a response will be obtained. Copy the `access_token`'s value and replace below's `<access_token>` accordingly. Execute the command to obtain `token` for subsequent `curl` commands as a bearer token.

    Request:
    ```bash
    curl -X POST http://127.0.0.1:8000/api/register-by-access-token/social/google-oauth2/ \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"access_token": "<access_token>"}'
    ```

    Response (SUCCESS):
    ```json
    {"token": string}
    ```

- **Testing purpose:** You may test the `token` received via below command

    Request:
    ```bash
    curl http://127.0.0.1:8000/api/authentication-test/ \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token <token>'
    ```

    Response (SUCCESS):
    ```json
    {"message": "User successfully authenticated"}
    ```

---

## To-Do-List API

**Notes:** Subsequent APIs would require `token` received previously. Please replace `<token>` accordingly.
```bash
-H 'Authorization: Token <token>'
```

1. **Create API**
    ```http
    POST /todo/create/
    ```

    Request (with example):
    ```bash
    curl -X POST http://127.0.0.1:8000/todo/create/ \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token <token>' \
    -d '{"title": "Bake Cookies"}'
    ```

    Response (SUCCESS):
    ```json
    {
        "id": integer,
        "title": string,
        "is_completed": bool,
        "owner": string
    }
    ```

1. **Update API**
    ```http
    PUT /todo/update/{id}
    ```

    Request (with example):
    ```bash
    curl -X PUT http://127.0.0.1:8000/todo/update/1/ \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token <token>' \
    -d '{"title": "Wash Laundry", "is_completed": true}'
    ```

    Response (SUCCESS):
    ```json
    {
        "id": integer,
        "title": string,
        "is_completed": bool,
        "owner": string
    }
    ```

1. **List API**
    ```http
    GET /todo/
    ```

    Request:
    ```
    curl http://127.0.0.1:8000/todo/ \
    -H 'Authorization: Token <token>'
    ```

    Response (SUCCESS):
    ```json
    [
        {
            "id": integer,
            "title": string,
            "is_completed": bool,
            "owner": string
        },
    ]
    ```

1. **Delete API**
    ```http
    DELETE /todo/delete/{id}
    ```

    Request (with example):
    ```bash
    curl -X DELETE http://127.0.0.1:8000/todo/delete/1/ \
    -H 'Authorization: Token <token>'
    ```

    **Notes:** No response is provided
