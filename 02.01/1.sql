drop database if exists phonebook;
create database phonebook;
use phonebook;

create table people (
           `id` smallint unsigned not null auto_increment primary key,
     `fullname` varchar(30) not null,
                constraint `CH_people_fullname` check (`fullname` <> ''),
`date of birth` date not null,
       `gender` varchar(10) not null,
                constraint `CH_people_gender` check (`gender` <> ''),
  `phonenumber` varchar(30) not null,
                constraint `CH_people_phonenumber` check (`phonenumber` <> ''),
		 `city` varchar(30) not null,
                constraint `CH_people_city` check (`city` <> ''),
      `country` varchar(30) not null,
                constraint `CH_people_country` check (`country` <> ''),
 `home address` varchar(30) not null,
                constraint `CH_people_home address` check (`home address` <> '')
);
