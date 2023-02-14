drop database if exists music_collection;
create database music_collection;
use music_collection;

create table album (
          `id` smallint unsigned not null auto_increment primary key,
       `title` varchar(30) not null
               constraint `CH_album_title` check (`title` <> ''),
`performer_id` smallint unsigned not null,
        `date` date not null,
    `style_id` smallint unsigned not null,
`publisher_id` smallint unsigned not null
);

create table style (
  `id` smallint unsigned not null auto_increment primary key,
`name` varchar(10) not null
       constraint `CH_style_name` check (`name` <> '')
);

create table performer (
  `id` smallint unsigned not null auto_increment primary key,
`name` varchar(30) not null
       constraint `CH_performer_name` check (`name` <> '')
);

create table publisher (
     `id` smallint unsigned not null auto_increment primary key,
   `name` varchar(30) not null
          constraint `CH_publisher_name` check (`name` <> ''),
`country` varchar(30) not null
          constraint `CH_publisher_country` check (`country` <> '')
);

create table songs (
          `id` smallint unsigned not null auto_increment primary key,
        `name` varchar(30) not null
               constraint `CH_songs_name` check (`name` <> ''),
    `album_id` smallint unsigned not null,
        `time` time not null,
    `style_id` smallint unsigned not null,
`performer_id` smallint unsigned not null
);

alter table album
    add constraint `FK_album_performer_id`
		foreign key (`performer_id`)
		references performer (`id`),
    add constraint `FK_album_style_id`
		foreign key (`style_id`)
		references style (`id`),
	add constraint `FK_album_publisher_id`
		foreign key (`publisher_id`)
		references publisher (`id`);

alter table songs
    add constraint `FK_songs_album_id`
		foreign key (`album_id`)
		references album (`id`),
    add constraint `FK_songs_style_id`
		foreign key (`style_id`)
		references style (`id`),
	add constraint `FK_songs_performer_id`
		foreign key (`performer_id`)
		references performer (`id`);
