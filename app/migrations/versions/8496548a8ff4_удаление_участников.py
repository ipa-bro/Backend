"""Удаление участников

Revision ID: 8496548a8ff4
Revises: b2e18d2d8862
Create Date: 2024-05-07 18:37:24.752498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8496548a8ff4'
down_revision: Union[str, None] = 'b2e18d2d8862'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    op.alter_column('events', 'photoUrl',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'photoUrl',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_table('members',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date_of_birthday', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='members_pkey')
    )
    # ### end Alembic commands ###
