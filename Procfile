web: gunicorn mysite.wsgi --log-file -
web: npm install
release: python manage.py collectstatic -v0 --noinput
release: python manage.py migrate