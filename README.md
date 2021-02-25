Установка проекта локально
=====================
1. Скачайте проект с гитхаб
2. Извлеките папку market--master из архива
3. Нажмите ПКМ (ПКМ + Shift на Windows) по извлеченной папке и откройте консоль (консоль PowerShell на Windows)
4. Установите виртуальное окружение командой  
`python3 -m venv venv` - Linux  
`python -m venv venv` - Windows
5. Активируйте виртуальное окружение командой  
`. venv/bin/activate` - Linux  
`venv/Scripts/activate` - Windows  
После активации перед приглашением в командной строке у вас должно высветиться название вашего окружения (в нашем случае venv)  
Пример на Windows:  
`(venv) PS C:\Users\user\Desktop\html_practice\market--master>`
7. Установите все зависимости с файла requirements.txt командой    
`pip install -r requirements.txt`
8. Теперь можно запускать проект командой  
`python manage.py runserver`
9. Откройте браузер и в поисковой строке введите: http://localhost:8000/catalog/
  
  
  
Подключение PostgreSQL
=====================
### На данный момент наш проект берет данные с файловой БД SQLite, исправим это
1. Установите [PostgreSQL](https://www.postgresql.org/download/) и [pgAdmin](https://www.pgadmin.org/download/)
2. Создайте новую БД в pgAdmin
3. Настройте подключение к новой БД в настройках:  
'ENGINE': 'django.db.backends.postgresql_psycopg2',  
'NAME': 'django_db',  
'USER' : 'user_name',  
'PASSWORD' : 'password',  
'HOST' : '127.0.0.1',  
'PORT' : '5432',
4. Сделайте миграцию всех данных на новую БД  
`python manage.py migrate`
