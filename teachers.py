# -*- coding: utf-8 -*-
from odoo import models,fields


class teachers(models.Model):
    _name = 'library.teachers'

    matricula = fields.Char(string='Id Docente', required=True)
    name = fields.Char(string='Nombre(s)', required=True)
    a_paterno = fields.Char(string='Apellido Paterno', required=True)
    a_materno = fields.Char(string='Apellido Materno', required=True)
    academia = fields.Many2one('library.careers', string='Academia', required=True)
    
    _order = 'name'
    _sql_constraints = [ ('id_teacher_uniq', 'unique(matricula)', 'Id de Docente duplicado: ingrese uno distinto') ]
