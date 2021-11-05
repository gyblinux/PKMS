import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'PKMS.settings'

import django
django.setup()

from app.models import Post, Para
from users.models import CustomUser

def populate() -> None:
    u1 = CustomUser.objects.create_user('username1', 'jab@gmail.com', 'password1')
    u2 = CustomUser.objects.create_user('username2', 'nick@gmail.com', 'password2')
    post = Post.objects.create(owner=u1)
    p1 = Para.objects.create(content="This is the first paragraph")
    p2 = Para.objects.create(content="I'm the SECOND paragraph")
    p3 = Para.objects.create(content="3nd paragraph here")
    p1.link_to(post=post)
    p2.link_to(predecessor=p1)
    p3.link_to(predecessor=p2)

if __name__ == '__main__':
    populate()