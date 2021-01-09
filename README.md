# Push-Notification-Server

- ### Yolo-Server Yolo 모델을 이용하여 도로 위 이상현상(교통사고, 장애물)을 감지하였을 때 감지되었을 때의 이미지가 캡쳐되어 HTTP Post로 전송되어 오면 DB에 사진을 저장한다. 또한 이 사진이 교통사고를 감지하는 Flask 서버에서 왔을 경우 사전에 저장되어 있던 Web application의 토큰으로 FCM(Firebase clouding messaging)을 보낸다.

- 이 Web server는 pythonanywhere를 통해 deploy를 하여 Web application에서 알림을 보여줄 때 해당 서버의 DB에서 URL로 이미지를 가져와서 사용할 수 있도록 한다.

### pythonanywhere에 Web application depoly 방법
 ####  <pythonanywhere console 창에서>
    - git clone https://github.com/chea-young/deploy_pushserver.git
    - virtualenv --python=python3.6 myvenv
    - source myvenv/bin/activate
    - python manage.py migrate
    - python manage.py createsuperuser
    - pip install requirement.txt
    - /home/cheayoung/deploy_pushserver/myvenv/

#### 해당 Web application이 배포된 URL : http://chaeyoung.pythonanywhere.com/
 - http://chaeyoung.pythonanywhere.com/admin -> ID : iceboat, password : 1234
 - DB에 도로 위 이상현상(교통사고, 장애물)이 감지되었을 때의 전송받은 이미지가 저장되어있는 것을 확인 할 수 있습니다.