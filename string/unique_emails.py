# "Distinct Emails" from SWE Careers

# Every email consists of a local name and a domain name, separated by the @ sign.

# For example, in alice@swecareers.com, alice is the local name, 
# and swecareers.com is the domain name.

# Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods ('.') between some characters in the local name part of 
# an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@swecareers.com" and "alicez@swecareers.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

# If you add a plus ('+') in the local name, everything after the first plus 
# sign will be ignored. This allows certain emails to be filtered, for example 
# m.y+name@email.com will be forwarded to my@email.com.  
# (Again, this rule does not apply for domain names.)

# It is possible to use both of these rules at the same time.

# Given a list of emails, we send one email to each address in the list.  
# How many different addresses actually receive mails? 

# Example 1:

# Input: ["test.email+alex@swecareers.com","test.e.mail+bob.cathy@swecareers.com","testemail+david@swecareer.scode.com"]
# Output: 2
# Explanation: "testemail@swecareers.com" and "testemail@swecareer.scode.com" actually receive mails

def numUniqueEmails(emails):
    uniqueEmails = []
    for email in emails:
        localName = email.split("@")[0]
        domainName = email.split("@")[1]

        # remove dots
        cleanLocalName = localName.replace(".", "")  
        # split string by + and take the first partition
        cleanLocalName = cleanLocalName.split("+")[0]
        
        cleanEmail = cleanLocalName+domainName
        if cleanEmail not in uniqueEmails:
            uniqueEmails.append(cleanEmail)
    
    return len(uniqueEmails)

emails = ["test.email+alex@swecareers.com","test.e.mail+bob.cathy@swecareers.com","testemail+david@swecareer.scode.com"]

print(numUniqueEmails(emails))