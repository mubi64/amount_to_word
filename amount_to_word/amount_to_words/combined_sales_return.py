import frappe
from amount_to_word.amount_to_words.api import (
    get_df_currency,
    convert_amount_to_words
)

def before_save(doc, method):
    currency = get_df_currency(doc.company)

    # Sales / Return dono ke liye safe
    amount = abs(doc.grand_total) if doc.grand_total else 0

    doc.in_words_arabic = convert_amount_to_words(
        amount,
        "ar",
        currency[0].get("currency") if currency else "SAR"
    )
