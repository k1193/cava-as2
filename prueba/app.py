from flask import Flask, render_template, request, session, redirect, url_for, session
import pymongo


# Conexión
myClient = pymongo.MongoClient("mongodb://localhost:27017")
myDb = myClient["talesapp"] #database
myCollection = myDb["tales"] #collection
myCavanas = myDb["cavanas"] #collection
myPerfil = myDb["perfil"] #collection
myReservas = myDb["reservas"] #["perfil"] #collection

app = Flask(__name__)
app.secret_key = "ascd123"



@app.route('/login', methods=["POST", "GET"])  # decorador)
def login():
  if request.method == "POST":
    users = myCollection
    email = request.form['email']
    existing_user = users.find_one({'EMail' : email})
    rol_name = users.find_one({'EMail' : email, 'rol_name' : "Anfitrion"})
    
    if existing_user:
      if request.form['password'] == existing_user['password']:
        if rol_name:
          session['user'] = email
          session['rol'] = "true"
        return redirect(url_for('anfitrion'))
        
    return 'Invalid username/password combination'
    
  return render_template('login.html')


@app.route('/reserva', methods=["POST", "GET"])
def reserva():
    if request.method == "POST":
      reserva = myReservas
      
      email = request.form['email']
      telefono = request.form['telefono']
      llegada = request.form['llegada']
      permanencia = request.form['permanencia']
      cantidad = request.form['cantidad']
      reserva.insert({'email' : email, 'telefono' : telefono, 'llegada' : llegada,
                      'permanencia' : permanencia, 'cantidad' : cantidad})
      return redirect(url_for('index'))
  
      
      
    return render_template('reserva.html')



@app.route('/anfitrion')
def anfitrion():
  if 'user' in session and session['rol'] == 'true':
    return  render_template("anfitrion.html")
  else:
    return render_template('index.html')



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
  
  
@app.route('/perfil')
def perfil():
  
  return render_template('perfil.html')
  


@app.route('/register', methods=["POST", "GET"])  # decorador)
def register():
    if request.method == "POST":
      users =myCollection
      existing_user = users.find_one({'name' : request.form['username']})
      
      if existing_user is None:
        name = request.form['username']
        EMail = request.form['EMail']
        Country = request.form['Country']
        city = request.form['city']
        password = request.form['password']
        rol_name = request.form['rol_name']
        users.insert({'name' : name, 'EMail' : EMail, 'Country' : Country, 'city' : city, 'password' : password,'rol_name' : rol_name})
        return redirect(url_for('index'))
        
      return 'That username already exists!'

    return render_template('register.html')

@app.route('/')
def index():
  return render_template('index.html')



@app.route('/addapartment', methods=["POST", "GET"])
def addapartment():
  if request.method == "POST":
      Cavanas = myCavanas
      
      Country = request.form['Country']
      city = request.form['city']
      Direction = request.form['Direction']
      Location = request.form['Location']
      rooms = request.form['rooms']
      ImagesApartment = request.form['ImagesApartment']
      night = request.form['night']
      ReviewApartment = request.form['ReviewApartment']
      
      insercavanas = {'Country': Country, 'city' : city, 'Direction' : Direction, 'Location' : Location, 'rooms' :rooms, 'ImagesApartment' : ImagesApartment, 'night' : night, 'ReviewApartment' : ReviewApartment}
      result = Cavanas.insert_one(insercavanas)
      return redirect(url_for('index'))
      
  return render_template('addApartment.html')

@app.route('/index')
def home():
  return render_template('index.html')


def deleteData():
  
  query ={"EMail": "victorg@gmail.com"}
  myCollection.delete_one(query)
  
deleteData()



def update():
  
  query ={"name": "Kasandra Pimienta"}
  newvalor = {"$set":{"name":"juaquin"}}
  myCollection.update_one(query,newvalor)
  
update()



if __name__ == '__main__':
     app.run(debug=True)