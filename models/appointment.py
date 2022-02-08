from tokenize import group
from attr import field
from odoo import fields, models, api

class Appointment_System(models.Model):
    _name = 'appointment.system'

    name = fields.Char()
    appointment_type = fields.Char()
    custmer = fields.Many2one("res.partner")
    time = fields.Date()
    price = fields.Float()
    phone_number = fields.Integer()
    # time_zone = fields.Timezone()
    address = fields.Char()
    location = fields.Char()
    schedule_appointment = fields.Char()
    appointment_duration = fields.Integer()
     
