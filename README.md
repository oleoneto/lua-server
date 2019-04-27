# lua-server
Backend server for Lua LMS

### Requirements
As listed in [requirements.txt](requirements.txt)

### Secrets
In order to run the project, create a `secrets.py` file next to `settings.py`. 
This file should contain the following configuration:

```python
ADMINS = (
    ('Name', 'email@example.com'),
)
```

You will also need to export the following variables:
```text
# Use to override ALLOWED_HOSTS and to enable use of secrets.py file for ADMINS
LOCAL_MACHINE=True

# User account that should receive error logs in production
ADMINS="(('Your Name', 'name@example.com'),)"

# The project uses S3 storage. 
# This is needed for static and media files to work
AWS_BUCKET_NAME=''
AWS_LOCATION=''
AWS_STATIC_LOCATION=''
AWS_MEDIA_LOCATION=''
AWS_PRIVATE_MEDIA_LOCATION=''
AWS_REGION_NAME=''
AWS_ORIGIN=''
AWS_ENDPOINT=''
AWS_ENDPOINT_URL=''
AWS_CUSTOM_DOMAIN=''
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''

# -----------------------
# -----------------------
# Optional. Used with 2FA
# -----------------------
TWILIO_SID=''
TWILIO_TOKEN=''
TWILIO_CALLER_ID=''
```


### API
In order to access the API, please provide your authentication `token`. 
Include it in the request header:
```text
http GET 'http://localhost:8000/api/v1/users' \
    'Authorization':'Token 8g*****************1'
```

The API also supports JWT authentication. The endpoint is at:
```text

```

The documentation of the API is at the following path:
```text
http://localhost:8000/api/v1/documentation
```

The project uses Swagger to display the endpoints and provide 
a way of interacting with the resources.


### Two-Factor Authentication
2FA is required for admin site, but optional for te rest of the site.

Check 2FA status for a given user:
```
manage.py two_factor_status username
```

Disable 2FA for a given user:
```
manage.py two_factor_disable username
```

### Build and run application
```text
manage.py makemigrations core && \
manage.py migrate core && \
manage.py migrate && \
manage.py runserver
```


Built by **Leo Neto** with [Django CLI](https://github.com/oleoneto/Django-CLI)
