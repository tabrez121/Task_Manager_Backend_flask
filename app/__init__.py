from flask import Flask, send_from_directory, render_template_string
from .config import Config
from .extensions import db, migrate, jwt
from .routes import register_routes
import os

SWAGGER_HTML = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Task Manager API Docs</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@4/swagger-ui.css" />
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
    <script>
      const ui = SwaggerUIBundle({
        url: "/static/openapi.json",
        dom_id: "#swagger-ui",
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout"
      });
    </script>
  </body>
</html>
"""

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config.from_object(config_class)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # register routes
    register_routes(app)

    # docs route
    @app.get("/docs")
    def swagger_ui():
        return render_template_string(SWAGGER_HTML)

    # create tables for local dev
    with app.app_context():
        db.create_all()

    return app
