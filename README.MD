# Учебный проект шаблон для CRUD параметров
```
python -m venv dtb_venv
source dtb_venv/bin/activate
source dtb_venv/Scripts/activate # for Windows
pip install -r requirements.txt

wget --continue https://github.com/intersystems-community/iris-driver-distribution/raw/main/DB-API/intersystems_irispython-3.2.0-py3-none-any.whl &&     pip install intersystems_irispython-3.2.0-py3-none-any.whl &&     rm intersystems_irispython-3.2.0-py3-none-any.whl

# pip install apptools/api/intersystems_irispython-3.2.0-py3-none-any.whl
python -m pip install --upgrade pip
python manage.py makemigrations #<name>
python manage.py migrate
python manage.py createsuperuser --noinput --username adm --email adm@localhost.com
# python run_polling.py
python manage.py runserver

python -m venv dtb_venv && source dtb_venv/Scripts/activate && pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate && python manage.py runserver 8081
```
run django-extensions console: 
`python manage.py shell_plus --ipython`