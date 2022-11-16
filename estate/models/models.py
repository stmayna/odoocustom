# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estate(models.Model):
    _name = 'estate'
    _description = 'estate'
    
    name = fields.Char(required=True)
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available From',copy=False, default=lambda self: fields.Datetime.today())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    active = fields.Boolean()
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="It will help the user to choose between 4 orientation."
    )
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_received,', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        copy=False,
    )
    property_type_id = fields.Char(string='Property Type')
    tag_ids = fields.Char()
    offer_ids = fields.Many2one('estate.property.offer')
