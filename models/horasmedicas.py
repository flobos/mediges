from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class partidas(models.Model):
    _name = "mediges.horasmedicas"
    _order = 'company, fecha_solicitud_hora'

    company =  fields.Many2one('res.company', string="Hora Para", required=True)
    fecha_solicitud_hora = fields.Datetime(String="Hora Reserva", required=True)
    fecha_solicitud_hora_termino = fields.Datetime(String="Hora Reserva")
    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    antecedentes_paciente = fields.Text(string="Antecedentes Paciente")


    @api.onchange('fecha_solicitud_hora')
    def calcula_hora_termino(self):

        ahora = datetime.now()
        if self.fecha_solicitud_hora != False:
            hora = fields.Datetime.from_string(self.fecha_solicitud_hora)
            self.fecha_solicitud_hora_termino = hora + timedelta(minutes=15)
