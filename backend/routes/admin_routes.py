from flask import jsonify, Blueprint, redirect, url_for

#  -----------    menu
admin_menu_route = Blueprint("admin_menu_route", __name__)
@admin_menu_route.route("/admin")
def admin_page():
    return redirect(url_for("home"))



# ------------   add / edit / delete asset
asset_route = Blueprint("asset_route", __name__)
@asset_route.route("/admin/assets")
def asset_page():
    return jsonify({"message": "asset manage"})



# -------------     edit admin
edit_admin_route = Blueprint("edit_admin_route", __name__)
@edit_admin_route.route("/admin/admins")
def edit_admin():
    return jsonify({"message": "edit admin"})



#edit team
edit_route = Blueprint("edit_route", __name__)
@edit_route.route("/teams/<tag>/edit")
def edit_team():
    return 




