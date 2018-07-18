from sqlalchemy import Column, Float, ForeignKey, Integer, String

from pricing_service import db


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    sku = Column(String(5), unique=True)
    name = Column(String(30))
    price = Column(Integer)
    vatband_id = Column(Integer, ForeignKey('vatband.id'),
        nullable=False)
    vatband = db.relationship('VATBand',
        backref=db.backref('product', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.sku


class VATBand(db.Model):
    __tablename__ = 'vatband'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    rate = Column(Float)

    def __repr__(self):
        return '<VATBand %r>' % self.name
