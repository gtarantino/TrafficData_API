from flask import Flask

from content import content_api

# Create the Server
app = Flask(__name__)

#Register Blueprints
app.register_blueprint(content_api)

@app.route("/")
def main():
   return "Kye & Gio's Traffic Data Server", 200

if __name__ == "__main__":
   app.debug = True
   app.run(threaded=True)
