# -*- coding: utf-8 -*-
from odoo import models,fields


class books(models.Model):
    _name = 'library.books'

<<<<<<< HEAD
    isbn= fields.Char(string='ISBN')
    author=fields.Char(string='Autor')
=======
    isbn= fields.Char(string='ISBN', required=True)
>>>>>>> cc81f62f2835c123e485b9b67e66c7f9bfdc695c
    name= fields.Char(string='Titulo', required=True)
    anio_edicion= fields.Char(string='Año de edicion',required=True)
    no_paginas= fields.Integer(string='Número de Páginas', required=True)
    existencias= fields.Integer(string='Número de Existencia', required=True)
<<<<<<< HEAD
    id_categoria= fields.Many2many('library.categorys',string='Categoria')
    id_editorial= fields.Many2one('library.editorials',string='Editorial', required=True)
    author_id = fields.Many2many( 'library.authors', 'book_id', string ='Autor' )
    #id_author_book = fields.Many2One('library.authors_books', string='Autor', required=True)

    _order = 'name'
    _sql_constraints = [('isbn_uniq', 'unique(isbn)', 'ISBN duplicada, intenta con otra...'),]
=======
    id_categoria= fields.Many2one('library.categorys',string='Categoria', required=True)
    id_editorial= fields.Many2one('library.editorials',string='Editorial', required=True)
    author_ids = fields.One2many( 'library.authors', 'book_id', string = 'Autor' )
    author_id = fields.Many2one( 'library.authors', string = 'Autores' )
    #id_author_book = fields.Many2One('library.authors_books', string='Autor', required=True)
    
    _order = 'name,isbn'
>>>>>>> cc81f62f2835c123e485b9b67e66c7f9bfdc695c
