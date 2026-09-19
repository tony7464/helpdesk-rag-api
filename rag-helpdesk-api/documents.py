"""
Approved support documents for the simplified RAG workflow.

In this lesson, the documents are stored in a Python list so you can focus on
how the API retrieves context and builds a grounded prompt.
"""

DOCUMENTS = [
    {
        "id": "it_password_reset",
        "title": "Password Reset Policy",
        "category": "accounts",
        "text": (
            "Employees must reset their password through the internal account portal. "
            "After opening the portal, choose 'Forgot password', verify your identity, "
            "and create a new password with at least 12 characters. If the reset link "
            "does not arrive within 10 minutes, contact the IT help desk."
        ),
        "tags": ["password", "reset", "account", "login", "portal", "help desk"],
    },
    {
        "id": "it_vpn_troubleshooting",
        "title": "VPN Troubleshooting Guide",
        "category": "network",
        "text": (
            "Employees who cannot connect to the VPN should first confirm they are connected "
            "to the internet, then restart the VPN client. If the issue continues, they should "
            "check for client updates and retry multi-factor authentication. Persistent VPN "
            "issues should be escalated to the network support team."
        ),
        "tags": ["vpn", "network", "remote", "connection", "mfa", "troubleshooting"],
    },
    {
        "id": "it_phishing_reporting",
        "title": "Phishing Email Reporting Procedure",
        "category": "security",
        "text": (
            "Employees should report suspicious emails by using the 'Report Phishing' button "
            "in the mail client. Do not click links, open attachments, or reply to the sender. "
            "If credentials were entered on a suspicious site, immediately reset the password "
            "and notify the security team."
        ),
        "tags": ["phishing", "email", "security", "suspicious", "report", "credentials"],
    },
    {
        "id": "it_software_access",
        "title": "Software Access Request Process",
        "category": "software",
        "text": (
            "Employees who need access to approved software should submit a software access "
            "request through the service catalog. The request must include the business reason, "
            "manager approval, and the required tool name. Most approved requests are processed "
            "within three business days."
        ),
        "tags": ["software", "access", "license", "tools", "approval", "service catalog"],
    },
    {
        "id": "it_device_replacement",
        "title": "Device Replacement Policy",
        "category": "hardware",
        "text": (
            "Company laptops are eligible for replacement after four years or when repair is "
            "not cost-effective. Employees should submit a hardware ticket with the device "
            "serial number, a description of the issue, and any troubleshooting steps already "
            "attempted."
        ),
        "tags": ["laptop", "device", "hardware", "replacement", "repair", "ticket"],
    },
    {
        "id": "it_file_storage",
        "title": "Approved File Storage Locations",
        "category": "data",
        "text": (
            "Employees must store company documents in approved cloud storage locations. "
            "Sensitive files should not be saved on personal drives or sent through personal "
            "email accounts. Teams should use shared folders with appropriate access controls "
            "for collaborative work."
        ),
        "tags": ["storage", "files", "cloud", "sensitive", "access controls", "documents"],
    },
]