-- Search 
CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

-- Pagination
CREATE OR REPLACE FUNCTION get_paginated(lim INT, off INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
