insert_base_user = """
INSERT INTO BASE_USER (user_name, email, phone_number, address)
 VALUES (:user_name, :email, :phone_number, :address
 )
"""


if_user_exists = """
SELECT USER_NAME FROM BASE_USER WHERE USER_NAME=?
"""
