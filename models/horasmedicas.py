from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class horasmedicas(models.Model):
    _name = "mediges.horasmedicas"
    _inherit = ['mail.thread']
    _order = 'company, fecha_solicitud_hora'

    company =  fields.Many2one('res.company', string="Doctor o Lab.", required=True,readonly=True ,default=lambda self: self.env['res.company']._company_default_get('account.invoice'))
    fecha_solicitud_hora = fields.Datetime(String="Hora Reserva", required=True)
    fecha_solicitud_hora_termino = fields.Datetime(string="Hora Termino Reserva" , readonly=True)
    tipo_prestacion = fields.Many2one('product.product', string="Prestación", required=True)
    valor_prestacion =  fields.Float(string="Valor Prestacion",  readonly=True ,store=True )
    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    forma_de_pago = fields.Many2one('mediges.formas_de_pagos', string="Forma de Pagos", required=True)
    historial = fields.Text(string="Historial")
    diagnostico = fields.Text(string="Diagnostico")
    Observacion = fields.Text(string="Observacion")
    antecedentes_paciente = fields.Text(string="Antecedentes Paciente")
    id_ventas = fields.Many2many('sale.order', 'horas_medicas_ventas', 'ventas_id', 'horas_id',
                                 string="Pago Prestación", copy=False)
    state = fields.Selection([
        ('draft', "Borrador"),
        ('confirmed', "Confirmada"),
        ('pagada', "Pagada"),
        ('final', "Finalizada"),
        ], default='draft', string="Estado", track_visibility='onchange')

    @api.onchange('fecha_solicitud_hora')
    def calcula_hora_termino(self):

        if self.fecha_solicitud_hora != False:
            hora = fields.Datetime.from_string(self.fecha_solicitud_hora)
            self.fecha_solicitud_hora_termino = hora + timedelta(minutes=15)

    @api.onchange('tipo_prestacion')
    def calcula_valor_prestacion(self):

            valor = 0
            valor = self.tipo_prestacion.lst_price
            self.valor_prestacion = valor

    @api.multi
    def btn_confirma_hora(self):
        self.write({'state': "confirmed"})

    @api.multi
    def btn_paga_hora(self):
        self.write({'state': "pagada"})

    @api.multi
    def btn_finaliza_hora(self):
        self.write({'state': "final"})




class horas_medicas_ventas(models.Model):
   _inherit = 'sale.order'
   hotas_medicas_vetas_id = fields.Many2many('mediges.horasmedicas', 'horas_medicas_ventas', 'horas_id', 'ventas_id', string="Pagos", copy=False)




