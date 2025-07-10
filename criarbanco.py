from WeltImage import database, app
from WeltImage.models import Usuario, Foto

with app.app_context():
    database.create_all()