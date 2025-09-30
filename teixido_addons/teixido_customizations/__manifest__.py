# -*- coding: utf-8 -*-
{
    'name': 'Teixido Customizations',
    'version': '17.0.1.0.20',
    'summary': 'Migración de personalizaciones de Odoo Studio a código',
    'category': 'Customization',
    'author': 'Arkiphere',
    'license': 'OEEL-1',
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/studio_deactivation.xml',
        'views/crm_lead_form_odoo_studio_crm.lead.form_customization.xml',
        'views/crm_lead_search_odoo_studio_crm.lead.search.opportunity_customization.xml',
        'views/res_partner_form_safe.xml',
        'views/res_partner_search_odoo_studio_res.partner.select_customization.xml',
        'views/res_partner_tree_odoo_studio_res.partner.tree_customization.xml',
    ],
    'installable': True,
    'application': False,
}
