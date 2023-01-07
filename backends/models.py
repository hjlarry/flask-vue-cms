import datetime

from sqlalchemy import ForeignKey, String, func, Table, Column, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db


class Base(db.Model):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        insert_default=func.now(), server_onupdate=func.now()
    )


user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(40), unique=True)
    _password: Mapped[str] = mapped_column("password", String(255))
    name: Mapped[str] = mapped_column(String(40))
    avatar: Mapped[str] = mapped_column(String(100), nullable=True, default="")
    roles: Mapped[list["Role"]] = relationship(
        secondary=user_roles, back_populates="users"
    )

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)

    def verify_password(self, password):
        try:
            result = check_password_hash(self.password, password)
        except:
            return False
        return result

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Role(Base):
    __tablename__ = "roles"
    title: Mapped[str] = mapped_column(String(40), unique=True)
    can_edit: Mapped[bool] = mapped_column(Boolean, default=True)
    description: Mapped[str] = mapped_column(String(100), nullable=True, default="")
    users: Mapped[list[User]] = relationship(
        secondary=user_roles, back_populates="roles"
    )
    permissions: Mapped[list["Permission"]] = relationship(secondary=role_permissions)


class Permission(Base):
    __tablename__ = "permissions"
    permission_id = Column("permission_id", db.String(40))
    permission_name = Column("permission_name", db.String(40))
    permission_mark = Column("permission_mark", db.String(40))
    permission_desc = Column("permission_desc", db.String(255))
