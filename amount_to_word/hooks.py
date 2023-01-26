from . import __version__ as app_version

app_name = "amount_to_word"
app_title = "Amount To Words"
app_publisher = "Sowaan"
app_description = "Frappe App to convert amount to words in arabic in sales invoice"
app_email = "info@sowaan.com"
app_license = "MIT"

fixtures = [
    {
        "doctype":"Custom Field",
        "filters":[
            [
                "fieldname","in",("in_words_arabic")
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amount_to_word/css/amount_to_word.css"
# app_include_js = "/assets/amount_to_word/js/amount_to_word.js"

# include js, css files in header of web template
# web_include_css = "/assets/amount_to_word/css/amount_to_word.css"
# web_include_js = "/assets/amount_to_word/js/amount_to_word.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amount_to_word/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "amount_to_word.utils.jinja_methods",
#	"filters": "amount_to_word.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "amount_to_word.install.before_install"
# after_install = "amount_to_word.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "amount_to_word.uninstall.before_uninstall"
# after_uninstall = "amount_to_word.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amount_to_word.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
    "Sales Invoice":{
        "before_save": "amount_to_word.amount_to_words.sales_invoice.before_save"
    },
    "Sales Order":{
        "before_save": "amount_to_word.amount_to_words.sales_order.before_save"
    },
    "Quotation":{
        "before_save": "amount_to_word.amount_to_words.quotation.before_save"
    },
    "Purchase Invoice":{
        "before_save": "amount_to_word.amount_to_words.purchase_invoice.before_save"
    },
    "Purchase Order":{
        "before_save": "amount_to_word.amount_to_words.purchase_order.before_save"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"amount_to_word.tasks.all"
#	],
#	"daily": [
#		"amount_to_word.tasks.daily"
#	],
#	"hourly": [
#		"amount_to_word.tasks.hourly"
#	],
#	"weekly": [
#		"amount_to_word.tasks.weekly"
#	],
#	"monthly": [
#		"amount_to_word.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "amount_to_word.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "amount_to_word.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "amount_to_word.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"amount_to_word.auth.validate"
# ]
