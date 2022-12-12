# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


class Estate(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _name = 'estate'
    _description = 'estate'
    _order = "id desc"

    # ---------------------------------------- Fields Declaration -------------------------------------

    name = fields.Char(required=True)
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one(
        'res.partner', string='Buyer', index=True, copy=False)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        'Available From', copy=False, default=lambda self: fields.Datetime.today())
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
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
        help="It will help the user to choose between 4 orientation."
    )
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_received,', 'Offer Received'),
                   ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        copy=False,
        string="Status"
    )
    property_type_id = fields.Many2one(
        'estate.property.type', string='Property Type')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many(
        'estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Integer(compute='_compute_total_area')
    best_price = fields.Float(
        compute='_compute_best_price', string='Best Offer', help="Best offer received")

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for offer in self:
            offer.best_price = max(offer.offer_ids.mapped(
                'price')) if offer.offer_ids else 0.0

    # ----------------------------------- Constrains and Onchanges --------------------------------

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for prop in self:
            if (
                not float_is_zero(prop.selling_price, precision_rounding=0.01)
                and float_compare(prop.selling_price, prop.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )

    # ---------------------------------------- Action Methods -------------------------------------

    def action_sold(self):
        if 'canceled' in self.mapped('state'):
            raise UserError("Canceled properties cannot be sold.")
        return self.write({'state': 'sold'})

    def action_cancel(self):
        if 'sold' in self.mapped('state'):
            raise UserError("Canceled properties cannot be sold.")
        return self.write({'state': 'canceled'})

    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_canceled(self):
        if not set(self.mapped("state")) <= {"new", "canceled"}:
            raise UserError("Only new and canceled properties can be deleted.")
