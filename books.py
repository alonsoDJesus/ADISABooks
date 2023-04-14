# -*- coding: utf-8 -*-
from odoo import models,fields


class books(models.Model):
    _name = 'library.books'

    isbn= fields.Char(string='ISBN', required=True)
    name= fields.Char(string='Titulo', required=True)
    anio_edicion= fields.Char(string='Año de edicion',required=True)
    no_paginas= fields.Integer(string='Número de Páginas', required=True)
    existencias= fields.Integer(string='Número de Existencia', required=True)
    id_categoria= fields.Many2one('library.categorys',string='Categoria', required=True)
    id_editorial= fields.Many2one('library.editorials',string='Editorial', required=True)
    author2_ids = fields.Many2many('library.authors',string='Autor(es)')
    ##author_ids = fields.One2many( 'library.authors', 'book_id', string = 'Autor' )
    ##author_id = fields.Many2one( 'library.authors', string = 'Autores' )
    #id_author_book = fields.Many2One('library.authors_books', string='Autor', required=True)
    
    _order = 'name,isbn'
