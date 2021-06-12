from app.__init__ import db, ma
from marshmallow import post_load


class ServiceModel(db.Model):
    __tablename__ = "Service"
    pk_id_service = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    amount = db.Column(db.Integer)
    service_price = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<{}:{}:{}:{}>".format(
            self.pk_id_service, self.name, self.service_price, self.active
        )


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceModel
        include_fk = True

    @post_load
    def make_service(self, data, **kwargs):
        return ServiceModel(**data)
