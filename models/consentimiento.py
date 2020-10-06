from odoo import api, fields, models, _


class consentimiento(models.Model):
    _name = "mediges.consentimiento"

    visitas_id = fields.One2many('mediges.visitas', 'consentimiento_id')
    fecha_inicio = fields.Date(string="Inicio")
    paciente_cons_id = fields.Many2one('res.partner', string="Paciente", related='visitas_id.paciente' )
    documento = fields.Char(string="N° Documento")
    doc_ver_electronica = fields.Char(string="Version Electronica")
    fecha_termino = fields.Date(string="Termino")


