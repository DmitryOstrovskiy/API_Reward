### **Reward system for the app Disease Tracker & web application.**

### Description

**The project includes a system of rewards for activity when adding data to the application database: first, the user needs to add data from his electronic wallet, then for each added test card, the user will receive a reward to the balance of his wallet.**
 
### Functionality

- **Registration and Authentication (JWT+Djoser).** Users register using a username and password. The registered user receives a JWT token. It is used for further authentication. Token and user management is implemented using the Djoser library. Further API functionality is available only for authenticated users.
- **Adding wallet data.** The user adds his wallet data to the application database. One user can add only one wallet. When trying to add a second wallet, the user will receive an error message.
- **Adding test cards.** The user can add their test cards to the application database. The number of test cards for the user is unlimited.
- **Reward.** When adding test cards, the user will receive a reward to the balance of his wallet for each added card.
- **Permission.** The user can view information about his wallet and the list of added test cards via a GET request. The user cannot view wallet data or test card data from other users. The user cannot add, update, or delete data from wallets and test cards of other users.

### Technologies

- Python 3.9
- Django 4.2.8
- Django Rest Framework 3.14.0
- djangorestframework-simplejwt 4.7.2
- djoser 2.1.0
- drf-spectacular 0.27.0

### Project launch

Clone the repository and navigate to it in the command line:
```sh
git clone https://github.com/DmitryOstrovskiy/API_Reward && cd API_Reward
```
Install the virtual environment, activate it and install dependencies:
```sh
python -m venv venv && Windows: ```source venv\scripts\activate```; Linux/Mac: ```sorce venv/bin/activate``` && pip install -r requirements.txt
```
Perform migrations:
```sh
python manage.py migrate
```
Create a superuser:
```sh
python manage.py createsuperuser
```
Start the server:
```sh
python manage.py runserver
```

###  The project is launched at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/schema/swagger-ui/ - project Swagger UI documentation
- http://127.0.0.1:8000/api/schema/redoc/ - project documentation
- http://127.0.0.1:8000/admin/ - admin page


### Query examples

### _Registration of the user_
**POST**: http://127.0.0.1:8000/auth/users/

Request example:
```json
{
    "username": "newuser4",
    "password": "Changeme4!"
}
```
Response example:
```json
{
    "email": "",
    "username": "newuser4",
    "id": 5
}
```

### _Getting a JWT token_
**POST**: http://127.0.0.1:8000/auth/jwt/create/   
Request example:
```json
{
    "username": "newuser4",
    "password": "Changeme4!"
} 
```
Response example:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMzc2OTc3MywianRpIjoiZDEwYTQ2NGE0ODg3NDhjYzlkYjQxZmJhNGRhNDU3ZTIiLCJ1c2VyX2lkIjo1fQ.fjB-bMNBGc2funKhLndge-1wEaQ4fSL_YaDZk6Nc49Q",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNzY5NzczLCJqdGkiOiI0ODdiNjgyNWViNGM0OGY1OTA5NTc0MmNhYzllYzI1MCIsInVzZXJfaWQiOjV9.tALtVLcENL3_rIwpO2z0phk-3xICdornj8SH_dXAv-M"
}
```
### Further functionality is available only to authenticated users. In Postman, you need to select the "Bearer Token" authorization type in the Authorization tab and specify the JWT token already there. You need to take an access token. 

### _Adding wallet data_
**POST**: http://127.0.0.1:8000/api/v1/wallet/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
    "wallet_address": "QAZWSXEDC1234567890qaz0",
    "private_key": "private_key3",
    "public_key": "public_key3",
    "mnemonic_phrase": "phrase3"
}
```
Response example:
```json
{
    "id": 3,
    "wallet_address": "QAZWSXEDC1234567890qaz0",
    "wallet_balance": 0,
    "private_key": "private_key3",
    "public_key": "public_key3",
    "mnemonic_phrase": "phrase3",
    "user": 5
}
```

### _Adding test card data_
**POST**: http://127.0.0.1:8000/api/v1/testcards/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
    "name": "tescard15",
    "parameter": "parameter15",
    "parameter_value": "parameter_value15"
}
```
Response example:
```json
{
    "id": 17,
    "name": "tescard15",
    "parameter": "parameter15",
    "parameter_value": "parameter_value15",
    "pub_date": "2023-12-27T13:35:42.151752Z",
    "author": 5
}
```

### _Getting wallet data_
**GET**: http://127.0.0.1:8000/api/v1/wallet/ - In the Authorization tab, you need to pass an access token

Response example:
```json
[
    {
        "id": 1,
        "wallet_address": "QAZWSXEDC1234567890",
        "wallet_balance": 4,
        "private_key": "private_key1",
        "public_key": "public_key1",
        "mnemonic_phrase": "phrase1",
        "user": 2
    }
]
```

### _Getting testcdrds data_
**GET**: http://127.0.0.1:8000/api/v1/testcsrds/ - In the Authorization tab, you need to pass an access token

Response example:
```json
[
    {
        "id": 2,
        "name": "tescard2",
        "parameter": "parameter2",
        "parameter_value": "parameter_value2",
        "pub_date": "2023-12-26T14:50:43.888915Z",
        "author": 3
    },
    {
        "id": 3,
        "name": "tescard3put",
        "parameter": "parameter3put",
        "parameter_value": "parameter_value3put",
        "pub_date": "2023-12-26T15:11:13.629509Z",
        "author": 3
    },
    {
        "id": 16,
        "name": "tescard10",
        "parameter": "parameter10",
        "parameter_value": "parameter_value10",
        "pub_date": "2023-12-27T08:02:09.908519Z",
        "author": 3
    }
]
```

### Author - Dmitry Ostrovsky

# 💫 About Me:
🔭 I am currently working on Django projects<br>👯 I’m looking to collaborate on<br>🤝 I’m looking for help with<br>🌱 I am currently learning how to work with FastAPI<br>💬 Ask me about<br>⚡ Fun fact


## 🌐 Socials:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/DmitriyOstrovskiy) 

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=DmitryOstrovskiy&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=DmitryOstrovskiy&theme=tokyonight&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=DmitryOstrovskiy&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

---
[![](https://visitcount.itsvg.in/api?id=DmitryOstrovskiy&icon=0&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->