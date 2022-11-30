CREATE TABLE
    `data`(
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` TEXT NOT NULL,
        `date` DATE NOT NULL,
        `words` LONGTEXT NOT NULL
    );

ALTER TABLE `data` ADD PRIMARY KEY `data_id_primary`(`id`);
