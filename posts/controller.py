from app import db
from .models import Post
from sqlalchemy.sql import text
from sqlalchemy import func

class PostController:
    @staticmethod
    def create_post(title, content):
        post = Post(title=title, content=content,lat=lat, lon=lon)

        db.session.add(post)
        db.session.commit()

    @classmethod
    def get_recent_posts(cls, lat, lon, page):
        per_page = 10
        radius = 50000  # meters
        point = f'POINT({lon} {lat})'
        posts = db.session.query(Post).filter(
            func.ST_DWithin(Post.location, point, radius)
        ).order_by(Post.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        return posts


