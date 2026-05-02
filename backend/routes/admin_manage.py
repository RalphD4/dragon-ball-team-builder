from flask import Blueprint, jsonify

#add admin
add_admin_route = Blueprint("add_admin_route", __name__)
@add_admin_route.route("/admins/add")
def add_admin():
    return ({"message": "add admin"}) 


#promote admin
promote_admin_route = Blueprint("promote_admin_route", __name__)
@promote_admin_route.route("/admins/promote")
def promote_admin():
    return ({"message": "promote admin"})


#deleting admin
delete_admin_route = Blueprint("delete_admin_route", __name__)
@delete_admin_route.route("/admins/delete")
def delete_asset():
    return ({"message": "del admin"})