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
  `contact_contact_id` INTEGER NOT NULL,
  `document_name` VARCHAR(45) NULL,
  `created_at` TIMESTAMP DEFAULT NOW,
  `updated_at` TIMESTAMP DEFAULT NOW,
  `document_type_document_type_id` INTEGER NOT NULL,
  PRIMARY KEY (`document_id`),
    FOREIGN KEY (`contact_contact_id`)
    REFERENCES `contact` (`contact_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`document_type_document_type_id`)
    REFERENCES `document_type` (`document_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table `contact`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `contact` (
  `contact_id` INTEGER NOT NULL,
  `contact_user_id` INTEGER NOT NULL,
  `contact_user_name` VARCHAR(45) NULL,
  `user_userid` INTEGER NOT NULL,
  `document_document_id` INTEGER NOT NULL,
  PRIMARY KEY (`contact_id`),
    FOREIGN KEY (`user_userid`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`document_document_id`)
    REFERENCES `document` (`document_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table `message`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `message` (
  `message_id` INTEGER NOT NULL,
  `user_user_id` INTEGER NOT NULL,
  `content` VARCHAR(30000) NOT NULL,
  `created_at` TIMESTAMP DEFAULT NOW,
  `viewed` TIMESTAMP DEFAULT NOW,
  `document_document_id` INTEGER NOT NULL,
  PRIMARY KEY (`message_id`),
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`document_document_id`)
    REFERENCES `document` (`document_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TRIGGER IF NOT EXISTS user_insert INSERT ON user
FOR EACH ROW
BEGIN
	UPDATE user SET username = NEW.email WHERE NEW.username IS NULL; END;
