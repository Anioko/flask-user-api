from user import db

class Profile(db.Document):
	user_email = db.EmailField(unique=True)
    school = db.StringField()
    lol_id = db.StringField()
    dota_id = db.StringField()

