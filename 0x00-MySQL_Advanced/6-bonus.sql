-- An SQL script that creates a stored procedure 
-- AddBonus which adds a new correction for a student

DELIMITER//
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus( IN user_id INT, IN project_name VARCHAR(255), IN score INT
)
BEGIN
   DECLARE project_id INT;

   IF NOT EXISTS (SELECT 1 FROM projects WHERE name=project_name) THEN
      INSERT INTO projects (name) VALUES (project_name);
   END IF;

   SET project_id = (SELECT id FROM projects WHERE name = project_name);

   INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score );
END//
DELIMITER;//
