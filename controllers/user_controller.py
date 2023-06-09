from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.account_repository as account_repository

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/user")
def user(id):
    user = user_repository.select_all()
    account = account_repository.select_all()
    return render_template("user/index.html", user = user, account = account)
