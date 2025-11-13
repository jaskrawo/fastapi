"""add content column to posts table

Revision ID: 62b51ffe247f
Revises: 399a337d303e
Create Date: 2025-11-13 18:17:18.485471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62b51ffe247f'
down_revision: Union[str, Sequence[str], None] = '399a337d303e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
