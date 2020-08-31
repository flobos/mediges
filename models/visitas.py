from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class visitas(models.Model):
    _name = "mediges.visitas"

    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    consentimiento = fields.Selection([('true','Si'),('false','No')]
                                      ,'Se realiza proceso de Consentimiento informado, anexo 1',required=True)
    consentimiento_desde = fields.Datetime(String="Hora Inicio", required=True)
    consentimiento_hasta = fields.Datetime(String="Hora Inicio", required=True)
    criterios_exclusion = fields.Selection([('true', 'Si'), ('false', 'No')]
                                            ,'Se revisa Criterios de inclusión/exclusión para screening, anexo 2', required=True)
    demografia_id = fields.Many2one('mediges.demografia', string="Demografia", required=True)
    estatura = fields.Integer(string="Estatura", required=True)
    peso = fields.Integer(string="Peso", required=True)
    imc = fields.Integer(string="IMC", readonly=True)
    signos_vitales_id = fields.One2many('mediges.signos_vitales', 'visitas_id', string='Signos Vitales')





