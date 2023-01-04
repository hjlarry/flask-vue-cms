from models import User, Role


def check_data_exist():
    return User.query.first()


def gen_admin_data(db):
    admin = User(
        username="admin",
        password="123",
        name="Hejl",
        avatar="https://avatar.52pojie.cn/data/avatar/001/15/47/76_avatar_small.jpg",
    )
    role = Role(name="超级管理员", can_edit=False)
    admin.roles.append(role)
    db.session.add_all([admin, role])
    db.session.commit()


def gen_user_data(db):
    for i in range(100):
        user = User(username=f"test{i}", password="123", name=f"testname{i}")
        db.session.add(user)
    db.session.commit()


def init_data(db):
    if check_data_exist():
        return
    gen_admin_data(db)
    gen_user_data(db)
