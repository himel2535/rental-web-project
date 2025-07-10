from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data
properties = [
    {'id': 1, 'title': '2 Bed Flat in Dhanmondi', 'rent': 15000, 'available': True},
    {'id': 2, 'title': 'Studio Apartment in Banani', 'rent': 20000, 'available': True},
    {'id': 3, 'title': '3 Bed House in Uttara', 'rent': 25000, 'available': True},
]

bookings = []

@app.route('/')
def index():
    return render_template('index.html', properties=properties)

@app.route('/book/<int:prop_id>', methods=['GET', 'POST'])
def book(prop_id):
    selected_property = next((p for p in properties if p['id'] == prop_id and p['available']), None)
    if not selected_property:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        bookings.append({'user': name, 'property': selected_property})
        selected_property['available'] = False
        return redirect(url_for('bookings_view'))

    return render_template('booking.html', property=selected_property)

@app.route('/bookings')
def bookings_view():
    return render_template('bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
