CREATE table Students
(
    StudentID   INT,
    StudentName VARCHAR(10)
);

CREATE table Classes
(
    ClassID   INT,
    ClassName VARCHAR(10)
);

CREATE table StudentClass
(
    StudentID INT,
    ClassID   INT
);

INSERT INTO Students (StudentID, StudentName)
VALUES (1, 'John'),
       (2, 'Matt'),
       (3, 'James');

INSERT INTO Classes (ClassID, ClassName)
VALUES (1, 'Maths'),
       (2, 'Arts'),
       (3, 'History');

INSERT INTO StudentClass (StudentID, ClassID)
VALUES (1, 1),
       (1, 2),
       (3, 1),
       (3, 2),
       (3, 3);

SELECT *
FROM Students;

SELECT *
FROM Classes;

SELECT *
FROM StudentClass;

-- What will be the possible join if we want to retrieve
-- all the students who have signed up for the classes in the summer
SELECT st.StudentName, cl.ClassName
FROM Students st
         INNER JOIN StudentClass sc ON st.studentid = sc.studentid
         INNER JOIN Classes cl ON sc.classid = cl.classid;

SELECT st.StudentName
FROM Students st
         LEFT JOIN StudentClass sc ON st.studentid = sc.studentid
WHERE sc.classid IS NULL;

DROP TABLE StudentClass;
DROP TABLE Students;
DROP TABLE Classes;
