from shared import db 

class Song(db.Model):
    __tablename__ = 'Songs'

    id = db.Column(db.Integer,primary_key=True)

    song_name = db.Column(db.String)

    song_lyrics = db.relationship("Article", uselist=False, backref="Song")
    external_links = db.relationship("Article", uselist=False, backref="Song")

    comments = db.relationship("Comment")