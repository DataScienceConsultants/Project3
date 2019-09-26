from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_gf






app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/FindmeGFapp"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    rest_dict = mongo.db.rest_dict.find_one()
    return render_template("Allergy.html", rest_dict=rest_dict)


@app.route("/scrape")
def scraper_M():
    rest_dict = mongo.db.rest_dict
    rest_dict_data = scrape_gf.scraper()
    rest_dict.update_one({}, rest_dict_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
