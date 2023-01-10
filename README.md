### Basic Airbnb RestAPI

### Envoriment: 
```
python3 -m venv venv 
OR
virtualenv --python=python3 venv

source venv/bin/activate
```

### Requirements: 
```
pip install -r requirements.txt
```

### Database - POSTGRES (Linux): 
```
sudo -i -u postgres
psql
CREATE USER user_default WITH PASSWORD 'defaultdatabase';
ALTER USER user_default CREATEDB;
CREATE DATABASE default_database;
ALTER DATABASE default_database OWNER TO user_default;
CREATE EXTENSION pg_trgm;
```


### Migration: 
```
python manage.py migrate
```

### New translations:
```
python manage.py makemessages --locale pt_BR

Change to pt-br on settings:
LANGUAGE_CODE= 'pt-BT'

Obs: Não traduzi.
```

### Run: 
```
python manage.py runserver
```


### Unit Tests: 
```
python manage.py test --failfast
```


### Dump seed: 
```
python manage.py dumpdata {app} --indent 4 > seed/{app}.json
```

### Load dump seed: 
```
bash migrate_and_seed.sh
```

### Authenticate Token: 
```
Bearer {access_token}
```



