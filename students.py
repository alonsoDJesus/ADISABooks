# -*- coding: utf-8 -*-
from odoo import models,fields

class students(models.Model):
    _name = 'library.students'

    no_control= fields.Many2one('library.lending',string='Identificador de Editorial')
    a_paterno= fields.Integer(string='Apelllido paterno')
    a_materno= fields.Integer(string='Apelllido materno')
    nombres= fields.Char(string='Nombre(s)')
    id_carrera= fields.Many2one('library.career',string='Carrera')
    
    _order = 'no_control'
    
class career(models.Model):
    _name = 'library.career'

    id_carrera= fields.One2Many('library.students','id_carrera',string='Carrera')
    nombres= fields.Char(string='Nombre(s)')
    
    
    _order = 'id_carrera'