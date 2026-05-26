from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="site123",  
    database="testdatabase"
)

cursor = db.cursor(dictionary=True)

@app.route("/api/events", methods=["POST"])
def add_event():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    date = data.get("date")

    if not title or not date:
        return jsonify({"error": "Missing title or date"}), 400

    query = "INSERT INTO reminders (title, description, date) VALUES (%s, %s, %s)"
    values = (title, description, date)

    cursor.execute(query, values)
    db.commit()
    return jsonify({"status": "success", "message": "Event added!"}), 201
@app.route("/api/events", methods=["GET"])
def get_events():
    cursor.execute("SELECT * FROM reminders")
    reminders = cursor.fetchall()
    return jsonify(reminders)
@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    title = data.get("title")
    description = data.get("description")
    date = data.get("date")

    if not title or not date:
        return jsonify({"error"}),

    query = "UPDATE reminders SET title = %s, description = %s, date = %s WHERE id = %s"
    values = (title, description, date, event_id)

    cursor.execute(query, values)
    db.commit()
#finish this
    if cursor.rowcount == 0:
        return jsonify({"error"}),

    return jsonify({"status": "success", "message": "Event updated!"})

@app.route("/api/events/<int:event_id>", methods=["DELETE"])#redo
def delete_event(event_id):
    cursor.execute("DELETE FROM reminders WHERE id = %s", (event_id,))
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Event not found!"}), 404

    return jsonify({"status": "success", "message": "Event deleted!"})

if __name__ == "__main__":
    app.run(debug=True)