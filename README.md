# ToDO
ToDo app will be responsible for creating user, login and CRUD od tasks.

#### Clone repo:
``` git clone https://github.com/MbxrAteeq/ToDo-App.git ```

#### Create virtual environment:
```python -m venv env```

#### Activate virtual environment:
```surce env/bin/activate```

#### Install requirements:
```pip install -r requirements.txt```

#### Create .env
create env file and set values of these variables
```
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost:port/db_name
JWT_SECRET_KEY=somesecretkey
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRES=8
```

### Run app
```python app.py```

### Alembic Migrations
#### Create Migration File
```alembic revision --autogenerate -m "name"```

#### Upgrade migrations
```alembic upgrade head```

#### Downgrade migration
```alembic downgrade -1```

#### See Migrations history
```alembic history```

