from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database function to connect
def get_db_connection():
    conn = sqlite3.connect("agings.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_experiment_stats():
    """Retrieve experiment success rates with specificity counts."""
    conn = get_db_connection()
    cur = conn.cursor()

# <th>Super Pedra</th><!-- <th><img src="icon2.png" width="30"></th> -->
# <th>Safira</th>
# <th>Ouro Mágico</th>
# <th>Ouro Mágico dos Anciões</th>
# <th>Ouro Mágico Superior</th>
# <th>Minério Mágico</th>

    cur.execute("""
        SELECT name,
            SUM(CASE WHEN   catalyst = 'Nenhum' THEN success ELSE 0 END) AS success_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' THEN 1 ELSE NULL END) AS attempts_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' AND specificity = '+1' THEN 1 ELSE NULL END) AS plus1_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' AND specificity = '+2' THEN 1 ELSE NULL END) AS plus2_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' AND specificity = '-1' THEN 1 ELSE NULL END) AS minus1_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' AND specificity = '-2' THEN 1 ELSE NULL END) AS minus2_c1,
            COUNT(CASE WHEN catalyst = 'Nenhum' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c1,
        
            SUM(CASE WHEN   catalyst = 'Pedra' THEN success ELSE 0 END) AS success_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' THEN 1 ELSE NULL END) AS attempts_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' AND specificity = '+1' THEN 1 ELSE NULL END) AS plus1_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' AND specificity = '+2' THEN 1 ELSE NULL END) AS plus2_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' AND specificity = '-1' THEN 1 ELSE NULL END) AS minus1_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' AND specificity = '-2' THEN 1 ELSE NULL END) AS minus2_c2,
            COUNT(CASE WHEN catalyst = 'Pedra' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c2,
        
            SUM(CASE WHEN catalyst =   'Super Pedra' THEN success ELSE 0 END) AS success_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' THEN 1 ELSE NULL END) AS attempts_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' AND specificity = '+1' THEN 1 ELSE NULL END) AS plus1_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' AND specificity = '+2' THEN 1 ELSE NULL END) AS plus2_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' AND specificity = '-1' THEN 1 ELSE NULL END) AS minus1_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' AND specificity = '-2' THEN 1 ELSE NULL END) AS minus2_c3,
            COUNT(CASE WHEN catalyst = 'Super Pedra' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c3,

            SUM(CASE WHEN   catalyst = 'Safira' THEN success ELSE 0 END) AS success_c4,
            COUNT(CASE WHEN catalyst = 'Safira' THEN 1 ELSE NULL END) AS attempts_c4,
            COUNT(CASE WHEN catalyst = 'Safira' AND specificity = '+1' THEN 1 ELSE NULL END) AS plus1_c4,
            COUNT(CASE WHEN catalyst = 'Safira' AND specificity = '+2' THEN 1 ELSE NULL END) AS plus2_c4,
            COUNT(CASE WHEN catalyst = 'Safira' AND specificity = '-1' THEN 1 ELSE NULL END) AS minus1_c4,
            COUNT(CASE WHEN catalyst = 'Safira' AND specificity = '-2' THEN 1 ELSE NULL END) AS minus2_c4,
            COUNT(CASE WHEN catalyst = 'Safira' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c4,

            SUM(CASE WHEN   catalyst = 'Ouro' THEN success ELSE 0 END) AS                        success_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' THEN 1 ELSE NULL END) AS                          attempts_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' AND specificity = '+1' THEN 1 ELSE NULL END) AS      plus1_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' AND specificity = '+2' THEN 1 ELSE NULL END) AS      plus2_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' AND specificity = '-1' THEN 1 ELSE NULL END) AS     minus1_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' AND specificity = '-2' THEN 1 ELSE NULL END) AS     minus2_c5,
            COUNT(CASE WHEN catalyst = 'Ouro' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c5,

            SUM(CASE WHEN   catalyst = 'Ouro_anc' THEN success ELSE 0 END) AS                        success_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' THEN 1 ELSE NULL END) AS                          attempts_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' AND specificity = '+1' THEN 1 ELSE NULL END) AS      plus1_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' AND specificity = '+2' THEN 1 ELSE NULL END) AS      plus2_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' AND specificity = '-1' THEN 1 ELSE NULL END) AS     minus1_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' AND specificity = '-2' THEN 1 ELSE NULL END) AS     minus2_c6,
            COUNT(CASE WHEN catalyst = 'Ouro_anc' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c6,

            SUM(CASE WHEN   catalyst = 'Ouro_sup' THEN success ELSE 0 END) AS                        success_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' THEN 1 ELSE NULL END) AS                          attempts_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' AND specificity = '+1' THEN 1 ELSE NULL END) AS      plus1_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' AND specificity = '+2' THEN 1 ELSE NULL END) AS      plus2_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' AND specificity = '-1' THEN 1 ELSE NULL END) AS     minus1_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' AND specificity = '-2' THEN 1 ELSE NULL END) AS     minus2_c7,
            COUNT(CASE WHEN catalyst = 'Ouro_sup' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c7,

            SUM(CASE WHEN   catalyst = 'Minerio' THEN success ELSE 0 END) AS                        success_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' THEN 1 ELSE NULL END) AS                          attempts_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' AND specificity = '+1' THEN 1 ELSE NULL END) AS      plus1_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' AND specificity = '+2' THEN 1 ELSE NULL END) AS      plus2_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' AND specificity = '-1' THEN 1 ELSE NULL END) AS     minus1_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' AND specificity = '-2' THEN 1 ELSE NULL END) AS     minus2_c8,
            COUNT(CASE WHEN catalyst = 'Minerio' AND specificity = 'Broken' THEN 1 ELSE NULL END) AS broken_c8

        FROM agings
        GROUP BY name
        ORDER BY CAST(name AS INTEGER);
""")

    results = cur.fetchall()
    cur.close()
    conn.close()

    # for r in results:
    #     print(f"")

    return results  # List of tuples (experiment_name, S1, A1, N+1, N+2, N-1, N-2, N_broken, S2, A2, ...)

# Home Page (Shows Statistics)
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get success rate statistics
    stats = get_experiment_stats()

    return render_template("index.html", stats=stats)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contribua')
def contribua():
    return render_template('contribua.html')

# Add Experiment Page
@app.route("/add_age", methods=["GET", "POST"])
def add_age():
    if request.method == "POST":
        nivel = request.form["nivel"]
        catalisador = request.form["catalyst"]
        specificity = request.form["specificity"]
        success = 1 if specificity in ("+1", "+2") else 0
        checkbox_multiple = request.form.get("checkbox")

        conn = get_db_connection()
        cursor = conn.cursor()
        
        if checkbox_multiple:
            number_of_tries = request.form.get("n_tents")
            for i in range(int(number_of_tries)):
                cursor.execute("INSERT INTO agings (name, catalyst, success, specificity) VALUES (?, ?, ?, ?)", (nivel, catalisador, success, specificity))
        else:
            cursor.execute("INSERT INTO agings (name, catalyst, success, specificity) VALUES (?, ?, ?, ?)", (nivel, catalisador, success, specificity))

            
        conn.commit()
        conn.close()
        
        return redirect(url_for("index"))
    
    return render_template("add_age.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)