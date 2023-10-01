def is_admin(user):
    return user.groups.filter(name='Admins').exists()

def is_user(user):
    return user.groups.filter(name='Users').exists()