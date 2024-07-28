from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Item

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@bp.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    description = request.form.get('description')
    new_item = Item(name=name, description=description)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    item = Item.query.get_or_404(id)
    item.name = request.form.get('name')
    item.description = request.form.get('description')
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))

