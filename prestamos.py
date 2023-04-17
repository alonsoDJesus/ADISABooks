# -- coding: utf-8 --
from odoo import fields, models, api

class prestamos(models.Model):
    _name = 'library.prestamos'
    
    name = fields.Char(string='folio', readonly=True, default='Nuevo Prestamo', copy=False)   
    book_id = fields.Many2many('library.books', string='Libro', required=True)
    fecha_prestamo = fields.Date(string='Fecha de préstamo', required=True)
    fecha_entrega = fields.Date(string='Fecha de vencimiento', required=True)
    tipo = fields.Selection([('nin','Ninguno'),('student','Estudiante'),('teacher','Maestro')],string='Usuario',default='nin')
    id_estudiante = fields.Many2one('library.students',string='Estudiante')
    id_docente = fields.Many2one('library.teachers',string='Docente')
    state = fields.Selection([('cre','Creado'),('rea','Realizo'),('can','Cancelado')],string='Estado',readonly=True, default='cre')
    

    _order = 'name'

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo Prestamo') == 'Nuevo Prestamo':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.prestamos_folio')  or 'Nuevo Prestamo'

        result = super(prestamos, self). create(vals)
        return result