from models import User, Role


def check_data_exist():
    return User.query.first()


def gen_admin_data(db):
    admin = User(
        username="admin",
        password="123",
        name="Hejl",
        avatar="https://avatar.52pojie.cn/images/noavatar_small.gif",
    )
    role = Role(title="超级管理员", can_edit=False, description="唯一账号，可以操作系统所有功能")
    admin.roles.append(role)
    db.session.add_all([admin, role])
    db.session.commit()


def gen_user_data(db):
    for i in range(20):
        user = User(username=f"test{i}", password="123", name=f"testname{i}")
        db.session.add(user)
    db.session.commit()


def gen_role_data(db):
    data = [
        {"id": "2", "title": "管理员", "description": "由超管指定，可以为多个，协助超管管理系统"},
        {"id": "3", "title": "人事经理", "description": "主管人事相关业务"},
        {"id": "4", "title": "销售经理", "description": "主管销售相关业务"},
        {"id": "5", "title": "保安队长", "description": "主管安保相关业务"},
        {"id": "6", "title": "员工", "description": "普通员工"},
    ]
    for item in data:
        role = Role(**item)
        db.session.add(role)
    db.session.commit()


def init_data(db):
    if check_data_exist():
        return
    gen_admin_data(db)
    gen_user_data(db)
    gen_role_data(db)
