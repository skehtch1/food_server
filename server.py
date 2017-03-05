from flask import Flask
import mongo_liason

app = Flask(__name__)
liason = mongo_liason


@app.route("/")
def hello():
    return "You can view food at our /api/v1/<food_id> endpoint! Give it a try with 01001."


@app.route("/api/v1/<food_id>")
def get_food_by_id(food_id):
    document = liason.get_document_by_id(food_id)
    return document

# what is this doing ?
if __name__ == "__main__":
    app.run()
