import json
from flask import Flask, request
from mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"]={
    "host": "mongodb://localhost/youtubedb"
}
db = MongoEngine(app)


class siswa(db.Document):
    name = db.StringField(max_length = 150)
    email = db.StringField()
    addres = db.DictField()
    created_at = db.DateTimeField()


@app.route('/')
def selamatdatangUser():
    return "selamat pagi dunia"

@app.route('/create_siswa', methods=["POST"])
def createsiswa():
    data = request.json
    siswa = siswa(**data).save()
    return siswa.to__json()


if __name__ == "__main__":
    app.run()