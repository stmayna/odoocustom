# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate.property.type'
    
    name = fields.Char(required=True)