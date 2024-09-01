from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from ziptie.config import DatabaseSettings

database_settings = DatabaseSettings()

engine = create_engine(database_settings.get_url())
local_session = sessionmaker(engine)


class Base(DeclarativeBase):
    """Base class for declarative models."""
