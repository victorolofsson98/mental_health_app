Create DATABASE IF NOT EXISTS mental_health_app;


CREATE USER if not exists 'mental_health_admin'@'localhost' IDENTIFIED BY 'mental_health123';
GRANT ALL PRIVILEGES ON
    `mental_health_app`.* TO `mental_health_admin`@`localhost` WITH GRANT OPTION;


USE mental_health_app;

CREATE TABLE  if not exists `users` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`userID`)
);

CREATE TABLE if not exists daily_questions(
	for_date DATE,
    userID int,
    amount_sleep DOUBLE not null,
    nutrition_score INT not null,
    amount_exercise DOUBLE not null,
    amount_social_activity DOUBLE not null,
    happiness_score INT not null,
    
    primary key(for_date),
    FOREIGN KEY(userId) REFERENCES users(userID) ON DELETE CASCADE
);


CREATE TABLE if not exists articles(
	articleID int NOT NULL AUTO_INCREMENT,
    articleType varchar(100),
    articleLink varchar(100),
    primary key(articleID)
);


INSERT INTO `articles`
VALUES
(default,'depression','https://www.healthline.com/health/depression/how-to-fight-depression#overview'),
(default,'loneliness','https://www.mcleanhospital.org/essential/4-steps-walk-away-loneliness'),
(default,'anxiety','https://www.mayoclinic.org/diseases-conditions/anxiety/diagnosis-treatment/drc-20350967');

