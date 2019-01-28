Feature: Calculate student's total grade

  Scenario: Getting total grade of the students
    Given There is a teacher "Amy Smith"
    And There is a "psycology" class that she teaches
    And There is a student "Peter Parker" in "psycology" class
    And There is another student "Marty McFly" in "psycology" class
    When Teacher getting quiz 'from json'
    And Teacher assigns quiz to student "Peter Parker"
    And Student "Peter Parker" solves the quiz
    Then Teacher gets the result for student "Peter Parker"
