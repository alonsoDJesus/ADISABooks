# -*- coding: utf-8 -*-
from odoo import models,fields


class books(models.Model):
    _name = 'library.books'

    isbn= fields.Char(string='ISBN')
    name= fields.Char(string='Titulo', required=True)
    anio_edicion= fields.Char(string='Año de edicion',required=True)
    no_paginas= fields.Integer(string='Número de Páginas', required=True)
    existencias= fields.Integer(string='Número de Existencia', required=True)
    id_categoria= fields.Many2many('library.categorys',string='Categoria', required=True)
    id_editorial= fields.Many2one('library.editorials',string='Editorial', required=True)
    author2_ids = fields.Many2many('library.authors',string='Autor(es)')

    _sql_constraints = [('isbn_uniq', 'unique(isbn)', 'ISBN duplicada, intenta con otra...'),]
   
    _order = 'name,isbn'
