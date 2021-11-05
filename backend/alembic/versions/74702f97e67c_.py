"""empty message

Revision ID: 74702f97e67c
Revises: 
Create Date: 2021-11-05 18:14:57.594106

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from app.models import StudyState

# revision identifiers, used by Alembic.
revision = '74702f97e67c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diagnosis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_diagnosis_id'), 'diagnosis', ['id'], unique=False)
    op.create_table('healthinsurance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('telephone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_healthinsurance_email'), 'healthinsurance', ['email'], unique=True)
    op.create_index(op.f('ix_healthinsurance_id'), 'healthinsurance', ['id'], unique=False)
    op.create_index(op.f('ix_healthinsurance_name'), 'healthinsurance', ['name'], unique=False)
    op.create_index(op.f('ix_healthinsurance_telephone'), 'healthinsurance', ['telephone'], unique=False)
    op.create_table('referringphysician',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('license', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_referringphysician_id'), 'referringphysician', ['id'], unique=False)
    op.create_index(op.f('ix_referringphysician_license'), 'referringphysician', ['license'], unique=True)
    op.create_table('typestudy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('study_consent_template', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('study_consent_template')
    )
    op.create_index(op.f('ix_typestudy_id'), 'typestudy', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('license', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('dni', sa.Integer(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('health_insurance_number', sa.Integer(), nullable=True),
    sa.Column('health_insurance_id', sa.Integer(), nullable=True),
    sa.Column('clinical_history', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['health_insurance_id'], ['healthinsurance.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dni'),
    sa.UniqueConstraint('license'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('study',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('referring_physician_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('type_study_id', sa.Integer(), nullable=True),
    sa.Column('presumptive_diagnosis_id', sa.Integer(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('current_state', sqlalchemy_utils.types.choice.ChoiceType(StudyState), nullable=True),
    sa.Column('current_state_entered_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['presumptive_diagnosis_id'], ['diagnosis.id'], ),
    sa.ForeignKeyConstraint(['referring_physician_id'], ['referringphysician.id'], ),
    sa.ForeignKeyConstraint(['type_study_id'], ['typestudy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_study_id'), 'study', ['id'], unique=False)
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('study_id', sa.Integer(), nullable=True),
    sa.Column('reporting_physician_id', sa.Integer(), nullable=True),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('date_report', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('report', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['reporting_physician_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['study_id'], ['study.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report_id'), 'report', ['id'], unique=False)
    op.create_table('studyhistory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('study_id', sa.Integer(), nullable=True),
    sa.Column('state', sqlalchemy_utils.types.choice.ChoiceType(StudyState), nullable=True),
    sa.Column('state_entered_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['study_id'], ['study.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_studyhistory_id'), 'studyhistory', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_studyhistory_id'), table_name='studyhistory')
    op.drop_table('studyhistory')
    op.drop_index(op.f('ix_report_id'), table_name='report')
    op.drop_table('report')
    op.drop_index(op.f('ix_study_id'), table_name='study')
    op.drop_table('study')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_typestudy_id'), table_name='typestudy')
    op.drop_table('typestudy')
    op.drop_index(op.f('ix_referringphysician_license'), table_name='referringphysician')
    op.drop_index(op.f('ix_referringphysician_id'), table_name='referringphysician')
    op.drop_table('referringphysician')
    op.drop_index(op.f('ix_healthinsurance_telephone'), table_name='healthinsurance')
    op.drop_index(op.f('ix_healthinsurance_name'), table_name='healthinsurance')
    op.drop_index(op.f('ix_healthinsurance_id'), table_name='healthinsurance')
    op.drop_index(op.f('ix_healthinsurance_email'), table_name='healthinsurance')
    op.drop_table('healthinsurance')
    op.drop_index(op.f('ix_diagnosis_id'), table_name='diagnosis')
    op.drop_table('diagnosis')
    # ### end Alembic commands ###