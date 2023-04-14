# -*- coding: utf-8 -*-
from odoo import models,fields

class students(models.Model):
    _name = 'library.students'

<<<<<<< HEAD
    no_control= fields.Many2one('library.lending',string='Identificador de Editorial')
    a_paterno= fields.Integer(string='Apelllido paterno')
    a_materno= fields.Integer(string='Apelllido materno')
    nombres= fields.Char(string='Nombre(s)')
    id_carrera= fields.Many2one('library.career',string='Carrera')
=======
    no_control = fields.Char(string='Numero de Control')
    a_paterno = fields.Char(string='Apelllido paterno')
    a_materno= fields.Char(string='Apelllido materno')
    name = fields.Char(string='Nombre(s)')
    id_carrera= fields.Many2one('library.careers',string='Carrera')
>>>>>>> cc81f62f2835c123e485b9b67e66c7f9bfdc695c
    
    _order = 'no_control'
    
class career(models.Model):
<<<<<<< HEAD
    _name = 'library.career'

    id_carrera= fields.One2Many('library.students','id_carrera',string='Carrera')
    nombres= fields.Char(string='Nombre(s)')
=======
    _name = 'library.careers'

    id_carrera= fields.One2many('library.students','id_carrera',string='Carrera')
    name = fields.Char(string='Carrera')
>>>>>>> cc81f62f2835c123e485b9b67e66c7f9bfdc695c
    
    
    _order = 'id_carrera'