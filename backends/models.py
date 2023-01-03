from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer,Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

import datetime

from ext import db

class Base(db.Model):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at:Mapped[datetime.datetime] = mapped_column(insert_default=func.now())
    updated_at:Mapped[datetime.datetime] = mapped_column(insert_default=func.now(),server_onupdate=func.now() )

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
    password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(40))
    avatar: Mapped[str] = mapped_column(String(100), nullable=True)
    roles: Mapped[list['Role']] = relationship(secondary=user_roles, back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

class Role(Base):
    __tablename__ = "roles"
    name: Mapped[str] = mapped_column(String(40), unique=True)
    can_edit: Mapped[bool] = mapped_column(Boolean, default=True)
    users: Mapped[list[User]] = relationship(secondary=user_roles, back_populates="roles")
    permissions: Mapped[list['Permission']] = relationship(secondary=role_permissions)


class Permission(Base):
    __tablename__ = "permissions"
    permission_id = Column("permission_id", db.String(40))
    permission_name = Column("permission_name", db.String(40))
    permission_mark = Column("permission_mark", db.String(40))
    permission_desc = Column("permission_desc", db.String(255))