from flask import Flask, render_template, jsonify, request, redirect, url_for
import threading
from customerCSV import CustomersJson
from pewee_sql_handler import grab_customers_for_jinja, read_customer, update_customer
from pathlib import Path
from time import sleep
from backend_extended_handler import process_pewee_update
import logging

td = Path(__file__).parent.parent.parent / 'templates'
sd = Path(__file__).parent.parent.parent / 'static'
app = Flask(__name__, template_folder=td.resolve(), static_folder=sd.resolve())
app.config.from_pyfile


def flask_thread(PORT):
    """`threading.Thread(flask)`"""
    try:
        t = threading.Thread(target=start_flask, args=[PORT])
        t.daemon = True
        t.start()
    except Exception as e:
        print(f"Error while starting Flask: {e}")

def start_flask(PORT):
    """`start_flask(PORT) => app.run(port=PORT)`"""
    app.run(port=PORT)


@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page of the application. It is used to display the list of customers and their profile.""" 
    return render_template('index.html', customers=grab_customers_for_jinja())

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

@app.route('/newCustomer')
def new_customer():
    return render_template('new_customer.html')

@app.route('/deleteCustomer')
def delete_customer():
    customerID = request.args.get('customerID')
    customer = read_customer(customerID)
    return render_template('confirmDelete.html', customer=customer)


# ==> view ==> edit ==> process ==> index
@app.route('/profileViewEdit')
def profile_view_edit():
    customerID = request.args.get('customerID')
    customer = read_customer(customerID)
    return render_template('profileViewEdit.html', customer=customer)


# open calendar app, wait to finish, then return to index
@app.route('/scheduleCustomerPost')
def schedule_customer():
    customerID = request.args.get('customerID')
    customer = read_customer(customerID)
    return render_template('profileViewEdit.html', customer=customer)


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/processUpdate', methods=['GET', 'POST'])
def process_customer_update():
    try:
        form_data = request.form
        status = process_pewee_update(form_data)
        if status == True:
            return redirect(url_for('index'))
        else:
            print(str(status))
            return redirect(url_for('index'))
    except Exception as e:
        print(str(e))
        return redirect(url_for('index'))