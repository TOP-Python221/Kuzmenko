drop database if exists music_collection;
create database music_collection;
use music_collection;

create table albums (
          `id` smallint unsigned not null auto_increment primary key,
       `title` varchar(30) not null,
               constraint `CH_albums_title` check (`title` <> ''),
`performer_id` smallint unsigned not null,
        `date` date not null,
    `style_id` smallint unsigned not null,
`publisher_id` smallint unsigned not null
);

create table styles (
  `id` smallint unsigned not null auto_increment primary key,
`name` varchar(10) not null,
       constraint `CH_styles_name` check (`name` <> '')
);

create table performers (
  `id` smallint unsigned not null auto_increment primary key,
`name` varchar(30) not null,
       constraint `CH_performers_name` check (`name` <> '')
);

create table publishers (
     `id` smallint unsigned not null auto_increment primary key,
   `name` varchar(30) not null,
          constraint `CH_publishers_name` check (`name` <> ''),
`country` varchar(30) not null,
          constraint `CH_publishers_country` check (`country` <> '')
);

create table songs (
          `id` smallint unsigned not null auto_increment primary key,
        `name` varchar(30) not null,
               constraint `CH_songs_name` check (`name` <> ''),
    `album_id` smallint unsigned not null,
        `time` time not null,
    `style_id` smallint unsigned not null,
`performer_id` smallint unsigned not null
);

alter table albums
    add constraint `FK_albums_performer_id`
		foreign key (`performer_id`)
		references performers (`id`),
    add constraint `FK_albums_style_id`
		foreign key (`style_id`)
		references styles (`id`),
	add constraint `FK_albums_publisher_id`
		foreign key (`publisher_id`)
		references publishers (`id`);

alter table songs
    add constraint `FK_songs_album_id`
		foreign key (`album_id`)
		references albums (`id`),
    add constraint `FK_songs_style_id`
		foreign key (`style_id`)
		references styles (`id`),
	add constraint `FK_songs_performer_id`
		foreign key (`performer_id`)
		references performers (`id`);
