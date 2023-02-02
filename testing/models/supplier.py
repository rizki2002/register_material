from odoo import api, fields, models, _


class Supplier(models.Model):
	 _name = 'supplier.material'
	 
	 name = fields.Char("Nama Supplier",required=True,)
	 keterangan = fields.Char("Keterangan", required=False)