from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, registry

metadata_obj = MetaData()
mapper_registry = registry(metadata=metadata_obj)
Base = declarative_base(metadata=metadata_obj)
