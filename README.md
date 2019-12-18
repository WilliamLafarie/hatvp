# hatvp

Project around [hatvp](https://www.hatvp.fr/)'s datas: [Download the data](https://www.hatvp.fr/agora/opendata/csv/Vues_Fusionnees.zip)

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

## Wiki

[Wiki](https://github.com/WilliamLafarie/hatvp/wiki)

## Contributors

[William Lafarie](https://github.com/WilliamLafarie)

[Odom Ear](https://github.com/Reamodo)

[Gauthier Magne](https://github.com/GauthierMagne)

[Sebastien Cosneau](https://github.com/sebastiencosneau)

## License
[MIT](https://choosealicense.com/licenses/mit/)
