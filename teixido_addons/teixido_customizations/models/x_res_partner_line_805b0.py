# -*- coding: utf-8 -*-

from odoo import models, fields


class XResPartnerLine805B0(models.Model):
    _name = 'x_res_partner_line_805b0'
    _description = 'Studio Partner Line (compat)'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    active = fields.Boolean(default=True)
    
    # Studio fields migrated to custom module

    teix_sequence = fields.Integer(
        string='Secuencia',
    )
