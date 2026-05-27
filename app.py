from flask import Flask, jsonify, request

app = Flask(__name__)


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


def find_event_by_id(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "id" not in data or "title" not in data:
        return jsonify({"error": "Missing required fields: 'id' and 'title'"}), 400

    if not data["title"].strip():
        return jsonify({"error": "Title cannot be empty"}), 400

    new_event = Event(data["id"], data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: 'title'"}), 400

    if not data["title"].strip():
        return jsonify({"error": "Title cannot be empty"}), 400

    event = find_event_by_id(event_id)

    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    event.title = data["title"]
    return jsonify(event.to_dict()), 200


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event_by_id(event_id)

    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    events.remove(event)
    return jsonify({"message": f"Event {event_id} deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)