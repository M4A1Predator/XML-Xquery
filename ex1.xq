(: 
4. list all student elements; do not use
5. find the title of the project that has the highest number of advisors
6. What is the length of the longest elemant-only patch
:)

(:
for $r in doc("project.xml")/projectList/project
return if ($r/members)
then <result>{$r/members/student/self::element()}</result>
else <result>{$r/student/self::element()}</result>
:)

let $a := 0
for $r in doc("project.xml")/projectList/project
return if ((count($r/advisor) > $a))
then let $a := (count($r/advisor)
else <result></result>
