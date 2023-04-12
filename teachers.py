# -*- coding: utf-8 -*-
from odoo import models,fields


class teachers(models.Model):
    _name = 'library.teachers'

    
    nombres= fields.Char(string='Nombre(s)')
    a_paterno= fields.Char(string='Apellido Paterno')
    a_materno= fields.Char(string='Apellido Materno')
    academio= fields.Char(string='Academia')
    
    _order = 'nombres'
