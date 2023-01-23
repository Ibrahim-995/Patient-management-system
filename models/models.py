
from odoo import models, fields


class SchoolProfile(models.Model):
    _name = "school.profile"

    image = fields.Image(string='Profile Picture')
    _id = fields.Char(string="ID")
    name = fields.Char(string="Patient Name")
    _address = fields.Char(string="Address")
    blood = fields.Char(string="Blood Group")
    _disease = fields.Char(string="Disease Name")
    _age = fields.Char(string="Age")
    phone = fields.Char(string="Phone")