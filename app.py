from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
 
    # Task 3 - Use the data to create a new Event object
    new_event = Event(data["id"], data["title"])
    events.append(new_event)  # Add it to our in-memory list
 
    # Task 4 - Return the new event with status 201 (Created)
    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Task 2 - Get the JSON data sent by the client
    data = request.get_json()
 
    # Task 3 - Loop through events to find the matching one
    for event in events:
        if event.id == event_id:
            event.title = data["title"]  # Update the title
 
            # Task 4 - Return the updated event with status 200 (OK)
            return jsonify(event.to_dict()), 200
 
    # Task 4 - If no event was found, return a 404 error
    return jsonify({"error": "Event not found"}), 404


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

if __name__ == "__main__":
    app.run(debug=True)
