This is my first ever project with django channels. the project is mostly similar to the tutorial from django channel's offical documentaion from [here](https://channels.readthedocs.io/). I add login and saving history messages of each room (which requires a model and saving each message to db)


### **Features :**

- sending and reading message in a room .
- seeing the history chat of a room .
- logging in

the only way to create a user instance is by `python manage.py createsuperuser`. 

so install dependencies by `pip install -r requirements.txt` . and then craete your own user instance using this command : `python manage.py createsuperuser` .
