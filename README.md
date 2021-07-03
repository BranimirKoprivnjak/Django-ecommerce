# Getting started

## Introduction
Simple e-commerce web application created with Django. 

## Prerequisites
This project was developed with:
1. Python 3.8.5
2. Django 3.2.4<br/>

## Running the project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repo and activate ur virtual environment

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate the environment

Mac OS / Linux:
```
source myenv/bin/activate
```

Windows:
```
myenv\Scripts\activate
```

Install the project dependencies with

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Run local server

```
python manage.py runserver
```

## Demo

### Item list
![shop](https://user-images.githubusercontent.com/85017668/124359350-dc6d0e00-dc24-11eb-961e-03a05ec0e920.png)

### Item detail
![item_detail](https://user-images.githubusercontent.com/85017668/124359373-ed1d8400-dc24-11eb-8eea-fd4a781e0e2e.png)

### Cart
![cart](https://user-images.githubusercontent.com/85017668/124359383-f6a6ec00-dc24-11eb-90e8-42ee413c8b66.png)

### Checkout
![checkout](https://user-images.githubusercontent.com/85017668/124359388-fc043680-dc24-11eb-850f-ca4c6b7b88eb.png)

### Payment
![payment](https://user-images.githubusercontent.com/85017668/124359393-01fa1780-dc25-11eb-8430-074ea09509e6.png)

### Login
![login](https://user-images.githubusercontent.com/85017668/124359401-09212580-dc25-11eb-824c-dbd068f697ef.png)

### Sign up
![signup](https://user-images.githubusercontent.com/85017668/124359407-0e7e7000-dc25-11eb-9871-d065e2fa5f50.png)
