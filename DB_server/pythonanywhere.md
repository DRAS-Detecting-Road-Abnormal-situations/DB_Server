pythonanywhere에 웹앱 게시

$ git clone https://github.com/chea-young/deploy_pushserver.git cheayoung.pythonanywhere.com
mkvirtualenv --python=python3.6 cheayoung.pythonanywhere.com
pip install 'django<2'
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic

`/home/cheayoung/cheayoung.pythonanywhere.com/static`

git clone https://github.com/chea-young/deploy_pushserver.git
virtualenv --python=python3.6 myvenv
source myvenv/bin/activate
python manage.py migrate
python manage.py createsuperuser

/home/cheayoung/deploy_pushserver/myvenv/