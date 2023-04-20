"""initial migration for account table

Revision ID: 60d1844cb5d3
Revises:
Create Date: 2022-12-09 18:25:25.301186

"""
"""import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "60d1844cb5d3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "account",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("email", sa.String(length=64), nullable=False),
        sa.Column("_hashed_password", sa.String(length=1024), nullable=True),
        sa.Column("_hash_salt", sa.String(length=1024), nullable=True),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_logged_in", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("account")
    # ### end Alembic commands ###
"""