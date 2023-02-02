from odoo import api, fields, models, _


class TipeMaterial(models.Model):
	 _name = 'tipe.material'
	 
	 name = fields.Char("Nama Type",required=True,)
	 keterangan = fields.Char("Keterangan", required=False)