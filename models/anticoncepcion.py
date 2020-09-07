from odoo import api, fields, models, _


class anticoncepcion(models.Model):
   _name = "mediges.anticoncepcion"

   tipo_anticoncepcion_id = fields.Many2one('mediges.tipo_anticoncepcion', string="Tipo Anticoncepcion", required=True)
   cuando = fields.Integer(string="Año")
   cual = fields.Char(string="Cual")
   visitas_id = fields.Many2one('mediges.visitas', string="Visitas",)