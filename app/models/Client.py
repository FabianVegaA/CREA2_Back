from app.__init__ import db, ma
from marshmallow import post_load

class ClientModel(db.Model):
    __tablename__ = "Client"
    pk_id_client = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    user = db.Column(db.String(45), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    fk_id_client = db.Column(db.Integer, db.ForeignKey("Client.pk_idClient"))

    def __repr__(self):
        return "<{}:{}:{}>".format(self.pk_id_client, self.user, self.active)


class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel
        include_fk = True

    @post_load
    def make_client(self, data, **kwargs):
        return ClientModel(**data)
