# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crm_Lead(models.Model):
    _inherit = 'crm.lead'
    
    # Studio fields migrated to custom module

    teix_alta_pt = fields.Date(
        string='Alta PT',
        help='Importe del Año Anterior',
        related='partner_id.teix_alta_pt',
        readonly=True,
        store=False,
    )

    teix_contacto = fields.Many2one(
        string='Contacto',
        comodel_name='res.partner',
    )

    teix_proveedor_actual = fields.Many2one(
        string='Proveedor Actual',
        comodel_name='res.partner',
        related='partner_id.teix_proveedor_actual',
        readonly=True,
        store=False,
    )

    teix_selection_actual = fields.Selection(
        string='Actual',
        selection=[('Actual', 'EUROPREVEN'), ('PREVINTEGRAL', 'PREVINTEGRAL'), ('VITALY', 'VITALY'), ('AVANTA', 'AVANTA'), ('ALTRES', 'ALTRES')],
    )

    teix_servei_prevencio = fields.Boolean(
        string='Servei de prevenció',
        related='partner_id.teix_prevenci_activo',
        readonly=True,
        store=False,
    )

    # Visibility flags (related to partner's booleans)
    teix_tag_laboral = fields.Boolean(related='partner_id.teix_tag_laboral', readonly=True)
    teix_tag_fiscal = fields.Boolean(related='partner_id.teix_tag_fiscal', readonly=True)
    teix_tag_asesoria = fields.Boolean(related='partner_id.teix_tag_asesoria', readonly=True)
    teix_tag_prevencion = fields.Boolean(related='partner_id.teix_tag_prevencion', readonly=True)
    teix_tag_juridico = fields.Boolean(related='partner_id.teix_tag_juridico', readonly=True)
    teix_tag_otros_servicios = fields.Boolean(related='partner_id.teix_tag_otros_servicios', readonly=True)
    teix_tag_rgpd = fields.Boolean(related='partner_id.teix_tag_rgpd', readonly=True)
    teix_tag_spa_colaboradores = fields.Boolean(related='partner_id.teix_tag_spa_colaboradores', readonly=True)
    teix_tag_seguros = fields.Boolean(related='partner_id.teix_tag_seguros', readonly=True)

    # Notas (related a partner para que se vean/editan igual desde CRM pero en solo lectura)
    teix_notas_fiscal = fields.Html(related='partner_id.teix_notas_fiscal', readonly=True)
    teix_notas_juridico = fields.Html(related='partner_id.teix_notas_juridico', readonly=True)
    teix_notas_laboral = fields.Html(related='partner_id.teix_notas_laboral', readonly=True)
    teix_notas_rgpd = fields.Html(related='partner_id.teix_notas_rgpd', readonly=True)
    teix_notas_spa_colaboradores = fields.Html(related='partner_id.teix_notas_spa_colaboradores', readonly=True)
    teix_notas_seguros = fields.Html(related='partner_id.teix_notas_seguros', readonly=True)
    teix_spa_notes = fields.Html(related='partner_id.teix_spa_notes', readonly=True)

    # Otros campos mostrados en pestañas
    teix_n_de_nominas = fields.Integer(related='partner_id.teix_n_de_nominas', readonly=True)
    teix_importe_del_servicio = fields.Integer(related='partner_id.teix_importe_del_servicio', readonly=True)

    # Booleans de "Otros Servicios" (solo lectura) 
    teix_tei = fields.Boolean(related='partner_id.teix_tei', readonly=True)
    teix_pe = fields.Boolean(related='partner_id.teix_pe', readonly=True)
    teix_lopd = fields.Boolean(related='partner_id.teix_lopd', readonly=True)
    teix_cfd = fields.Boolean(related='partner_id.teix_cfd', readonly=True)
    teix_pl = fields.Boolean(related='partner_id.teix_pl', readonly=True)
    teix_re = fields.Boolean(related='partner_id.teix_re', readonly=True)
    teix_kf = fields.Boolean(related='partner_id.teix_kf', readonly=True)
    teix_cd = fields.Boolean(related='partner_id.teix_cd', readonly=True)
