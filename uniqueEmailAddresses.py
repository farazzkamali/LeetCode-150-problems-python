class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for email in emails:
            i = 0
            local = ""
            while email[i] not in ["@", "+"]:
                if email[i] != ".":
                    local += email[i]
                i += 1

            while email[i] != "@":
                i += 1
            domain = email[i + 1:]
            unique.add((local, domain))
        return len(unique)
