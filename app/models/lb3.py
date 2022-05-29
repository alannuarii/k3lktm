from app import db

class LB3(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jenis_limbah = db.Column(db.String(250), nullable=False)
    konstanta = db.Column(db.Float, nullable=False)
    satuan_awal = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<{}>'.format(self.jenis_limbah)