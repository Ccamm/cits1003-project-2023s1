from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registrations(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    reason = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    address = db.Column(db.String(64), unique=True, nullable=False)
    approved = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'<Registration id={self.id} name={self.name} >'

def db_init(flag: str):
    db.drop_all()
    db.create_all()

    registrations = [
        Registrations(
            name='Mumble', 
            reason='The humans are stealing my fish and my dancing isn\'t working :(',
            email=f'mumble@penguin.com',
            address=f'123 {flag} Street, Antarctica'
        ),
        Registrations(
            name='Skipper',
            reason='Humans are incapable at looking after themselves. We need a new world order!',
            email='skipper@futureworldleader.aq',
            address='You didn\'t see anything...'
        ),
        Registrations(
            name='Pingu',
            reason='noot noot',
            email='pingu@nootnoot.com',
            address='42 Noot Noot Avenue, Antarctica'
        )
    ]

    db.session.add_all(registrations)
    db.session.commit()
