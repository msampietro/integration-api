from wtforms.form import Form
from wtforms import StringField, FieldList, FormField, SubmitField, IntegerField


class ClientForm(Form):
    codigo = IntegerField('id')
    empresa = StringField('empresa')
    db = StringField('db')
    usuario_lead = StringField('usuario_lead')
    eliminar = SubmitField(label="Eliminar")
    actualizar = SubmitField(label="Actualizar")


class ClientList(Form):
    client_list = FieldList(FormField(ClientForm))

class LoginForm(Form):
    username = StringField('username')
    password = StringField('password')



