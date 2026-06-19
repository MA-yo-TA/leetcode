class Solution:
    def normalize(self, email: str) -> str:
        local_name = ""
        index = 0
        after_plus = False
        while email[index] != "@":
            if not after_plus:
                if email[index] == "+":
                    after_plus = True
                elif email[index] != ".":
                    local_name += email[index]
            index += 1

        return local_name + email[index:]

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            normalized_email = self.normalize(email)
            unique_emails.add(normalized_email)
        return len(unique_emails)
