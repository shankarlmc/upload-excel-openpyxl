# Upload excel file using openpyxl

## Setup and run locally
- Clone the repository
```
git clone git@github.com:shankarlmc/upload-excel-openpyxl.git
cd upload-excel-openpyxl
cp .env-sample .env
```
- Create virtual environment
```
python -m venv .venv
source .venv/bin/activate
```
- Install Dependencies
```
pip install -r requirements.txt
```
- Migrate and runserver
```
python manage.py migrate
python manage.py runserver
```
- Sample file url
```
GET http://127.0.0.1:8000/base/sheet/
```
- Upload file url
```
POST http://127.0.0.1:8000/base/sheet/
```