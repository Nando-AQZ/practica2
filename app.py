from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/")
def index():
    
    return render_template('index.html',curso=session['index'])

@app.route("/cursos")
def cursos():
    if 'cursos' not in session:
        # Inicializar carrito como lista
        session['cursos'] = []
           
    return render_template('curso.html',cursos = session['cursos'])
   
@app.route("/procesa",methods=['POST'])
def procesa():
    nombre = request.form.get('nombre')
    apellido =request.form.get('apellido')
    curso = request.form.get('curso')
    
    if 'cursos' not in session:
        # Inicializar carrito como lista
        session['cursos'] = []
        
    # Agregar el producto al carrito
    session['cursos'].append({'nombre':nombre,'apellido':apellido,'curso':curso })
    session.modified = True
    
    return redirect(url_for("cursos")) 

@app.route("/vaciar")
def vaciar():
    session.pop('cursos',None)
    return redirect(url_for("cursos"))

# campo para usuarios

@app.route("/usuarios")
def usuarios():
    if 'usuarios' not in session:
        # Inicializar carrito como lista
        session['usuarios'] = []
           
    return render_template('usuarios.html',usuarios = session['usuarios'])

@app.route("/procesa_usuario",methods=['POST'])
def procesa_usuario():
    nombre = request.form.get('nombre')
    apellido =request.form.get('apellido')
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')
    
    if 'usuarios' not in session:
        # Inicializar carrito como lista
        session['usuarios'] = []
        
    # Agregar el producto al carrito
    session['usuarios'].append({'nombre':nombre,'apellido':apellido,'correo':correo,'contraseña':contraseña })
    session.modified = True
    
    return redirect(url_for("usuarios")) 

@app.route("/vaciar_usuario")
def vaciar_usuario():
    session.pop('usuarios',None)
    return redirect(url_for("usuarios"))

#espacio para productos
@app.route("/productos")
def productos():
    if 'productos' not in session:
        # Inicializar carrito como lista
        session['productos'] = []
           
    return render_template('productos.html',productos = session['productos'])

@app.route("/procesa_productos",methods=['POST'])
def procesa_productos():
    producto = request.form.get('producto')
    categoria =request.form.get('categoria')
    existencias = request.form.get('existencias')
    precio = request.form.get('precio')
    
    if 'productos' not in session:
        # Inicializar carrito como lista
        session['productos'] = []
        
    # Agregar el producto al carrito
    session['productos'].append({'producto':producto,'categoria':categoria,'existencias':existencias,'precio':precio })
    session.modified = True
    
    return redirect(url_for("productos")) 

@app.route("/vaciar_producto")
def vaciar_producto():
    session.pop('productos',None)
    return redirect(url_for("productos"))

#espacio de libros
@app.route("/libros")
def libros():
    if 'libros' not in session:
        # Inicializar carrito como lista
        session['libros'] = []
           
    return render_template('libros.html',libros = session['libros'])

@app.route("/procesa_libros",methods=['POST'])
def procesa_libros():
    titulo = request.form.get('titulo')
    autor =request.form.get('autor')
    resumen = request.form.get('resumen')
    medio = request.form.get('medio')
    
    if 'libros' not in session:
        # Inicializar carrito como lista
        session['libros'] = []
        
    # Agregar el producto al carrito
    session['libros'].append({'titulo':titulo,'autor':autor,'resumen':resumen,'medio':medio })
    session.modified = True
    
    return redirect(url_for("libros")) 

@app.route("/vaciar_libros")
def vaciar_libros():
    session.pop('libros',None)
    return redirect(url_for("libros"))


if __name__ == "__main__":
    app.run(debug=True)