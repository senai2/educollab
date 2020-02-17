# The Social Web Project - EduCollab

## Local Development

### Setup
Clone the repository and `cd` into the directory. Use the following commands to build the virtual environment.
```
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### DB Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Collect Static Files
```
python3 manage.py collectstatic
```
Not necessarily needed incase no changes are made to the static files.
### Create Superuser
```
python3 manage.py createsuperuser
```
Create a super user to log into the admin panel.

### Start Server
Enable debugging by changing `DEBUG=True` in `educollab/settings.py`
```
python3 manage.py runserver
```
