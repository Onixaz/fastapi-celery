"""add tags table

Revision ID: a04d79012711
Revises: dba4f311e944
Create Date: 2024-07-01 23:06:16.224606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a04d79012711'
down_revision: Union[str, None] = 'dba4f311e944'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('booktag',
    sa.Column('book_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('tag_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.uid'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.uid'], ),
    sa.PrimaryKeyConstraint('book_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booktag')
    op.drop_table('tags')
    # ### end Alembic commands ###
