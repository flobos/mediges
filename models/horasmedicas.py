from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class horasmedicas(models.Model):
    _name = "mediges.horasmedicas"
    _inherit = ['mail.thread']
    _order = 'company, fecha_solicitud_hora'

    @api.model
    def _parametro_company(self):
        company_ahora = self.env['res.company']._company_default_get('account.invoice')
        return company_ahora

    name = fields.Char('Referencia', readonly=True, required=True, index=True, copy=False,
                       default=lambda self: _('New'))
    company =  fields.Many2one('res.company', string="Doctor o Lab.", required=True,readonly=True ,
                               default=lambda self: self.env['res.company']._company_default_get('account.invoice'))
    fecha_solicitud_hora = fields.Datetime(String="Hora Reserva", required=True)
    fecha_solicitud_hora_termino = fields.Datetime(string="Hora Termino Reserva" , readonly=True, compute='_calcula_hora_termino')
    tipo_prestacion = fields.Many2one('product.product', string="Prestación", required=True)
    valor_prestacion =  fields.Float(string="Valor Prestacion",  readonly=True ,store=True, compute='_calcular_valor_prestacion' )
    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    forma_de_pago = fields.Many2one('mediges.formas_de_pagos', string="Forma de Pagos", required=True)
    historial = fields.Text(string="Antecedentes Medicos" , related="paciente.antecedentes_medicos" )
    anamnesis = fields.Text(string="Anamnesis")
    diagnostico = fields.Text(string="Diagnostico")
    numero_boleta = fields.Integer(string="N° Boleta")
    numero_bono = fields.Integer(string="N° Bono")
    antecedentes_paciente = fields.Text(string="Antecedentes Paciente")
    id_ventas = fields.Many2many('sale.order', 'horas_medicas_ventas', 'ventas_id', 'horas_id',
                                 string="Pago Prestación", copy=False)
    prescricion_id = fields.One2many('mediges.prescricion', 'hora_medica_id', string='Indicaciones')
    Observacion = fields.Text(string="Otras")

    state = fields.Selection([
        ('draft', "Borrador"),
        ('confirmed', "Confirmada"),
        ('pagada', "Pagada"),
        ], default='draft', string="Estado", track_visibility='onchange')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('mediges.horasmedicas') or _('New')
            result = super(horasmedicas, self).create(vals)
        return result

    @api.multi
    @api.depends('fecha_solicitud_hora')
    def _calcula_hora_termino(self):
        for record in self:
            if record.fecha_solicitud_hora != False:
                hora = fields.Datetime.from_string(record.fecha_solicitud_hora)
                record.fecha_solicitud_hora_termino = hora + timedelta(minutes=15)

    @api.multi
    @api.depends('forma_de_pago')
    def _calcular_valor_prestacion(self):
        valor = 0
        for record in self:
            valor = record.forma_de_pago.valor
            record.valor_prestacion = valor

    @api.multi
    def btn_confirma_hora(self):
        self.write({'state': "confirmed"})

    @api.multi
    def btn_paga_hora(self):
        self.write({'state': "pagada"})


class horas_medicas_ventas(models.Model):
   _inherit = 'sale.order'
   hotas_medicas_vetas_id = fields.Many2many('mediges.horasmedicas', 'horas_medicas_ventas', 'horas_id', 'ventas_id', string="Pagos", copy=False)




