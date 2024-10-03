INSERT OR IGNORE INTO users (username)
VALUES
    ('standard_user'),
    ('locked_out_user'),
    ('problem_user'),
    ('performance_glitch_user'),
    ('error_user'),
    ('visual_user');
select * from users;