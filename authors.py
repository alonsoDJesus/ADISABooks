from odoo import models, fields

class authors(models.Model):
    _name = 'library.authors'

    a_paterno = fields.Char( string='Apellido Paterno', required=True)
    name = fields.Char( string='Nombre', required=True )
    degree = fields.Char( string= 'Grado Académico' )
    book2_ids = fields.Many2many('library.books',string='Libros')

    _order = 'name'
    _sql_constraints = [ ('lastName_authors_uniq', 'unique(a_paterno, name)', 'Autor duplicado, escribe uno diferente.') ]
