from flask import Blueprint, render_template, request, redirect, url_for
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts
from flask_user import roles_accepted, roles_required, current_user
from website.areas.newsletter.forms import Newsletters
import flask_login


productBluePrint = Blueprint('product', __name__)




@productBluePrint.route('/')
def index() -> str:
    # flask_login.logout_user() om de fuckar
    #HÄR HIDE NEWSLETTER
    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()
    return render_template('products/index.html',trendingCategories=trendingCategories,
        products=trendingProducts
    )


@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)

