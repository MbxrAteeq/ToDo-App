# ToDO
ToDo app can be used to create user, login and CRUD tasks.

#### Clone repo:
``` git clone https://github.com/MbxrAteeq/ToDo-App.git ```

#### Create virtual environment:
```python -m venv env```

#### Activate virtual environment:
```source env/bin/activate```

#### Install requirements:
```pip install -r requirements.txt```

#### Create .env
`touch.env`

and set these variables
```
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost:port/db_name
JWT_SECRET_KEY=somesecretkey
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRES=8
DECRYPTION_KEY=secretdecryptionkey
COMMON_ENCRYPTION_KEY=asdjk@15r32r1234asdsaeqwe314SEFT
COMMON_16_BYTE_IV_FOR_AES=IVIVIVIVIVIVIVIV
```

### Alembic Migrations
#### Create Migration File (Not required to run this project)
```alembic revision --autogenerate -m "name"```

#### Upgrade migrations (Required)
```alembic upgrade head```

#### Downgrade migration  (Not required to run this project)
```alembic downgrade -1```

#### See Migrations history  (Not required to run this project)
```alembic history```

### Run app
```python app.py```

### Decrypt Response
Request this endpoint `/decrypt_data` with json payload containing `decryption_key` and `encrypted_data`.

### Postman Collection
https://drive.google.com/file/d/15b-POj6TNm6sg-fsll4mS-LCEqI364Bx/view?usp=sharing