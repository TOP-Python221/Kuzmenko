drop database if exists sales;
create database sales;
use sales;

create table buyers (
         `id` smallint unsigned not null auto_increment primary key,
       `name` varchar (10) not null
              constraint `CH_buyers_name` check (`name` <> ''),
      `email` varchar (30) not null
              constraint `CH_buyers_email` check (`email` <> ''),
`phonenumber` varchar(30) not null
              constraint `CH_buyers_phonenumber` check (`phonenumber` <> '')
);

create table sellers (
         `id` smallint unsigned not null auto_increment primary key,
       `name` varchar (10) not null
              constraint `CH_sellers_name` check (`name` <> ''),
      `email` varchar (30) not null
              constraint `CH_sellers_email` check (`email` <> ''),
`phonenumber` varchar(30) not null
              constraint `CH_sellers_phonenumber` check (`phonenumber` <> '')
);

create table sales_info (
 `buyer_id` smallint unsigned not null,
`seller_id` smallint unsigned not null,
  `product` varchar (30) not null
            constraint `CH_sales_info_product` check (`product` <> ''),
    `price` decimal (8, 2) not null
            constraint `CH_sales_info_price` check (`price` > 0),
     `date` date not null default (curdate())
);

alter table sales_info
    add constraint `FK_sales_info_buyer_id`
		foreign key (`buyer_id`)
		references buyers (`id`),
    add constraint `FK_sales_info_seller_id`
		foreign key (`seller_id`)
		references sellers (`id`);
