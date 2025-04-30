import os
from django.contrib.auth import get_user_model

User = get_user_model()

# 从环境变量中获取用户名、邮箱和密码
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f'Superuser {username} created.')
    else:
        print(f'Superuser {username} already exists.')