import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'PKMS.settings'

import django
django.setup()

from app.models import Post, Para
from users.models import CustomUser

def populate() -> None:
    u1 = CustomUser.objects.create_user('username1', 'jab@gmail.com', 'password1')
    u2 = CustomUser.objects.create_user('username2', 'nick@gmail.com', 'password2')

    # u1: post1-p1-p2-p3
    post1 = Post.objects.create(owner=u1)
    p1 = Para.objects.create(content="This is the first paragraph")
    p2 = Para.objects.create(content="I'm the SECOND paragraph")
    p3 = Para.objects.create(content="3nd paragraph here")
    p1.link_to(post=post1)
    p2.link_to(predecessor=p1)
    p3.link_to(predecessor=p2)

    # u2: post2-p4
    post2 = Post.objects.create(owner=u2)
    p4 = Para.objects.create(content="I'm the first paragraph for another user")
    p4.link_to(post=post2)

    # u3: post3-p5-p6
    post3 = Post.objects.create(owner=u1)
    p5 = Para.objects.create(content="another post for the first user")
    p5.link_to(post=post3)
    p6 = Para.objects.create(content="lastes paragraph")
    p6.link_to(predecessor=p5)

if __name__ == '__main__':
    populate()