import enum


class UsersErrors(str, enum.Enum):
    invalid_email = "Incorrect email format"
    invalid_password = "Password should contain X letters and Y numbers"
    invalid_phone = "Invalid phone format"

    not_unique = "Sent params already exist!"
