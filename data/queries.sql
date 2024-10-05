INSERT OR IGNORE INTO users (username)
VALUES
    ('standard_user'),
    ('locked_out_user'),
    ('problem_user'),
    ('performance_glitch_user'),
    ('error_user'),
    ('visual_user');
select * from users;

alter table users add column user_type varchar(250) default 'valid';

update users set user_type = 'invalid' where username = 'locked_out_user';

insert into users(username,password,user_type) values('test','test123','invalid');

alter table users add column used bool default 0;
