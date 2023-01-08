from models import User, Role, Permission


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


def gen_permission_data(db):
    child1 = [
        {
            "permission_id": "1-1",
            "permission_name": "分配角色",
            "permission_mark": "distributeRole",
            "permission_desc": "为员工分配角色",
        },
        {
            "permission_id": "1-2",
            "permission_name": "导入员工",
            "permission_mark": "importUser",
            "permission_desc": "通过 excel 导入员工",
        },
        {
            "permission_id": "1-3",
            "permission_name": "删除员工",
            "permission_mark": "removeUser",
            "permission_desc": "删除员工",
        },
    ]
    child2 = {
        "permission_id": "2-1",
        "permission_name": "分配权限",
        "permission_mark": "distributePermission",
        "permission_desc": "为角色分配权限",
    }
    menu_data = [
        {
            "permission_id": "1",
            "permission_name": "员工管理",
            "permission_mark": "userManage",
            "permission_desc": "员工管理菜单",
        },
        {
            "permission_id": "2",
            "permission_name": "角色列表",
            "permission_mark": "roleList",
            "permission_desc": "角色列表菜单",
        },
        {
            "permission_id": "3",
            "permission_name": "权限列表",
            "permission_mark": "permissionList",
            "permission_desc": "权限列表菜单",
        },
        {
            "permission_id": "4",
            "permission_name": "文章排名",
            "permission_mark": "articleRanking",
            "permission_desc": "文章排名菜单",
        },
        {
            "permission_id": "5",
            "permission_name": "创建文章",
            "permission_mark": "articleCreate",
            "permission_desc": "创建文章页面",
        },
    ]
    for item in menu_data:
        permission = Permission(**item)
        db.session.add(permission)
    db.session.commit()
    for item in child1:
        p1 = Permission.query.get(1)
        permission = Permission(**item)
        p1.children.append(permission)
    db.session.commit()

    p2 = Permission.query.get(2)
    permission = Permission(**child2)
    p2.children.append(permission)
    db.session.commit()


def init_data(db):
    if check_data_exist():
        return
    gen_admin_data(db)
    gen_user_data(db)
    gen_role_data(db)
    gen_permission_data(db)
