from flask import Blueprint, jsonify

add_asset_route = Blueprint("add_asset_route", __name__)

# adding a character
@add_asset_route.route("/assets/add")
def add_asset():
    return ({"message": "add"}) 

#edit character
edit_asset_route = Blueprint("edit_asset_route", __name__)
@edit_asset_route.route("/assets/<id>/edit")
def edit_asset():
    return ({"message": "edit"})

#delete character
delete_asset_route = Blueprint("delete_asset_route", __name__)
@edit_asset_route.route("/assets/<id>/delete")
def delete_asset():
    return ({"message": "del"})