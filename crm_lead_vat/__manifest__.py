# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "VAT in leads",
    "summary": "Add VAT field to leads",
    "version": "17.0.1.0.1",
    "category": "Customer Relationship Management",
    "website": "https://github.com/OCA/crm",
    "author": "Antiun Ingeniería S.L., Odoo Community Association (OCA)",
    "maintainers": ["EmilioPascual"],
    "license": "AGPL-3",
    "application": False,
    "description": """
VAT in leads
============
This module adds VAT field to leads, so you can specify VAT of the contact
in leads.
    """,
    "installable": True,
    "depends": ["crm"],
    "data": ["views/crm_lead_views.xml"],
}
