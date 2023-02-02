-- 1 --

select t.`name`,
       t.`surname`,
       g.`name`
  from `teachers` as t
  join `lectures` as l
    on t.`id` = l.`teacher_id`
  join `groups_lectures` as gl
    on gl.`lecture_id` = l.`id`
  join `groups` as g
    on g.`id` = gl.`group_id`;

-- 2 --

  select f.`name` as 'Факультеты',
         f.`financing` as 'Финансирование'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
group by `Финансирование`, `Факультеты`
  having f.`financing` < sum(d.`financing`);

-- 3 --

  select `curators`.`surname` as 'Кураторы',
         group_concat(`groups`.`name` separator ', ') as 'Группы'
    from `curators`
	 join `groups_curators`
      on `curators`.`id` = `groups_curators`.`curator_id`
    join `groups`
      on `groups_curators`.`group_id` = `groups`.`id`
group by `Кураторы`;

-- 4 --

select c.`name`,
       c.`surname`
  from `groups` as g
  join `groups_curators` as gc
    on g.`id` = gc.`group_id`
  join `curators` as c
    on c.`id` = gc.`curator_id`
 where g.`name`='HC-044';

-- 5 --

  select concat(c.`surname`, ' ',  c.`name`) as 'Полное имя',
         group_concat(f.`name` separator ', ') as 'Факультеты'
    from `curators` as c
    join `groups_curators` as gc
      on c.`id`= gc.`curator_id`
    join `groups` as g
      on g.`id`=gc.`group_id`
    join `departments` as d
      on g.`department_id`=d.`id`
    join `faculties` as f
      on f.`id`=d.`faculty_id`
group by `Полное имя`;

-- 6 --

  select d.`name` as 'Каферы',
         group_concat(g.`name` separator ', ') as 'Группы'
    from `groups` as g
    join `departments` as d
      on g.`department_id`=d.`id`
group by `Каферы`;

-- 7 --

  select s.`name` as 'group'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
    join `subjects` as s
      on s.`id`= l.`subject_id`
   where t.`name` = 'Doris' and  t.`surname` = 'Bentley'
group by `group`;

-- 8 --

  select d.`name` as 'Кафедры'
    from `departments` as d
    join `groups` as g
      on d.`id` = g.`department_id`
    join `groups_lectures` as gl
      on gl.`lecture_id` = g.`id`
    join `lectures` as l
      on l.`id` = gl.`lecture_id`
    join `subjects` as s
      on s.`id` = l.`subject_id`
   where s.`name` = 'Cursus A Enim'
group by `Кафедры`;

-- 9 --

  select f.`name` as 'Факультет',
         group_concat(g.`name` separator ', ') as 'Группы'
    from `groups` as g
    join `departments` as d
      on g.`department_id` = d.`id`
    join `faculties` as f
      on d.`faculty_id` = f.`id`
   where f.`name` = 'School of Life Sciences'
group by `Факультет`;

-- 10 --

  select f.`name` as 'Факультеты',
         group_concat(g.`name` separator ', ') as 'Группы'
    from `groups` as g
    join `departments` as d
      on g.`department_id` = d.`id`
    join `faculties` as f
      on f.`id` = d.`faculty_id`
   where g.`year` = 5
group by `Факультеты`;

-- 11 --

select concat(t.`name`, ' ', t.`surname`) as 'Полное имя',
       g.`name` as 'Группа',
       s.`name` as 'Дисциплины'
  from `teachers` as t
  join `lectures` as l
    on t.`id` = l.`teacher_id`
  join `subjects` as s
    on s.`id` = l.`subject_id`
  join `groups_lectures` as gl
    on gl.`lecture_id` = l.`id`
  join `groups` as g
    on gl.`group_id` = g.`id`
 where l.`date` = '2022-10-25';
