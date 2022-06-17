'''
Create Project
1. Always use a new app for the User. Create the model class for the new User.
2. Set the AUTH_USER_MODEL in settings.py -->> AUTH_USER_MODEL = 'app_name.app_nameUser'
        example AUTH_USER_MODEL = 'accounts.PetstagramUser'

3. Create file 'managers.py' in the new app. Go to "User -> AbstractUser -> UserManager and copy
    the 3 methods 'create user' and 'create superuser'. Delete args we don't need (email for exmpl).
    Write objects = app_nameUserManager(). i.e. objects = PetstagramUserManager(). Drop the DB and
    make migrations again

4. Create register/log in forms.
5. In models next to 'profile' add UserModel = get_user_model() and inside add a relation to current user
 -> user = models.OneToOneFieldUserModel,
        on_delete=models.CASCADE,
        primary_key=True,)



'''