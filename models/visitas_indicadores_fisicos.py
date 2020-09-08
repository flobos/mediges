from odoo import api, fields, models, _

class visitas_indicadores_fisicos(models.Model):
    _name = "mediges.visitas_indicadores_fisicos"

    indicadores_fisicos_id = fields.Many2one('mediges.indicadores_fisicos', string="Indicador", required=True)
    estado = fields.Selection([
        ('NORMAL', "Normal"),
        ('ANORMAL', "Anormal"),
    ], default='NORMAL', string="Estado", track_visibility='onchange', required=True)
    glosa = fields.Char(string="Comentario")
    visitas_id = fields.Many2one('mediges.visitas', string="Visitas", )
