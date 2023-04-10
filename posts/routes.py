from flask import Blueprint, request, jsonify
from .models import Post
from app import app, db
from.controller import PostController
import datetime

posts_bp = Blueprint('create_post', __name__)

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    text = data.get('text')
    lat = data.get('lat')
    lon = data.get('lon')
    if not text or not lat or not lon:
        return jsonify({'message': 'Missing required parameters'}), 400
    location = f'POINT({lon} {lat})'
    post = Post(text=text, location=location)
    post.save()
    return jsonify({'message': 'Post created successfully'}), 201

@posts_bp.route('/recent_posts', methods=['GET'])
def get_recent_posts():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    page = request.args.get('page', default=1, type=int)
    if not lat or not lon:
        return jsonify({'message': 'Missing required parameters'}), 400
    posts = PostController.get_recent_posts(lat=lat, lon=lon, page=page)
    recent_posts = []
    for post in posts.items:
        created_at = post.created_at
        pretty_time = get_pretty_time(created_at)
        recent_posts.append({
            'id': post.id,
            'text': post.text,
            'location': post.location,
            'created_at': pretty_time
        })
    return jsonify({
        'posts': recent_posts,
        'has_next': posts.has_next,
        'has_prev': posts.has_prev,
        'next_page': posts.next_num,
        'prev_page': posts.prev_num
    }), 200


def get_pretty_time(created_at):
    now = datetime.datetime.utcnow()
    time_diff = now - created_at
    if time_diff < datetime.timedelta(minutes=1):
        return 'just now'
    elif time_diff < datetime.timedelta(hours=1):
        minutes = int(time_diff.seconds / 60)
        return f'{minutes} min ago'
    elif time_diff < datetime.timedelta(days=1):
        hours = int(time_diff.seconds / 3600)
        return f'{hours} hours ago'
    elif time_diff < datetime.timedelta(days=7):
        days = int(time_diff.days)
        if days == 1:
            return 'yesterday'
        else:
            return f'{days} days ago'
    elif time_diff < datetime.timedelta(days=30):
        weeks = int(time_diff.days / 7)
        if weeks == 1:
            return '1 week ago'
        else:
            return f'{weeks} weeks ago'
    else:
        months = int(time_diff.days / 30)
        if months == 1:
            return '1 month ago'
        else:
            return f'{months} months ago'