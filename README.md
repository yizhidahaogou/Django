1.кройте терминал в корневой папке проекта и выполните: python -m venv venv
2.Активируйте виртуальное окружение： .\venv\Scripts\Activate.ps1
3.Установите зависимости： pip install -r requirements.txt
4.Инициализируйте базу данных： python manage.py makemigrations
python manage.py migrate
5.Создайте суперпользователя ：python manage.py createsuperuser
6.Запустите сервер разработки：python manage.py runserver
