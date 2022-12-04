-- -----------------------------------------------------
-- Table `user`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INTEGER NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45),
  `password` VARCHAR(45) NOT NULL,
  `photo` VARCHAR(45),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, --DEFAULT NOW(),
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, --DEFAULT NOW(),
  PRIMARY KEY (`user_id`));

-- -----------------------------------------------------
-- Table `document_type`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `document_type` (
  `document_type_id` INTEGER NOT NULL,
  `document_type_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`document_type_id`));

-- -----------------------------------------------------
-- Table `document`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `document` (
  `document_id` INTEGER NOT NULL,
  `document_name` VARCHAR(45) NULL,
  `created_at` TIMESTAMP DEFAULT NOW,
  `updated_at` TIMESTAMP DEFAULT NOW,
  PRIMARY KEY (`document_id`));

-- -----------------------------------------------------
-- Table `contact`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `contact` (
  `contact_id` INTEGER NOT NULL,
  `contact_user_id` INTEGER NOT NULL,
  `contact_user_name` VARCHAR(45) NULL,
  PRIMARY KEY (`contact_id`));

-- -----------------------------------------------------
-- Table `message`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `message` (
  `message_id` INTEGER NOT NULL,
  `content` VARCHAR(30000) NOT NULL,
  `created_at` TIMESTAMP DEFAULT NOW,
  `viewed` TIMESTAMP DEFAULT NOW,
  
  PRIMARY KEY (`message_id`));


CREATE TRIGGER IF NOT EXISTS user_insert INSERT ON user
FOR EACH ROW
BEGIN
	UPDATE user SET username = NEW.email WHERE NEW.username IS NULL; END;
