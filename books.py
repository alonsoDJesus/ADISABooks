# -*- coding: utf-8 -*-
from odoo import models,fields


class books(models.Model):
    _name = 'library.books'

    isbn= fields.Char(string='ISBN')
    name= fields.Char(string='Titulo')
    anio_edicion= fields.Char(string='Año de edicion')
    no_paginas= fields.Integer(string='Número de Páginas')
    existencias= fields.Integer(string='Número de Existencia')
    
    _order = 'name,isbn'
    
class category(models.Model):
    _name = 'library.category'

    id_categoria= fields.Many2one('library.books',string='Identificador de Categoria')
    name= fields.Integer(string='Nombre')
    
    _order = 'id_categoria'
