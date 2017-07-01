from wtforms.form import Form
from wtforms import StringField, FieldList, FormField, SubmitField

class ClientForm(Form):
    empresa = StringField('empresa')
    db = StringField('db')
    usuario_lead = StringField('usuario_lead')
    eliminar = SubmitField(label="Eliminar")
    actualizar = SubmitField(label="Actualizar")


class ClientList(Form):
    client_list = FieldList(FormField(ClientForm))

