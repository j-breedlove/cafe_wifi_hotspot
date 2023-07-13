from app import db


class Hotspot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    wifi_quality = db.Column(db.String(64), index=True, unique=True)
    # wifi_quality = db.Column(db.Integer)
    power_rating = db.Column(db.String(64), index=True, unique=True)
    # has_power = db.Column(db.Boolean)

    def __repr__(self):
        return '<Hotspot {}>'.format(self.name)
