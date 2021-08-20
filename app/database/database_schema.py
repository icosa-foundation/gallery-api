import sqlalchemy
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from sqlalchemy import (
    Column, 
    BigInteger, 
    String, 
    Binary, 
    Text, 
    ForeignKey, 
    Boolean,
    Integer
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import JSON

Base = declarative_base()

class BaseTable(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)

class ClientTable(BaseTable):
    __tablename__ = "users"

    url = Column(String(255), nullable = False)
    email = Column(String(255), nullable = False)
    password = Column(Binary, nullable = False)
    displayname = Column(sqlalchemy.VARCHAR(50), nullable=False)
    description = Column(Text)

class AssetsTable(BaseTable):
    __tablename__ = "assets"

    url = Column(String(255), nullable = False)
    name = Column(String(255), nullable = False)
    owner = Column(BigInteger, ForeignKey('users.id'), nullable = False)
    description = Column(Text)
    formats = Column(JSONB, nullable = False)
    visibility = Column(String(255), nullable = False)
    curated = Column(Boolean)
    polyid = Column(String(255))
    polydata = Column(JSONB)
    thumbnail = Column(Text)

class ExpandedAssetsTable(AssetsTable):
    __tablename__ = "expandedassets"

    ownername = Column(String(255))
    ownerurl = Column(String(255))

#Oauth2

class ClientTable(BaseTable):
    __tablename__ = "oauth2_client"

    client_id = Column(String)
    client_secret = Column(String)
    grant_types = Column(ARRAY(String))
    response_types = Column(ARRAY(String))
    redirect_uris = Column(ARRAY(String))
    scope = Column(String)


class AuthorizationCodeTable(BaseTable):
    __tablename__ = "oauth2_code"

    code = Column(String)
    client_id = Column(String)
    redirect_uri = Column(String)
    response_type = Column(String)
    scope = Column(String)
    auth_time = Column(Integer)
    expires_in = Column(Integer)
    code_challenge = Column(String)
    code_challenge_method = Column(String)
    nonce = Column(String)

    user_id = Column(
        BigInteger,
        nullable=False,
    )


class TokenTable(BaseTable):
    __tablename__ = "oauth2_token"

    access_token = Column(String)
    refresh_token = Column(String)
    scope = Column(String)
    issued_at = Column(Integer)
    expires_in = Column(Integer)
    refresh_token_expires_in = Column(Integer)
    client_id = Column(String)
    token_type = Column(String)
    revoked = Column(Boolean)

    user_id = Column(
        BigInteger,
        nullable=False,
    )

# users = sqlalchemy.Table("users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True),
#     sqlalchemy.Column("url", sqlalchemy.VARCHAR(255), nullable=False),
#     sqlalchemy.Column("email", sqlalchemy.VARCHAR(255), nullable=False),
#     sqlalchemy.Column("password", sqlalchemy.Binary),
#     sqlalchemy.Column("displayname", sqlalchemy.VARCHAR(50), nullable=False),
#     sqlalchemy.Column("description", sqlalchemy.TEXT),
# )

# assets = sqlalchemy.Table("assets",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True),
#     sqlalchemy.Column("url", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("name", sqlalchemy.VARCHAR(255), nullable=False),
#     sqlalchemy.Column("owner", sqlalchemy.BigInteger, sqlalchemy.ForeignKey("users.id"), nullable=False),
#     sqlalchemy.Column("description", sqlalchemy.TEXT),
#     sqlalchemy.Column("formats", sqlalchemy.dialects.postgresql.JSONB, nullable=False),
#     sqlalchemy.Column("visibility", sqlalchemy.VARCHAR(255), nullable=False),
#     sqlalchemy.Column("curated", sqlalchemy.BOOLEAN),
#     sqlalchemy.Column("polyid", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("polydata", sqlalchemy.dialects.postgresql.JSONB),
#     sqlalchemy.Column("thumbnail", sqlalchemy.TEXT),
# )

# expandedassets = sqlalchemy.Table("expandedassets",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.BigInteger),
#     sqlalchemy.Column("url", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("name", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("owner", sqlalchemy.BigInteger),
#     sqlalchemy.Column("ownername", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("ownerurl", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("formats", sqlalchemy.dialects.postgresql.JSONB),
#     sqlalchemy.Column("description", sqlalchemy.TEXT),
#     sqlalchemy.Column("visibility", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("curated", sqlalchemy.BOOLEAN),
#     sqlalchemy.Column("polyid", sqlalchemy.VARCHAR(255)),
#     sqlalchemy.Column("polydata", sqlalchemy.dialects.postgresql.JSONB),
#     sqlalchemy.Column("thumbnail", sqlalchemy.TEXT),
# )
