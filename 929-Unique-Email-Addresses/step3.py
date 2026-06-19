class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            email_parts = email.partition("@")
            domain_name = email_parts[2]
            local_name = email_parts[0]
            normalized_local_name = local_name.split("+")[0].replace(".", "")
            unique_emails.add(f"{normalized_local_name}@{domain_name}")

        return len(unique_emails)
