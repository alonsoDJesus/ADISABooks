# -*- coding: utf-8 -*-
from odoo import models,fields

class editorials(models.Model):
    _name = 'library.editorials'

    name= fields.Char(string='Lista de editoriales',required=True)
    estado= fields.Char(string='Estado',required=True)
    pais= fields.Char(string='Pais',required=True)
    books_id = fields.One2many('library.books','id_editorial',string='Libros',readonly=True)

    _order = 'name'
    _sql_constraints = [('editorials_uniq', 'unique(name)', 'Editorial duplicada, intenta con otra...'),]
