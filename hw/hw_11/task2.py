def hide_email(email):
    dog = email.index('@')
    new_email = email[:dog - 3] + '***@**' + email[dog + 3:]
    return new_email


email = 'danil.churko@gmail.com'
print(hide_email(email))
