import frappe
from frappe.utils import money_in_words
from num2words import num2words

@frappe.whitelist()
def convert_amount_to_words(amount, lang, currency):
    doc = num2words(amount, lang=lang, to='currency', currency=currency)

    return doc