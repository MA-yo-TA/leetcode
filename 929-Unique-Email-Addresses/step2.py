class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            at_split = email.split("@")
            domain_name = at_split[1]
            local_name = at_split[0]
            normalized_local_name = local_name.split("@")[0].replace(".", "")
            unique_emails.add(normalized_local_name + "@" + domain_name)

        return len(unique_emails)
