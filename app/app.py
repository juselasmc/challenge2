# J. Sebastian Laverde - Challenge2
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail
import os
import json
import csv

# Creacion del directorio para procesar los ficheros
if not os.path.exists('uploads'):
    os.makedirs('uploads')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@db/challenge_db' #Nos conectamos a la BD.
db = SQLAlchemy(app)

class challenge_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_db = db.Column(db.String(255), nullable=False)
    owner_email = db.Column(db.String(255), nullable=False)
    manager_email = db.Column(db.String(255), nullable=False)
    db_classification = db.Column(db.String(255), nullable=False)
    db_severity = db.Column(db.String(255), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST': 
        csv_file = request.files['csv']
        json_file = request.files['json']

        if csv_file.filename.endswith('.csv') and json_file.filename.endswith('.json'): #Restriccion de tipo de fichero. Aun que no es seguro. 
            csv_file.save(os.path.join('uploads', csv_file.filename))
            json_file.save(os.path.join('uploads', json_file.filename))
            
            with open(os.path.join('uploads', json_file.filename), 'r') as f:
                json_data = json.load(f)

            # Parse CSV file
            with open(os.path.join('uploads', csv_file.filename), 'r') as f:
                csv_data = csv.DictReader(f)
                for row in csv_data:
                    for item in json_data:
                        if row['user_id'] == item.get('User', 'CISO@miprogramita.co'):
                            manager_email = row['user_manager']
                            nombre_db = item.get('DB', 'SinIdentificar')
                            owner_email = item.get('User', 'CISO@miprogramita.co')
                            db_classification = item.get('Classification', 'NonCDE_NonCritical')
                            db_severity = item.get('Severity', 'Medio')

                            #AcaEnviariamos los correos, pero en este caso no, por que no tenngo un Servidor SMTP a la mano. 
                            #Solamente pondremos correos enviados en el OK
                            #send_mail(manager_email, owner_email, nombre_db)

                            new_entry = challenge_table(
                                nombre_db=nombre_db,
                                owner_email=owner_email,
                                manager_email=manager_email,
                                db_classification=db_classification,
                                db_severity=db_severity
                            )
                            db.session.add(new_entry)
                            db.session.commit()

                            break
            return render_template('satis.html')

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
