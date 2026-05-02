from flask import Flask, jsonify
from flask_cors import CORS
from backend.routes.api.public_routes import team_api
from backend.routes.pages.team_pages import team_pages

from routes.team_edit import edit_team_route
from routes.auth_route import login_route
from routes.admin_routes import admin_menu_route, asset_route, edit_admin_route
from routes.assets_route import add_asset_route, edit_asset_route, delete_asset_route
from routes.admin_manage import add_admin_route, promote_admin_route, delete_admin_route


app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")
CORS(app)


#Teams, Team, Character
app.register_blueprint(team_api)
app.register_blueprint(team_pages)


#edit team
app.register_blueprint(edit_team_route)

#admin login
app.register_blueprint(login_route)

#admin control
app.register_blueprint(admin_menu_route)
app.register_blueprint(asset_route)
app.register_blueprint(edit_admin_route)

#asset management 
app.register_blueprint(add_asset_route)
app.register_blueprint(edit_asset_route)
app.register_blueprint(delete_asset_route)

#admin management
app.register_blueprint(add_admin_route)
app.register_blueprint(promote_admin_route)
app.register_blueprint(delete_admin_route)



#home
@app.route("/")
def home():
    return jsonify({"message": "Backend is working!"})


if __name__ == "__main__":
    app.run(debug=True)






