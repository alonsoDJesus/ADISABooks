# -*- coding: utf-8 -*-
from odoo import models,fields


class teachers(models.Model):
    _name = 'library.teachers'

    matricula = fields.Char(string='Id Docente')
    name = fields.Char(string='Nombre(s)')
    a_paterno = fields.Char(string='Apellido Paterno')
    a_materno = fields.Char(string='Apellido Materno')
    academia = fields.Many2one('library.careers',string='Academia')
    
    _order = 'name'
