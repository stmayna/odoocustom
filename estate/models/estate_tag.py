# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import unique


class EstatePropertyTag(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _name = 'estate.property.tag'
    _description = 'estate.property.tag'
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # ---------------------------------------- Fields Declaration -------------------------------------

    name = fields.Char(required=True)
    color = fields.Integer("Color Index")
