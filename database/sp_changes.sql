DELIMITER //
create procedure sp_getAdmins()
BEGIN
	select users.full_name, users.phone, users.created_at from user_role inner join users on user_role.user_id = users.id where user_role.role_id = 1;
END //
DELIMITER ; 