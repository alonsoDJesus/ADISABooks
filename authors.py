from odoo import models, fields

class authors(models.Model):
    _name = 'library.authors'

    a_paterno = fields.Char( string='Apellido Paterno', required=True)
    name = fields.Char( string='Nombre', required=True )
    degree = fields.Char( string= 'Grado Académico' )
    book_id = fields.Many2one( 'library.books', string = 'Libro' )

    book_ids = fields.One2many( 'library.books', 'author_id', string = 'Libros' )
    #id_author_book = fields.Many2One('library.authors_books', string = )

    _order = 'name'
    _sql_constraints = [ ('lastName_authors_uniq', 'unique(a_paterno, name)', 'Autor duplicado, escribe uno diferente.') ]
#class authors_books(models.Model):
 #   _name = 'library.authors_books'
  #  books_id = fields.One2Many( 'library.books', 'id_author_book', string = 'Libros', readonly=True )
   # authors_id = fields.One2Many( 'library.authors', 'id_author_book', string = 'Autores', readonly=True )
    

