-- 1 --

  select d.`building` as 'Building'
    from `departments` as d
group by `Building`
  having sum(d.`financing`) > 12000000
order by `Building`;

-- 2 --

-- Еще думаю...

-- 3 --

  select g.`name` as 'Group',
         avg(s.`rating`) as 'Student rating'
    from `groups` as g
    join `groups_students` as gs
      on g.`id` = gs.`group_id`
    join `students` as s
      on s.`id` = gs.`student_id`
group by `Group`
  having avg(s.`rating`) > (select avg(s.`rating`)
                              from `groups` as g
                              join `groups_students` as gs
                                on g.`id` = gs.`group_id`
                              join `students` as s
                                on s.`id` = gs.`student_id`
                             where g.`name` = 'ZQ-002');

-- 4 --

select concat_ws(' ', t.`name`, t.`surname`) as 'Full name'
from `teachers` as t
where t.`salary` > (select avg(t.`salary`)
                      from `teachers` as t
                     where t.`is_professor` = 1);

-- 5 --

  select g.`name` as 'Name group',
         count(gc.`curator_id`) as 'Amount curators'
    from `curators` as c
    join `groups_curators` as gc
      on c.`id` = gc.`curator_id`
    join `groups` as g
      on g.`id` = gc.`group_id`
group by `Name group`
  having count(gc.`curator_id`) > 1;

-- 6 --
-- Вывел названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) меньше, чем минимальный средний рейтинг групп 6-го курса.

  select g.`name` as 'Group'
	  from `groups` as g
    join `groups_students` as gs
      on g.`id` = gs.`group_id`
    join `students` as s
      on s.`id` = gs.`student_id`
group by `Group`
  having avg(s.`rating`) < (select MIN(subq.`Rating`)
                                      from (select g.`name` as 'Group',
                                           avg(s.`rating`) as 'Rating'
                                      from `groups` as g
                                      join `groups_students` as gs
                                        on g.`id` = gs.`group_id`
                                      join `students` as s
                                        on s.`id` = gs.`student_id`
                                     where g.`year` = 6
                                  group by `Group`) as subq);

-- 7 --

  select f.`name` as 'Faculty name'
    from `departments` as d
    join `faculties` as f
      on d.`faculty_id` = f.`id`
group by `Faculty name`
  having sum(d.`financing`) > (select subq.`department`
                                 from (select f.`name` as 'faculty',
                                              sum(d.`financing`) as 'department'
                                         from `departments` as d
                                         join `faculties` as f
                                           on d.`faculty_id` = f.`id`
                                     group by `Faculty`
                                       having f.`name` = 'School of Life Sciences') as subq);

-- 8 --

-- Еще думаю...

-- 9 --

  select s.`name` as 'Subject name',
         sum(l.`date`) as 'amount'
    from `subjects` as s
    join `lectures` as l
      on s.`id` = l.`subject_id`
group by `Subject name`
order by `amount`
   limit 1;

-- 10 --

select count(distinct st.`id`) as 'Amount of Students',
       count(distinct s.`id`) as 'Amount of subjects'
  from `departments` as d
  join `groups` as g
    on g.`department_id` = d.`id`
  join `groups_lectures` as gl
    on gl.`group_id` = g.`id`
  join `lectures` as l
    on l.`id` = gl.`lecture_id`
  join `subjects` as s
    on s.`id` = l.`subject_id`
  join `groups_students` as gs
    on gs.`group_id` = g.`id`
  join `students` as st
    on st.`id` = gs.`student_id`
 where d.`name` = 'Biotechnologies'
