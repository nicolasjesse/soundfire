from app.models.Profile import Profile


class Admin(Profile):
    def __init__(self, code, name, email, password, picture):
        Profile.__init__(self, code, name, email, password, picture)
