-- Decrease the quantity of an item after adding a new order

CREATE TRIGGER decrement AFTER
INSERT
    ON orders FOR EACH ROW
UPDATE items
SET
    quantity = quantity - NEW.order_quantity
WHERE
    item_id = NEW.item_id;