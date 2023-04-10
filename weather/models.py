from app import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    weather_description = db.Column(db.String(500))

    def __repr__(self):
        return f'<Weather {self.id}>'

    @classmethod
    def get_recent_posts(cls, lat, lon, page):
        per_page = 10
        radius = 50000  # meters
        point = f'POINT({lon} {lat})'
        posts = cls.query.filter(
            func.ST_DWithin(cls.location, point, radius)
        ).order_by(cls.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        return posts
