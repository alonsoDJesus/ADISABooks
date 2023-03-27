# -*- coding: utf-8 -*-
from odoo import models,fields


class books(models.Model):
    _name = 'library.books'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    numero = fields.Integer(string='Número de playera')
    
    _order = 'name'
