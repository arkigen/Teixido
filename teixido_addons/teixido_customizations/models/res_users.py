# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Res_Users(models.Model):
    _inherit = 'res.users'
    
    # Studio fields migrated to custom module

    teix_Grupo_Empresarial = fields.Many2one(
        string='Pertenece a un Grupo Empresarial',
        comodel_name='res.partner',
    )

    teix_alta_pt = fields.Date(
        string='Alta PT',
    )

    teix_boolean_field_1h9_1j32b0fqr = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_1i3_1j32ar8cr = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_1no_1j32b5hua = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_1qi_1j322de9h = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_26d_1j322gavj = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_27f_1j32avs4b = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_29u_1j321sb9b = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_35v_1j32b7aa0 = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_3hj_1j321ehpl = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_3k7_1j32b6ehd = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_49e_1j322h0bf = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_4bv_1j33j5ign = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_5pk_1j322f4ph = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_6n1_1j32f4pfn = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_7ts_1j32b8i2n = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_di_1j322hq78 = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_ec_1j32aqoki = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_boolean_field_rf_1j3228aei = fields.Boolean(
        string='Nuevo Casilla de verificación',
    )

    teix_cd = fields.Boolean(
        string='Canal de denúncias',
    )

    teix_cfd = fields.Boolean(
        string='Firman contractos digitalment con KF',
    )

    teix_char_field_7tl_1j32e57um = fields.Char(
        string='Nuevo Texto',
    )

    teix_colaborador = fields.Many2one(
        string='Colaborador',
        comodel_name='res.partner',
    )

    teix_contratos_activos = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_users_contratos_activos_rel',
        column1='user_id',
        column2='partner_id',
        string='Contratos Activos / Historicos',
    )

    teix_date_field_574_1j32f7did = fields.Date(
        string='Nuevo Fecha',
    )

    teix_delegacion = fields.Many2one(
        string='Oficina de Facturación del Cliente',
        comodel_name='res.partner',
    )

    teix_dni = fields.Char(
        string='DNI / TIE / NIE',
    )

    teix_html_field_38n_1j32f6g91 = fields.Html(
        string='Nuevo HTML',
    )

    teix_importe_del_servicio = fields.Integer(
        string='Importe del Servicio',
    )

    teix_integer_field_1p_1j321qj63 = fields.Integer(
        string='Nuevo Entero',
    )

    teix_integer_field_4gc_1j32h533s = fields.Integer(
        string='Nuevo Entero',
    )

    teix_integer_field_4he_1j393li4f = fields.Integer(
        string='Nuevo Entero',
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
        relation='teix_many2many_field_43n_1j33hkn81_rel',
    )

    teix_many2one_field_10n_1j32d70tb = fields.Many2one(
        string='Nuevo Many2One',
        comodel_name='res.partner',
    )

    teix_many2one_field_1um_1j32gkpbf = fields.Many2one(
        string='Nuevo Many2One',
        comodel_name='res.partner',
    )

    teix_many2one_field_2cr_1j32cd6f9 = fields.Many2one(
        string='Nuevo Many2One',
        comodel_name='res.partner',
    )

    teix_many2one_field_8du_1j34cm69k = fields.Many2one(
        string='Nuevo Many2One',
        comodel_name='sale.order',
    )

    teix_many2one_field_qc_1j32c360a = fields.Many2one(
        string='Nuevo Many2One',
        comodel_name='res.partner',
    )

    teix_n_de_nominas = fields.Integer(
        string='Nº de Trabajadores',
    )

    teix_nuevo_cacdsilla_de_verificacin = fields.Boolean(
        string='Nuevo CaCDsilla de verificación',
    )

    teix_one2many_field_3k4_1j34j3lt3 = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_users_rel_3k4_1j34j3lt3',
        column1='user_id',
        column2='partner_id',
        string='Nuevas líneas',
    )

    teix_one2many_field_885_1j32d381d = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_users_rel_885_1j32d381d',
        column1='user_id',
        column2='partner_id',
        string='Nuevo One2Many',
    )

    teix_one2many_field_8e0_1j32d56ae = fields.Many2many(
        comodel_name='res.partner',
        relation='teix_users_rel_8e0_1j32d56ae',
        column1='user_id',
        column2='partner_id',
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

    teix_pl_1 = fields.Boolean(
        string='PL',
    )

    teix_portal_de_lempleat_per_als_treballadors = fields.Boolean(
        string='Portal de l’Empleat per als treballadors',
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

    teix_registrae = fields.Boolean(
        string='RegistraE',
    )

    teix_s_de_la_plataforma = fields.Boolean(
        string='Ús de la plataforma',
    )

    teix_servicios_contratados = fields.Boolean(
        string='Relación Contratos / Servicios Activos',
    )

    teix_spa = fields.Html(
        string='SPA',
    )

    teix_spa_notes = fields.Html(
        string='SPA Notes ',
    )

    teix_tei = fields.Boolean(
        string='TEI 24',
    )

    teix_tei24 = fields.Boolean(
        string='TEI24',
    )

    teix_text_field_4l1_1j322vve2 = fields.Text(
        string='Nuevo Texto multilínea',
    )

    teix_tiene_servicios_contratados = fields.Boolean(
        string='Tiene servicios Contratados',
    )
