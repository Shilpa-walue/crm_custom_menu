import frappe

no_cache = 1

def get_context(context):
    csrf_token = frappe.sessions.get_csrf_token()
    frappe.db.commit()
    context.csrf_token = csrf_token

    if frappe.session.user == "Guest":
        frappe.throw("Log in to access Frappe CRM", frappe.AuthenticationError)

    boot = frappe.website.utils.get_boot_data()
    context.boot = boot
