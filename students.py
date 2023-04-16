# -*- coding: utf-8 -*-
from odoo import models,fields, api

class students(models.Model):
    _name = 'library.students'

    no_control = fields.Char(string='Numero de Control', readonly = True)
    a_paterno = fields.Char(string='Apelllido paterno', required=True)
    a_materno= fields.Char(string='Apelllido materno', required=True)
    name = fields.Char(string='Nombre(s)', required=True)
    id_carrera= fields.Many2one('library.careers',string='Carrera', required=True)
    
    _order = 'no_control'
    _sql_constraints = [ ('id_students_uniq', 'unique(no_control)', 'No. de Control duplicado: ingrese uno distinto') ]

    @api.model
    def create(self,vals):
        vals['no_control'] = self.env['ir.sequence'].next_by_code('library.students.nocontrol')

        return super(students,self).create(vals)
    
class career(models.Model):
    _name = 'library.careers'

    id_carrera= fields.One2many('library.students','id_carrera',string='Carrera')
    name = fields.Char(string='Carrera', required=True)
    clave = fields.Char(string='Clave', required=True)
    
    _sql_constraints = [ ('career_uniq', 'unique(name)', 'Nombre de carrera duplicada, ingrese una nueva'),
                         ('id_career_uniq', 'unique(clave)', 'Clave de carrera duplicada, ingrese una nueva')]
    _order = 'id_carrera'
