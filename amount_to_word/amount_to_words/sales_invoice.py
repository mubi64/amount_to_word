import frappe
from frappe import _
from amount_to_word.amount_to_words.api import convert_amount_to_words


def before_save(doc, method):
    amount = doc.rounded_total if (
        doc.rounded_total is not None and doc.rounded_total > 0) else doc.grand_total
    doc.in_words_arabic = convert_amount_to_words(amount, 'ar', 'SAR')
