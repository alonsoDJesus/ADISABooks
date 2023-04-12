# -*- coding: utf-8 -*-
from odoo import models,fields


class editorials(models.Model):
    _name = 'library.editorials'

    
    id_editorial= fields.Many2one('library.books',string='Identificador de Editorial')
    nombre= fields.Char(string='Nombre de la ')
    estado= fields.Char(string='Estado')
    pais= fields.Char(string='Pais')
    
    _order = 'id_editorial'
