from shared import db

# An article is basically any hunk of text that needs revisions.
class Article(db.Model):
    __tablename__ = 'Articles'

    id = db.Column(db.Integer,primary_key=True)
    article_name = db.Column(db.String) # E.G. PressureZone_ExternalLinks
    revisions = db.relationship("Revision")

    def get_active_revision(self):
        pass