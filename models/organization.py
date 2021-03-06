import sqlalchemy as db
from sqlalchemy.orm import relationship
from models.base import Base, PHMixin
import models.shared_protocol as SharedProtocol


class Organization(PHMixin, Base):
    __tablename__ = 'ph_organizations'

    name = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))

    owner = relationship("User", back_populates="owned_organizations")
    groups = relationship("OrganizationGroup", back_populates="organization")
    mds_links = relationship("OrganizationMDSLink", back_populates="organization")
