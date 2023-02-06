-- 1 --

select count(distinct t.`id`) as 'Amount'
  from `departments` as d
  join `groups` as g
    on d.`id` = g.`department_id`
  join `groups_lectures` as gl
    on gl.`group_id` = g.`id`
  join `lectures` as l
    on l.`id` = gl.`lecture_id`
  join `teachers` as t
    on t.`id` = l.`teacher_id`
 where d.`name` = 'Infochemistry';

-- 2 --

select count(distinct l.`id`) as 'Amount'
  from `teachers` as t
  join `lectures` as l
    on t.`id` = l.`teacher_id`
 where concat_ws (' ', t.`name`, t.`surname`) = 'Christopher Fulton';

-- 3 --

select count(distinct l.`id`) as 'Amount'
  from `lectures` as l
  join `groups_lectures` as gl
    on l.`id` = gl.`lecture_id`
  join `groups` as g
    on g.`id` = gl.`group_id`
  join `departments` as d
    on d.`id` = g.`department_id`
 where d.`building` = 4 and l.`date` = '2022-09-15';

-- 4 --

  select d.`building` as 'Building',
         count(distinct g.`id`) as 'Amount'
    from `lectures` as l
    join `groups_lectures` as gl
      on l.`id` = gl.`lecture_id`
    join `groups` as g
      on g.`id` = gl.`group_id`
    join `departments` as d
      on d.`id` = g.`department_id`
   where g.`year` = '6'
group by `Building`;

-- 5 --

select count(distinct s.`id`) as 'Amount'
  from `students` as s
  join `groups_students` as gs
    on s.`id` = gs.`student_id`
  join `groups` as g
    on g.`id` = gs.`group_id`
  join `groups_lectures` as gl
    on gl.`group_id` = g.`id`
  join `lectures` as l
    on l.`id` = gl.`lecture_id`
  join `teachers` as t
    on t.`id` = l.`teacher_id`
 where  t.`name` = 'Trevor' and t.`surname` =  'Wood';

-- 6 --

select round(avg(t.`salary`), 1) as 'Average salary'
  from `faculties` as f
  join `departments` as d
    on f.`id` = d.`faculty_id`
  join `groups` as g
    on g.`department_id` = d.`id`
  join `groups_lectures` as gl
    on gl.`group_id` = g.`id`
  join `lectures` as l
    on l.`id` = gl.`lecture_id`
  join `teachers` as t
    on t.`id` = l.`teacher_id`
 where f.`name` = 'School of Physics and Engineering';

-- 7 --

select MIN(amount.`cs`) as 'Min',
       MAX(amount.`cs`) as 'Max'
  from (select `group_id` as 'gi',
	           count(`student_id`) as 'cs'
		  from `groups_students`
      group by `gi`) as amount;

-- 8 --

select avg (d.`financing`) as 'Average'
      from `departments` as d;

-- 9 --

  select concat_ws(' ', t.`name`, t.`surname`) as 'Full name',
		 count(distinct s.`id`) as 'Amount'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
    join `subjects` as s
      on s.`id` = l.`subject_id`
group by `Full name`;

-- 10 --

  select l.`date` as 'Date',
         count(l.`id`) as 'Amount'
    from `lectures` as l
group by `Date`
order by l.`date`;

-- 11 --

   select d.`building` as 'Building',
         count(f.`id`) as 'Amount'
    from `departments` as d
    join `faculties` as f
      on f.`id` = d.`faculty_id`
group by d.`building`;

-- 12 --

  select f.`name` as 'Faculties',
         count(distinct s.`id`) as 'Amount'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
    join `groups` as g
      on g.`department_id` = d.`id`
    join `groups_lectures` as gl
      on gl.`group_id` = g.`id`
    join `lectures` as l
      on l.`id` = gl.`lecture_id`
    join `subjects` as s
      on l.`subject_id` = s.`id`
group by `Faculties`;

-- 13 --

  select concat(t.`name`, ' ', t.`surname`, ' - ', d. `building`) as 'Teacher/Building',
         count(*) as 'Lectures'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
    join `groups_lectures` as gl
      on l.`id` = gl.`lecture_id`
    join `groups` as g
      on gl.`group_id` = g.`id`
    join `departments` as d
      on g.`department_id` = d.`id`
group by `Teacher/Building`
order by `Teacher/Building`;
