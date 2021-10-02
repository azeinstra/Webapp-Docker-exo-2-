create database if not exists webapp;

use webapp;

create table if not exists student(
    id int auto_increment primary key,
    firstname varchar(255),
    lastname varchar(255),
    exam_note float
);

insert into student (firstname, lastname, exam_note) values ('Pamela', 'AFOUDA', 15);
insert into student (firstname, lastname, exam_note) values ('Pierre', 'CASTETS', 17.5);
insert into student (firstname, lastname, exam_note) values ('Alexandre', 'DEBALS', 19);
insert into student (firstname, lastname, exam_note) values ('Aude', 'A', 5);
insert into student (firstname, lastname, exam_note) values ('Lucie', 'B', 10);
insert into student (firstname, lastname, exam_note) values ('Alice', 'C', 7);