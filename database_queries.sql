create database if not exists pythno_mini_project;
use python_mini_project;
create table if not exists users(
    id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    ph_no int(11) not null,
    username varchar(255) not null,
    passw varchar(255) not null,
    address varchar(255) not null,
    primary key(id)
);
desc users;
select * from users;
alter table users modify ph_no decimal(12,0);
