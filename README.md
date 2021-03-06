Twilio API App
--------

**Description**

This app allows users to send a message to anyone from their computer.


### Technology Stack

**Application:** Python, Flask, SQLAlchemy, PostgreSQL, Twilio API    
**Front-End**: HTML/CSS


### How to run this app locally


Create a virtual environment 

```
> virtualenv env
> source env/bin/activate
```

Install the dependencies

```
> pip install -r requirements.txt
```

Create Twilio account to get authentication for API usage. Then create a secrets.sh file inputting your credentials

```
export TWILIO_ACCOUNT_SID="[input your sid here]"
export TWILIO_AUTH_TOKEN="[input your auth token here]"
export TWILIO_PHONE_NUMBER="[input your twilio phone number here]"
```

Run this line in your terminal (You will need to re-run this every time)

```
> source secrets.sh
```

Install PostgreSQL 9.6.2 with homebrew and set up the database

```
> brew install postgresql
> createdb twilio_app
> python model.py
```

In a new Terminal run App

```
> python server.py
```

Open your browser and navigate to 

```
http://localhost:5000/
```


### About the Developer    
Emily Flagg  
[Linkedin](https://www.linkedin.com/in/emilyflagg)    