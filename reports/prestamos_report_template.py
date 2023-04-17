# -*- coding: utf-8 -*-
from odoo import models, api
from datetime import datetime
import math

class prestamo_report_template(models.AbstractModel):
    _name = 'report.htld_carriers.prestamo_report_template'
    _template = 'htld_carriers.prestamo_report_template'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('library.prestamo_report_template')
        # get the records selected for this rendering of the report
        docs = self.env[report.model].browse(docids)
        # return a custom rendering context
        return {
            'docs': docs,
        }
