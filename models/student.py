from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    birth_date = fields.Date(string='Birth date', required=True)
    email = fields.Char(string='Email', required=True)
    active = fields.Boolean(string='Active', default=True)
