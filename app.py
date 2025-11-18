from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pilot_hours', methods=['POST'])
def create_pilot_hours():
    data = request.get_json()
    pilot_id = data.get('pilot_id')
    last_12_months_hours = data.get('last_12_months_hours')

    # Add data validation here

    # Store the data in the database (replace with your database logic)
    print(f"Storing data for pilot_id: {pilot_id}, hours: {last_12_months_hours}")

    return jsonify({'message': 'Pilot hours created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)