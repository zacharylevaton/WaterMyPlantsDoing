from flask import render_template, url_for, redirect, request, flash
from waterMyPlantsDoing import app
import pymysql

# AWS Database connection setup.
username = 'zachlevaton'
password = 'zalpassword'
hostname = 'istherewaterdb.cdelqzkyx7bn.us-east-2.rds.amazonaws.com'
db = pymysql.connect(host=hostname, user=username, password=password)
cursor = db.cursor()
connect_sql = '''use istherewaterdb'''
cursor.execute(connect_sql)


@app.route('/')
def home():
    # Grabbing last row for Bonsai from database.
    cursor.execute('''select moisturelevel from moisture where sensorid=1 order by id desc limit 1''')
    bonsai_data = cursor.fetchall()
    bonsai = bonsai_data[0][0]
    # Grabbing last row for Big Boi from database.
    cursor.execute('''select moisturelevel from moisture where sensorid=2 order by id desc limit 1''')
    bigboi_data = cursor.fetchall()
    bigboi = bigboi_data[0][0]

    return render_template('main.html', bonsai=bonsai, bigboi=bigboi)
