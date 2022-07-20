# Pre-setup

## Create a virtual environment

```
python3 -m venv venv
```

## Activate the virtual environment

```
source venv/bin/activate
```

## Install requirements

```
pip install -r requirements.txt
```

# Usage

## Apply the migrations

```
python manage.py migrate
```

## Run the project

```
python manage.py runserver
```

## Home page

```
http://127.0.0.1:8000/
```

## Create a user

```
http://127.0.0.1:8000/reg/
```

## Login

Enter your credentials at ```url``` below:

```
http://127.0.0.1:8000/login/
```

## All posts

```
http://127.0.0.1:8000/blog/
```

## Detail view for post

```
http://127.0.0.1:8000/blog/post_id
```

Where ```post_id``` is the unique id for the each post.

## Profile page, where you can edit your user:

```
http://127.0.0.1:8000/profile/
```

## Create an admin.

From admin user you can create posts which will be shown in the blog page. To create admin user, run the command:

```
python manage.py createsuperuser
```

Then, enter credentials for the admin user.
