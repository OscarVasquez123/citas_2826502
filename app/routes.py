from . import app
from .models import Medico, Paciente, Consultorio, Citas
from flask import render_template

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" ,  medicos=medicos )

#crear ruta para ver los pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" ,  pacientes=pacientes )

@app.route("/Consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" ,  consultorios=consultorios )

@app.route("/citas")
def get_all_citas():
    citas = cita.query.all()
    return render_template("citas.html" ,  cita=citas )
    
    