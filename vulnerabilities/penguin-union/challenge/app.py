from flask import Flask, render_template, request, jsonify
from sqldb import db, db_init

FLAG='UWA{tH4t5_s0Me_b3Z0s_lVl_vN1oN_bUsTin}'

app = Flask(__name__, static_folder='./static', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/penguinunion.db'
db.init_app(app)

with app.app_context():
    db_init(FLAG)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', None)
    with db.engine.begin() as conn:
        regos = [(r[0], r[1]) for r in conn.exec_driver_sql('SELECT name,reason FROM registrations;').all()]
        if isinstance(query, str):
            try:
                regos = [(r[0], r[1]) for r in conn.exec_driver_sql(f'SELECT name,reason FROM registrations WHERE name LIKE \'%{query}%\' OR reason LIKE \'%{query}%\';').all()]
            except Exception as e:
                return render_template('index.html', error=f'An error occurred: {e}', registrations=regos)
    return render_template('index.html', registrations=regos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=False)