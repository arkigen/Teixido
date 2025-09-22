# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Res_Partner(models.Model):
    _inherit = 'res.partner'
    
    # Studio fields migrated to custom module

    teix_Grupo_Empresarial = fields.Many2one(
        string='Pertenece a un Grupo Empresarial',
        comodel_name='res.partner',
    )

    teix_alta_pt = fields.Date(
        string='Alta PT',
    )

    teix_cd = fields.Boolean(
        string='Canal de denúncias',
    )

    teix_cfd = fields.Boolean(
        string='Firman contractos digitalment con KF',
    )

    teix_colaborador = fields.Many2one(
        string='Colaborador',
        comodel_name='res.partner',
    )

    teix_contratos_activos = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_contratos_activos_rel',
        column1='partner_id',
        column2='related_partner_id',
        string='Contratos Activos / Historicos',
    )

    teix_delegacion = fields.Many2one(
        string='Oficina de Facturación del Cliente',
        comodel_name='res.partner',
    )

    teix_dni = fields.Char(
        string='DNI / TIE / NIE',
    )

    teix_importe_del_servicio = fields.Integer(
        string='Importe del Servicio',
    )

    teix_kf = fields.Boolean(
        string='Konfirma',
    )

    teix_lopd = fields.Boolean(
        string='LOPD Protecció de datos',
    )

    teix_many2many_field_43n_1j33hkn81 = fields.Many2many(
        string='Areas con Servicios activos',
        comodel_name='documents.tag',
        relation='teix_partner_documents_tag_rel',
        column1='partner_id',
        column2='tag_id',
    )

    teix_n_de_nominas = fields.Integer(
        string='Nº de Trabajadores',
    )

    teix_one2many_field_885_1j32d381d = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_partner_rel_885_1j32d381d',
        column1='partner_id',
        column2='related_partner_id',
        string='Nuevo One2Many',
    )

    teix_one2many_field_8e0_1j32d56ae = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_partner_rel_8e0_1j32d56ae',
        column1='partner_id',
        column2='related_partner_id',
        string='Nuevo One2Many',
    )

    teix_pe = fields.Boolean(
        string='Portal de Empleado ',
    )

    teix_pedidos = fields.Many2one(
        string='Pedidos',
        comodel_name='sale.order',
    )

    teix_pl = fields.Boolean(
        string='Plan deI Igualtat',
    )

    teix_prevenci_activo = fields.Boolean(
        string='Es Cliente Prevención de Teixidó',
    )

    teix_proveedor_actual = fields.Many2one(
        string='Contratado con',
        comodel_name='res.partner',
    )

    teix_re = fields.Boolean(
        string='Resgistra Entrada',
    )

    teix_servicios_contratados = fields.Boolean(
        string='Relación Contratos / Servicios Activos',
    )

    teix_spa_notes = fields.Html(
        string='SPA Observaciones',
    )

    teix_tei = fields.Boolean(
        string='TEI 24',
    )

    # Computed flags for tag-driven visibility on the form
    teix_tag_laboral = fields.Boolean(string='Tiene etiqueta Laboral', compute='_compute_teix_tag_flags', store=False)
    teix_tag_fiscal = fields.Boolean(string='Tiene etiqueta Fiscal', compute='_compute_teix_tag_flags', store=False)
    teix_tag_asesoria = fields.Boolean(string='Tiene etiqueta Asesoria', compute='_compute_teix_tag_flags', store=False)
    teix_tag_prevencion = fields.Boolean(string='Tiene etiqueta Prevención', compute='_compute_teix_tag_flags', store=False)
    teix_tag_juridico = fields.Boolean(string='Tiene etiqueta Juridico', compute='_compute_teix_tag_flags', store=False)

    @api.depends('category_id', 'category_id.name')
    def _compute_teix_tag_flags(self):
        """Compute presence of key tags by name (case-insensitive contains)."""
        for partner in self:
            names = set((partner.category_id.mapped('name') or []))
            lowered = {n.lower() for n in names}
            def has(term: str) -> bool:
                t = term.lower()
                return any(t in n for n in lowered)
            partner.teix_tag_laboral = has('laboral')
            partner.teix_tag_fiscal = has('fiscal')
            partner.teix_tag_asesoria = has('asesor') or has('asesoría') or has('asesoria')
            partner.teix_tag_prevencion = has('prevenci')
            partner.teix_tag_juridico = has('jurid') or has('juríd')

    @api.onchange('category_id')
    def _onchange_category_id_update_flags(self):
        """Ensure booleans reflect current tags immediately in the form UI."""
        for partner in self:
            names = set((partner.category_id.mapped('name') or []))
            lowered = {n.lower() for n in names}
            def has(term: str) -> bool:
                t = term.lower()
                return any(t in n for n in lowered)
            partner.teix_tag_laboral = has('laboral')
            partner.teix_tag_fiscal = has('fiscal')
            partner.teix_tag_asesoria = has('asesor') or has('asesoría') or has('asesoria')
            partner.teix_tag_prevencion = has('prevenci')
            partner.teix_tag_juridico = has('jurid') or has('juríd')
