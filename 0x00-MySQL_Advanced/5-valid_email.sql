-- Resets valid_email if the email changed
DELIMITER / /

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END //