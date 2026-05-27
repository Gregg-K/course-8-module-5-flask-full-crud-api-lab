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


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Events API"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)

    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "title is required"}), 400

    new_id = max(event.id for event in events) + 1 if events else 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json(silent=True)

    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "title is required"}), 400

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