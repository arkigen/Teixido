# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crm_Lead(models.Model):
    _inherit = 'crm.lead'
    
    # Studio fields migrated to custom module

    teix_alta_pt = fields.Date(
        string='Alta PT',
        help='Importe del Año Anterior',
    )

    teix_contacto = fields.Many2one(
        string='Contacto',
        comodel_name='res.partner',
    )

    teix_proveedor_actual = fields.Many2one(
        string='Proveedor Actual',
        comodel_name='res.partner',
        readonly=True,
    )

    teix_selection_actual = fields.Selection(
        string='Actual',
        selection=[('Actual', 'EUROPREVEN'), ('PREVINTEGRAL', 'PREVINTEGRAL'), ('VITALY', 'VITALY'), ('AVANTA', 'AVANTA'), ('ALTRES', 'ALTRES')],
    )

    teix_servei_prevencio = fields.Boolean(
        string='Servei de prevenció',
    )
