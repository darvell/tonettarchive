from shared import db

class Revision(db.Model):
    __tablename__ = 'Revisions'

    id = db.Column(db.Integer,primary_key=True)
    parent_article = db.Column(db.Integer, db.ForeignKey('Articles.id'))
    is_current_revision = db.Column(db.Boolean)
    is_worthy = db.Column(db.Boolean) # An admin has checked whether it's good or not
    revision_content = db.Column(db.String)
    # user = db.Column()
    # submitted_date = db.Column()