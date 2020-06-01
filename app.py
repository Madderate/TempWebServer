import os
import sys
import click
from flask import Flask, render_template
from flask import escape, url_for
from flask_sqlalchemy import SQLAlchemy


# 判断操作系统
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# app实例
app = Flask(__name__)
# SQL位置
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(
    app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 数据库实例
db = SQLAlchemy(app)

# 两个数据库模型类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    luminous_intensity = db.Column(db.Integer)
    air_quality = db.Column(db.Integer)

# 建库
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

# 自定义命令forge
@app.cli.command()
def forge():
    """Gemerate fake data."""
    db.create_all()

    name = 'madderate'
    environmentList = [
        {'temperature': 24, 'humidity': 50, 'luminous_intensity':500, 'air_quality':25},
        {'temperature': 23, 'humidity': 57, 'luminous_intensity':700, 'air_quality':28},
        {'temperature': 27, 'humidity': 80, 'luminous_intensity':1200, 'air_quality':46},
        {'temperature': 26, 'humidity': 46, 'luminous_intensity':400, 'air_quality':35},
        {'temperature': 24, 'humidity': 23, 'luminous_intensity':625, 'air_quality':56},
        {'temperature': 20, 'humidity': 42, 'luminous_intensity':736, 'air_quality':100},
        {'temperature': 30, 'humidity': 52, 'luminous_intensity':632, 'air_quality':46},
        {'temperature': 24, 'humidity': 50, 'luminous_intensity':746, 'air_quality':35},
        {'temperature': 24, 'humidity': 25, 'luminous_intensity':100, 'air_quality':62},
        {'temperature': 22, 'humidity': 63, 'luminous_intensity':1652, 'air_quality':142}        
    ]

    user = User(name=name)
    db.session.add(user)
    for en in environmentList:
        environment = Environment(
            temperature=en['temperature'],
            humidity=en['humidity'],
            luminous_intensity=en['luminous_intensity'],
            air_quality=en['air_quality'])
        db.session.add(environment)
    db.session.commit()
    click.echo('Done.')

# 处理请求
@app.route('/')
def index():
    environmentQuery = Environment.query.all()
    return render_template('index.html', environmentQuery=environmentQuery)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

