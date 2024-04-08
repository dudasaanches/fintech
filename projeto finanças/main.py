from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def receitas():
    # Replace with your actual data source (e.g., database, list)
    receitas_data = [
        {'tipo': 'Salário', 'valor': 2500},
        {'tipo': 'Freelancer', 'valor': 500},
        # Add more receitas items here
    ]
    total = sum(item['valor'] for item in receitas_data)
    return render_template('receitas.html', receitas_data=receitas_data, total=total)

if __name__ == '__main__':
    app.run(debug=True)
