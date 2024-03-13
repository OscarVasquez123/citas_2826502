from . import app, db
from .models import Medico, Paciente, Consultorio
from flask import render_template, request, flash , redirect

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

    

@app.route("/paciente/<int:id>")
def get_paciente_by_id(id):

    paciente = Paciente.query.get(id)
    #y meterlo a una vista
    return render_template("paciente.html" , 
                           pa = paciente)  
    
    
@app.route("/pacientes/create", methods = [ 'GET' , 'POST'] )
def create_paciente():
    
    if( request.method == 'GET'  ):
    
        tipo_sangre = [
            "O+",
            "A+",
            "AB+",
            "O-",
            "A-",
        ]
        return render_template("paciente_form.html", 
                            tipo_sangre = tipo_sangre )
        
        
    
    
    
    elif(request.method == 'POST'):
    
     new_paciente = Paciente (nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["nu"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["sa"]
                            )
    
    ##añadirlo a la sesion sqlalchemy
    db.session.add(new_paciente)
    db.session.commit()
    return "paciente registrado"



##CREAR MEdcio

@app.route("/medicos/create", methods =['GET','POST'])
def create_medico():
    ##mostrar el formulario
    
    if(request.metod == 'GET' ):
        
    ##ingreso de usuario
        especialidades = [
        "cardiologia",
        "odontologia",
        "urologia"
        ]
    
        return render_template("medico_form.html",
                           especialidades = especialidades)
    
    elif(request.method == 'POST'):
    
        new_medico = Medico(nombre = request.form["nombre"],
                        apellidos = request.form["apellidos"],
                        tipo_identificacion = request.form["ti"],
                        numero_identificacion = request.form["ni"],
                        registro_medico = request.form["rm"],
                        especialidad = request.form["es"]
                        )
    db.session.add(new_medico)
    db.session.commit()
    flash("Medico registradp corresctamente")
    return redirect("/medicos")

@app.route("/medicos/update/<int:id>", methods=["POST", "GET"])
def update_medico(id):
    especialidades = [
            "cardiologia",
            "odontologia",
            "urologia"
        ]
    medico_update= Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                           medico_update = medico_update,
                           especialidades = especialidades)
    elif(request.method == "POST"):
    #actualizar al medico, con los datos del form
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return "medico actualizado"
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect ("/medicos")


















#crear ruta traer el consultorio
@app.route("/Consultorios/<int:id>")
def get_Consultorio_by_id(id):
    Consultorio = Consultorio.query.get(id)
    return render_template("Consultorios.html", con = Consultorio)

@app.route("/Consultorios/create", methods = [ 'GET' , 'POST'] )
def create_Consultorio():
    
    if( request.method == 'GET'  ):
    
        numero = [
            "402",
            "123",
            "102"
        ]
        return render_template("Consultorio_form.html",
                            numero = numero )
        
    
    elif(request.method== 'POST'):

        new_consultorio = Consultorio(numero = request.form["numero"])
        
    db.session.add(new_consultorio)
    db.session.commit()
    return "consultorio registrado"
    