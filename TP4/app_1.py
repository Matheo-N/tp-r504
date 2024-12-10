from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'tp4-sql',
    'user': 'root',
    'password': 'foo',
    'database': 'demosql'
}

# Initialize MySQL connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Route pour afficher les données SQL et le formulaire d'inscription
@app.route('/')
def index():
    # Sample query
    query = "SELECT * FROM myTable"
    cursor.execute(query)
    data = cursor.fetchall()
    
    return render_template('index.html', data=data)

# Route pour la validation de l'identifiant
@app.route('/newuser/', methods=['GET', 'POST'])
def new_user():
    message = None  # Initialiser un message vide
    
    # Si la méthode est POST, on valide l'identifiant
    if request.method == 'POST':
        username = request.form.get('username')
        message = validate_username(username)
    
    return render_template('index.html', message=message)

# Fonction de validation de l'identifiant
def validate_username(username):
    # Vérification que l'identifiant a au moins 6 caractères
    if not re.search(r'.{6,}', username):
        return "L'identifiant doit comporter au moins 6 caractères."
    
    # Vérification qu'il y a au moins un chiffre
    if not re.search(r'\d', username):
        return "L'identifiant doit contenir au moins un chiffre."
    
    # Vérification qu'il y a au moins une majuscule
    if not re.search(r'[A-Z]', username):
        return "L'identifiant doit contenir au moins une majuscule."
    
    # Vérification qu'il y a au moins une minuscule
    if not re.search(r'[a-z]', username):
        return "L'identifiant doit contenir au moins une minuscule."
    
    # Vérification qu'il y a au moins un caractère spécial parmi #%{}@
    if not re.search(r'[%#{}@]', username):
        return "L'identifiant doit contenir au moins un caractère parmi #%{}@."
    
    # Si tous les critères sont validés
    return "Identifiant valide!"

if __name__ == '__main__':
    app.run(debug=True)

