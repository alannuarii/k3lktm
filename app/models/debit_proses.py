from app import db

class DebitProses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    debit = db.Column(db.Float, nullable=False)
    tanggal = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<{}. {} = {}>'.format(self.id, self.tanggal, self.debit)