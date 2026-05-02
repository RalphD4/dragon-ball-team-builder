from data.universe import ADMINS


def add_admin(admin):
    if admin.username not in ADMINS_BY_USERNAMES:
        ADMINS.append(admin)
        ADMINS_BY_USERNAMES[admin.username] = admin
    else:
        raise Exception("This user already exists")
    

def promote_admin(name, new_type):
    if name not in ADMINS_BY_USERNAMES:
        raise Exception("User does not exist")
    else:
        admin = ADMINS_BY_USERNAMES.get(name)
        admin.admin_type = new_type


def del_admin(name):
    if name not in ADMINS_BY_USERNAMES:
        raise Exception("User does not exist")
    else:
        admin = ADMINS_BY_USERNAMES.get(name)
        ADMINS.remove(admin)
        del ADMINS_BY_USERNAMES[name]


ADMINS_BY_USERNAMES = {admin.username: admin for admin in ADMINS}