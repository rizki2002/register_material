from odoo import api, fields, models, _


class RegMaterial(models.Model):
	 _name = 'reg.material'
	 
	 material_code = fields.Char("Material Code",required=True,)
	 material_name = fields.Char("Material Name",required=True)
	 tipe_material_id = fields.Many2one(comodel_name="tipe.material", string="Tipe Material", required=True, )
	 material_buy_price =fields.Char(string="Material Buy Price", required=True)
	 related_supplier_id = fields.Many2one(comodel_name="res.partner", string="Supplier", required=True, )
	 


	 @api.onchange('material_buy_price')
	 def _calc_sum(self):
	 	print("material buy price ", self.material_buy_price)
	 	if float(self.material_buy_price) < 100.0:
	 		print("masuk sini")
	 		return False

	 	return True

	 _constraints = [(_calc_sum, 'Price tidak boleh kurang dari 100', ['material_buy_price'])]