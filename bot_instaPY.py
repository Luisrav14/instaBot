import getpass
from instapy import InstaPy

username = input('Ingresa nombre se usuario Instagram: ')
password = getpass.getpass('Ingresa contraseña: ')

session = InstaPy(username, password)
session.login()
session.set_comments(False)
session.set_do_follow(enabled=True, percentage=100)
session.like_by_tags(["bmw", 'tesla'], amount=5)
session.end()
