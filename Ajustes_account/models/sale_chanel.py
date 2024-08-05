from odoo import models, fields, api

class SaleChannel(models.Model):
    _name = 'sale.channel'
    _description = 'Sale Channel'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
