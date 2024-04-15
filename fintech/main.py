from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

receitas = []
despesas = []


@app.route('/')
def receita():
    total = sum(float(item['valor']) for item in receitas)
    return render_template('receitas.html', receitas=receitas, total=total)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        valor = request.form['valor']
        descricao = request.form['descricao']

        if valor == '' or descricao == '':
            return 'Esses campos são obrigatórios!!'

        receitas.append({
            'tipo': 'receita',
            'valor': valor,
            'descricao': descricao,
        })

        return redirect(url_for('receita'))

    total = sum(float(item['valor']) for item in receitas)
    return render_template('adicionar.html', total=total)


@app.route('/excluir_receita/<int:index>')
def excluir_receita(index):
    if 0 <= index < len(receitas):
        del receitas[index]
    return redirect(url_for('receita'))


@app.route('/despesas', methods=['GET', 'POST'])
def despesa():
    if request.method == 'POST':
        valor = request.form['valor']
        descricao = request.form['descricao']
        data = request.form['data']

        if valor == '' or descricao == '' or data == '':
            return 'Esses campos são obrigatórios!!'

        despesas.append({
            'tipo': 'despesa',
            'valor': valor,
            'descricao': descricao,
            'data': data
        })

    total = sum(float(item['valor']) for item in despesas)
    return render_template('despesas.html', despesas_data=despesas, total=total)

@app.route('/excluir_despesa/<int:index>')
def excluir_despesa(index):
    if 0 <= index < len(despesas):
        del despesas[index]
    return render_template('despesas.html', despesas_data=despesas,
                           total=sum(float(item['valor']) for item in despesas))


if __name__ == '__main__':
    app.run(debug=True)
