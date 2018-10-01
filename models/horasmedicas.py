from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class horasmedicas(models.Model):
    _name = "mediges.horasmedicas"
    _order = 'company, fecha_solicitud_hora'

    company =  fields.Many2one('res.company', string="Hora Para", required=True,readonly=True ,default=lambda self: self.env['res.company']._company_default_get('account.invoice'))
    fecha_solicitud_hora = fields.Datetime(String="Hora Reserva", required=True)
    fecha_solicitud_hora_termino = fields.Datetime(String="Hora Reserva")
    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    forma_de_pago = fields.Many2one('mediges.formas_de_pagos', string="Forma de Pagos", required=True)
    historial = fields.Text(string="Historial")
    diagnostico = fields.Text(string="Diagnostico")
    Observacion = fields.Text(string="Observacion")
    antecedentes_paciente = fields.Text(string="Antecedentes Paciente")


    @api.onchange('fecha_solicitud_hora')
    def calcula_hora_termino(self):

        ahora = datetime.now()
        if self.fecha_solicitud_hora != False:
            hora = fields.Datetime.from_string(self.fecha_solicitud_hora)
            self.fecha_solicitud_hora_termino = hora + timedelta(minutes=15)
