from models import User, Role, Permission, Article


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
        {"id": "3", "title": "运营", "description": "运营人员"},
        {"id": "4", "title": "测试", "description": "测试人员"},
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
            "permission_name": "所有文章",
            "permission_mark": "articles",
            "permission_desc": "文章列表菜单",
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

    admin_role = Role.query.get(1)
    admin_role.permissions = Permission.query.all()
    db.session.commit()


def gen_article_data(db):
    data = [
        {"title": "ESLint + Git Hooks", "description": "编码规范"},
        {"title": "Tags View", "description": "便签快捷导航功能"},
        {"title": "Element-Plus", "description": "基于 Vue 3.0 的桌面端组件库"},
        {"title": "侧边栏", "description": "根据路由动态生成的 Menu 菜单"},
        {"title": "动态面包屑", "description": "动态生成的面包屑数据"},
        {"title": "权限验证", "description": "页面权限、功能权限、动态权限、权限配置"},
        {"title": "vue-element-admin", "description": "后台前端解决方案"},
        {"title": "Vue3 + 全家桶", "description": "项目基于最新的vue3全家桶进行开发"},
        {"title": "功能引导", "description": "对用户的功能引导"},
        {"title": "架构设计", "description": "架构设计"},
    ]
    for item in data:
        a = Article(**item, author_id=1)
        db.session.add(a)
    db.session.commit()


def init_data(db):
    if check_data_exist():
        return
    gen_admin_data(db)
    gen_user_data(db)
    gen_role_data(db)
    gen_permission_data(db)
    gen_article_data(db)
