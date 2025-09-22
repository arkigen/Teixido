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

    # Campos de notas por área
    teix_notas_fiscal = fields.Html(string='Notas Fiscal')
    teix_notas_juridico = fields.Html(string='Notas Jurídico')
    teix_notas_laboral = fields.Html(string='Notas Laboral')
    teix_notas_rgpd = fields.Html(string='Notas RGPD')
    teix_notas_spa_colaboradores = fields.Html(string='Notas SPA Colaboradores')
    teix_notas_seguros = fields.Html(string='Notas Seguros')

    # Computed flags for tag-driven visibility on the form
    teix_tag_laboral = fields.Boolean(string='Tiene etiqueta Laboral', compute='_compute_teix_tag_flags', store=False)
    teix_tag_fiscal = fields.Boolean(string='Tiene etiqueta Fiscal', compute='_compute_teix_tag_flags', store=False)
    teix_tag_asesoria = fields.Boolean(string='Tiene etiqueta Asesoria', compute='_compute_teix_tag_flags', store=False)
    teix_tag_prevencion = fields.Boolean(string='Tiene etiqueta Prevención', compute='_compute_teix_tag_flags', store=False)
    teix_tag_juridico = fields.Boolean(string='Tiene etiqueta Juridico', compute='_compute_teix_tag_flags', store=False)
    teix_tag_otros_servicios = fields.Boolean(string='Tiene etiqueta Otros Servicios', compute='_compute_teix_tag_flags', store=False)
    teix_tag_rgpd = fields.Boolean(string='Tiene etiqueta RGPD', compute='_compute_teix_tag_flags', store=False)
    teix_tag_spa_colaboradores = fields.Boolean(string='Tiene etiqueta SPA Colaboradores', compute='_compute_teix_tag_flags', store=False)
    teix_tag_seguros = fields.Boolean(string='Tiene etiqueta Seguros', compute='_compute_teix_tag_flags', store=False)

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
            partner.teix_tag_otros_servicios = has('otros servicios') or has('otros')
            partner.teix_tag_rgpd = has('rgpd') or has('lopd') or has('protecci')
            partner.teix_tag_spa_colaboradores = has('spa colaboradores') or has('colaborador')
            partner.teix_tag_seguros = has('seguro') or has('seguros')

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
            partner.teix_tag_otros_servicios = has('otros servicios') or has('otros')
            partner.teix_tag_rgpd = has('rgpd') or has('lopd') or has('protecci')
            partner.teix_tag_spa_colaboradores = has('spa colaboradores') or has('colaborador')
            partner.teix_tag_seguros = has('seguro') or has('seguros')

    # Ejecuta una vez: migración de datos desde campos de Odoo Studio a teix_*
    def _register_hook(self):
        res = super()._register_hook()
        env = self.env
        param_key = 'teixido_customizations.data_migrated_v12'
        if env['ir.config_parameter'].sudo().get_param(param_key):
            return res
        mapping = [
            ('x_studio_prevenci_activo', 'teix_prevenci_activo'),
            ('x_studio_alta_pt', 'teix_alta_pt'),
            ('x_studio_proveedor_actual', 'teix_proveedor_actual'),
            ('x_studio_importe_del_servicio', 'teix_importe_del_servicio'),
            ('x_studio_spa_notes', 'teix_spa_notes'),
            ('x_studio_n_de_nominas', 'teix_n_de_nominas'),
            ('x_studio_tei', 'teix_tei'),
            ('x_studio_pe', 'teix_pe'),
            ('x_studio_lopd', 'teix_lopd'),
            ('x_studio_cfd', 'teix_cfd'),
            ('x_studio_pl', 'teix_pl'),
            ('x_studio_re', 'teix_re'),
            ('x_studio_kf', 'teix_kf'),
            ('x_studio_cd', 'teix_cd'),
            ('x_studio_dni', 'teix_dni'),
        ]
        # Copiar solo si el destino está vacío/False
        partners = env['res.partner'].sudo().search([])
        for partner in partners:
            vals = {}
            for src, dst in mapping:
                if src in partner._fields and dst in partner._fields:
                    src_val = partner[src]
                    dst_val = partner[dst]
                    if src_val and not dst_val:
                        vals[dst] = src_val
            if vals:
                partner.write(vals)
        env['ir.config_parameter'].sudo().set_param(param_key, '1')
        return res
