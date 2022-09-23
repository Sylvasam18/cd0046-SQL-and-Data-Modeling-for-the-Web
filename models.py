from app import db


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    address = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    website_link = db.Column(db.String(), nullable=True)
    facebook_link = db.Column(db.String(), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(), nullable=True)
    image_link = db.Column(db.String(), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=False)
    
    def __repr__(self):
          return f'<Venue {self.id} {self.name}>'
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    website_link = db.Column(db.String(), nullable=True)
    facebook_link = db.Column(db.String(), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(), nullable=True)
    image_link = db.Column(db.String(), nullable=False)
    shows = db.relationship('Show', backref='artist', lazy=False)
    
    def __repr__(self):
          return f'<Artist {self.id} {self.name}>'
        
class Show(db.Model):
  _tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)

  def __repr__(self):
    return f'<Show {self.id} {self.start_time}>'
