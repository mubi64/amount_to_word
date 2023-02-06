import frappe
from frappe.utils import money_in_words
from num2words import num2words

@frappe.whitelist()
def get_df_currency(company_name):
    doc = frappe.db.get_list('Company', filters={"company_name": company_name}, fields=["default_currency as currency"])

    return doc


@frappe.whitelist()
def convert_amount_to_words(amount, lang, currency):
    str_amount = str(amount)
    if (str_amount[0] == "-"):
        str_amount = str_amount.split("-")
        amount = float(str_amount[1])
    else:
        amount = amount
    
    doc = num2words(amount, lang=lang, to='currency', currency=currency)
    return doc