
from odoo import models,fields,api

class LeaseProperty(models.Model):
        _name = 'lease.property'
        _inherits ={"res.partner" : "partner_id"}

        partner_id = fields.Many2one("res.partner")
        lease_duration = fields.Char()
        lease_rent_monthly = fields.Intager()