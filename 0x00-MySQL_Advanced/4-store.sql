-- Decrease the quantity of an item after adding a new order
DELIMITER / /

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.order_quantity
    WHERE item_id = NEW.item_id;
END //