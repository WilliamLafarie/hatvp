# hatvp

Project around [hatvp](https://www.hatvp.fr/)'s datas: [Download the data](https://www.hatvp.fr/agora/opendata/csv/Vues_Fusionnees.zip)

## Prerequisites

* A PostregreSQL database
* Python 3
* Pyenv

## Installation 
After cloning the project repository, you have to create your **virtual environment**
### Ubuntu
```bash
#Create a virtual environment directory
pyvenv venv

#Activate venv
source ./venv/bin/activate.sh

#Install librairies from requirements.txt
pip install -r requirements.txt

#Run Django App
python manage.py runserver
```
### Windows
```powershell
#Create a virtual environment directory
virtualenv -ppython3 venv

#Activate venv
venv\Scripts\activate

#Install librairies from requirements.txt
pip install -r requirements.txt

#Run Django App
python manage.py runserver
```
## Setting up the project

#### First step: create & fill your .env file

```bash
# Create a .env file at the root of the project
touch .env
```

```bash
# Your .env file

DB_NAME = [your_database_name]
DB_USER = [your_database_username]
DB_PASS = [your_database_password]
```

#### Second step: import the database

```bash
# Create an admin account 
python manage.py createsuperuser

# Populate the database (it may take some time)
python manage.py import

# And then run Django App
python manage.py runserver
```


## Wiki

[Wiki](https://github.com/WilliamLafarie/hatvp/wiki)

## Contributors

[William Lafarie](https://github.com/WilliamLafarie)

[Odom Ear](https://github.com/Reamodo)

[Gauthier Magne](https://github.com/GauthierMagne)

[Sebastien Cosneau](https://github.com/sebastiencosneau)

## License
[MIT](https://choosealicense.com/licenses/mit/)
