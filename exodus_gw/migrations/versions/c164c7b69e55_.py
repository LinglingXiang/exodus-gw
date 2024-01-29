"""Add updated column to publishes and tasks

Revision ID: c164c7b69e55
Revises: 854e06069e65
Create Date: 2021-02-23 17:49:13.493461

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c164c7b69e55"
down_revision = "854e06069e65"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "publishes",
        sa.Column("updated", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "tasks",
        sa.Column("updated", sa.DateTime(timezone=True), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.drop_column("updated")

    with op.batch_alter_table("publishes") as batch_op:
        batch_op.drop_column("updated")
