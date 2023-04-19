<h1 align=center><strong>Backend Online Serving 🐍</strong></h1>


This backend consists of:

* Create the backend server with FastAPI and Uvicorn,
* Connect the backend app with PostgreSQL server via the asynchronous SQLAlchemy with AsyncPG driver.
* Create data validation for our database entity with [Pydantic](https://pydantic-docs.helpmanual.io/).
* Create formatters for `json` convention and `datetime`.
* Create custom error/exception handlers for both source code and HTTP.


---

## Python, Env, & Requirements Installation

**INFO**: All related to Python will be setup **IN** and **FROM** the directory `online_serving/`!

* Step 1 $\rightarrow$ Open your project root directory and set up your Python via `Python venv`:

    ```shell
    pyenv install 3.11.0
    ```

* Step 2 $\rightarrow$ Create our virtual environment:

    ```shell
    python -m venv YOUR_Env_env
    ```

* Step 3 $\rightarrow$ Activate your newly created virtual environment as your Python interpreter in the root directory:

    ```shell
    source tutorial-env/bin/activate
    ```

* Step 4 $\rightarrow$ Install the initial project requirements with `pip3`:

    ```shell
    sudo pip install -r requirements.txt
    ```

---

## Docker
When the `Docker` is started, these are the URL addresses:

* Backend Application (API docs) $\rightarrow$ `http://localhost:8001/docs`
* Database editor (Adminer) $\rightarrow$ `http//localhost:8081`

The backend API without `Docker` can be found in `http://localhost:8000/docs`.
## Docker setup:
   ```shell
    # Make sure you are in the ROOT project directory
    chmod +x backend/entrypoint.sh

    docker-compose build
    docker-compose up

    # Every time you write a new code, update your container with:
    docker-compose up -d --build
   ```

<!-- 
## (IMPORTANT) Database setup:
   ```shell
    # (Docker) Generate revision for the database auto-migrations
    docker exec backend_app alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    docker exec backend_app alembic upgrade head    # to register the database classes
    
    # (Local) Generate revision for the database auto-migrations
    alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    alembic upgrade head    # to register the database classes
   ```



## Database
*   Nothing to see here

-->

**INFO**: Make sure that you are in the `online_serving/` directory!

* Stp 1 $\rightarrow$ Run the server:
    ```shell
    uvicorn src.main:backend_app --reload
    ```

* Step 2 (Optional) $\rightarrow$ To stop the server click simultaneously `control` and `C`

---

## Test with PyTest

**INFO**: For running the test, make sure you are in the root directory and NOT in the `backend/` directory!

**INFO**: The testing report is automatically generated and saved in `backend/coverage/**`

* Step 1: Run PyTest:

    ```shell
    pytest
    ```

---