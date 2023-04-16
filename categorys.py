# -*- coding: utf-8 -*-
from odoo import models,fields

class categorys(models.Model):
    _name = 'library.categorys'

    name= fields.Char(string='Lista de Categorias',required=True)
    books_id = fields.One2many('library.books','id_categoria',string='Libros',readonly=True)
        
    _order = 'name'
    _sql_constraints = [('categorys_uniq', 'unique(name)', 'Categoria duplicada, intenta con otra...'),]
