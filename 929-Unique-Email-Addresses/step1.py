class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_email = set()
        for email in emails:
            parts = email.split("@")
            local_name = parts[0]
            domain_name = parts[1]

            local_name = "".join(local_name.split("+")[0].split("."))

            unique_email.add(local_name + "@" + domain_name)

        return len(unique_email)
