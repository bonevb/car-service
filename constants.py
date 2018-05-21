insert_base_user = """
INSERT INTO BASE_USER (user_name, email, phone_number, address, type)
 VALUES (:user_name, :email, :phone_number, :address, :type
 )
"""

insert_client_id = """
INSERT INTO CLIENT  VALUES (?)
"""


if_user_exists = """
SELECT USER_NAME FROM BASE_USER WHERE USER_NAME=?
"""

insert_vehicle = """
INSERT INTO VEHICLE (category, make, model, register_number, gear_box, owner) VALUES
 (:category, :make, :model, :register_number, :gear_box, :owner)
"""

select_vehicle = """
SELECT * FROM VEHICLE WHERE OWNER = ?
"""
update_vehicle = """
UPDATE VEHICLE SET (category, make, model, register_number, gear_box, owner) WHERE ID = id
"""
