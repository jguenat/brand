# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = ['account.invoice', 'res.brand.mixin']

    brand_id = fields.Many2one(
        states={
            'in_payment': [('readonly', True)],
            'paid': [('readonly', True)],
            'cancel': [('readonly', True)],
        }
    )
    brand_name = fields.Many2one(
        comodel_name="res.brand.name",
        string="Template",
        help="Ce template sera utilisé pour ce document",
    )

    @api.onchange('brand_name')
    def _onchange_brand_name(self):
        self.brand_id = self.brand_name.brand
        self.partner_bank_id = self.brand_name.bank


    @api.multi
    def _is_brand_required(self):
        self.ensure_one()
        if self.type in ('in_invoice', 'in_refund'):
            return False
        return super(AccountInvoice, self)._is_brand_required()

    @api.model
    def _prepare_refund(self, invoice, date_invoice=None, date=None,
                        description=None, journal_id=None):
        values = super(AccountInvoice, self)._prepare_refund(
            invoice, date_invoice=date_invoice, date=date,
            description=description, journal_id=journal_id)
        if invoice.brand_id and invoice.brand_name:
            values['brand_id'] = invoice.brand_id.id
            values['brand_name'] = invoice.brand_name.id
        return values
