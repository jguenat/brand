# Copyright 2019 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResBrand(models.Model):

    _name = 'res.brand'
    _description = 'Brand'

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
        index=True,
        auto_join=True,
        delegate=True,
        ondelete="restrict",
    )


class ResBrandName(models.Model):

    _name = 'res.brand.name'
    _description = 'Brand Name'

    name = fields.Char(
        string="Template",
    )
    brand = fields.Many2one(
        comodel_name="res.brand",
        string="brand",
        required=True,
    )
    bank = fields.Many2one(
        comodel_name="res.partner.bank",
        string="Compte bancaire",
        required=True,
    )
