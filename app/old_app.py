
@app.route('/clientes', methods=['GET', 'POST'])
@login_required
def clientes():
    if request.method == 'GET':
        return render_template('clientes.html', title="Clientes")
    if request.method == 'POST':
        return "<h1> Salvou! </h1>"

@app.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuarios():
    if request.method == 'GET':
        return render_template('usuarios.html', title="Usuários")

    if request.method == 'POST':

        usuario = Usuarios(
            usu_nome = request.form['usu_nome'],
            usu_email = request.form['usu_email'],
            usu_senha = request.form['usu_senha'],
            usu_departamento = request.form['usu_departamento'],
        )

        db.session.add(usuario)
        db.session.commit()

        flash("Usuário cadastrado com sucesso.", "success")
        return redirect(url_for('usuarios'))
