# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import unique


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _name = 'estate.property.type'
    _description = 'estate.property.type'
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # ---------------------------------------- Fields Declaration -------------------------------------

    name = fields.Char(required=True)
    property_ids = fields.One2many(
        'estate', 'property_type_id', string="Properties")
