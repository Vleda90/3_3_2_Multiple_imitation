Create a class hierarchy:
Person class - provides the basic attributes for describing a person: first name, last name, gender, date of birth.
Student class - which extends Person with the major attribute and the to_learn() method. Think about how the __init__() method will change.
Teacher class, which extends Person with the to_teach() method

UPD. Look at the code of the previous task: refactor it to implement the functionality by multiple inheritance of the required functionality using mixin classes. 
Add not only the functionality (student, senior student, teacher, dean), but also the remuneration (assuming that we have two systems of relations - payment of a scholarship and payment of a salary). 
The level of salary (or scholarship) is an individual parameter of each employee, fix the difference only with a description (“scholarship in the amount of XXX”, “salary in the amount of XXX”)
