def hide_email(email):
    dog = email.index('@')
    new_emai = email[:dog - 3] + '***@**' + email[dog + 3:]
    return new_emai


email = 'danil.churko@gmail.com'
print(hide_email(email))
