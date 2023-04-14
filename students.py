# -*- coding: utf-8 -*-
from odoo import models,fields

class students(models.Model):
    _name = 'library.students'

    no_control = fields.Char(string='Numero de Control')
    a_paterno = fields.Char(string='Apelllido paterno')
    a_materno= fields.Char(string='Apelllido materno')
    name = fields.Char(string='Nombre(s)')
    id_carrera= fields.Many2one('library.careers',string='Carrera')
    
    _order = 'no_control'
    
class career(models.Model):
    _name = 'library.careers'

    id_carrera= fields.One2many('library.students','id_carrera',string='Carrera')
    name = fields.Char(string='Carrera')
    
    
    _order = 'id_carrera'