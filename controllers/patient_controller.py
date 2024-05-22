from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from models import Patient, db

@login_required
def list_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@login_required
def create_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        patient = Patient(name=name, age=age, condition=condition)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient.list_patients'))
    return render_template('patient_form.html')

@login_required
def update_patient(id):
    patient = Patient.query.get(id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.condition = request.form['condition']
        db.session.commit()
        return redirect(url_for('patient.list_patients'))
    return render_template('patient_form.html', patient=patient)

@login_required
def delete_patient(id):
    patient = Patient.query.get(id)
    if request.method == 'POST':
        db.session.delete(patient)
        db.session.commit()
        return redirect(url_for('patient.list_patients'))
    return render_template('confirm_delete.html', patient=patient)
