from sqlalchemy import *
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    nickname = Column(String(50), nullable=False, unique=True, primary_key=True, index=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    hashed_password = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
