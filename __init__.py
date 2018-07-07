from flask import Flask
import os
import scFinder

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/kcsctracker")
    def main():
        northStops = scFinder.getstopinfo("North")
        southStops = scFinder.getstopinfo("South")
        text = "North bound<br>"
        for ns in northStops:
            text = text + ns.name + ": " + ', '.join(ns.times) + '<br/>'
        text = text + '<br>South bound<br>'
        for ss in southStops:
            text = text + ss.name + ": " + ', '.join(ss.times) + '<br>'
        return text

    if __name__ == '__main__':  # Script executed directly?
        app.run()  # Launch built-in web server and run this Flask webapp

    return app

