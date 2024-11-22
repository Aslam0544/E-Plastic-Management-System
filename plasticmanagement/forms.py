from django.forms import CharField, Form, PasswordInput, FileField

class UserForm(Form):
    username = CharField(max_length=50)
    name = CharField(max_length=50)
    password = CharField(max_length=50)
    mobile = CharField(max_length=50)
    address = CharField(max_length=50)
    usertype = CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

class WastageForm(Form):
    wastagename =CharField(max_length=50)
    image =FileField()
    cost = CharField(max_length=50)
    quantity =CharField(max_length=50)
    address = CharField(max_length=50)
    category = CharField(max_length=50)
    collectiondate = CharField(max_length=50)