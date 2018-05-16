insert_base_user = """
INSERT INTO BASE_USER (user_name, email, phone_number, address)
 VALUES (:user_name, :email, :phone_number, :address
 )
"""