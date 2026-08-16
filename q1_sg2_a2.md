
Annex C
Code Quality Assessment Worksheet

Section: 9 - Arayat | Score:____________

C# / Name: #1 Angeles, #2 Apostol, #3 Aquino | Date: 8/16/2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


**PseudoCode 1**

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm

**PseudoCode 2**

Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

**Questions with Checklists**
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

The first pseudocode is faster since it only iterates through the list once.

PseudoCode 1

[One] Does the algorithm use one loop or two nested loops?

[No] Does the algorithm repeat work unnecessarily?

[1st] Which algorithm finishes in fewer steps?

PseudoCode 2

[Two] Does the algorithm use one loop or two nested loops?

[Yes] Does the algorithm repeat work unnecessarily?

[1st] Which algorithm finishes in fewer steps?

Checklist to guide your answer:
2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

The first algorithm is easier to understand since it is shorter and only uses one loop.

Checklist to guide your answer:

PseudoCode 1

[Yes] Are variable names meaningful (e.g., max vs. bigger)?

[Simple] Is the logic simple or complicated?

[Yes] Are there fewer lines of code?

PseudoCode 2

[Yes?] Are variable names meaningful (e.g., max vs. bigger)?

[Complicated] Is the logic simple or complicated?

[No] Are there fewer lines of code?

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

The first algorithm would be easier to update since it only uses one loop meaning you can just add extra logic to the code.

Checklist to guide your answer:

PseudoCode 1

[Yes] Is the structure straightforward?

[No] Would adding new steps break the code easily?

[Yes] Is there less chance of errors when updating?

PseudoCode 2

[No] Is the structure straightforward?

[Yes?] Would adding new steps break the code easily?

[No] Is there less chance of errors when updating?

4. Testability
Which algorithm is easier to test with different inputs? Why?

The first one is easier to test with different inputs since it only loops one time and does the same number of steps unlike the 
second algorithm which takes a number and compares it with every other number in the list.

Checklist to guide your answer:

PseudoCode 1

[Yes] Can you test with small lists easily?

[Yes] Does the algorithm have fewer conditions to check?

[Yes] Is the output predictable and clear?

PseudoCode 2

[Yes] Can you test with small lists easily?

[No?] Does the algorithm have fewer conditions to check?

[Yes] Is the output predictable and clear?


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

The algorithm should check if the list is empty, if a number is an int or float, and if there are any strings in the list.

Checklist to guide your answer:

PseudoCode 1

[No] Does the algorithm check if the list is empty?

[No] Does it handle invalid inputs (like letters instead of numbers)?

[No] Does it avoid crashing when inputs are unusual?

PseudoCode 2

[No] Does the algorithm check if the list is empty?

[No] Does it handle invalid inputs (like letters instead of numbers)?

[No] Does it avoid crashing when inputs are unusual?

 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of
finding the highest number? Why? Summarize your answer.

The first algorithm is the better one since it only reads the list once and uses a single loop. It is faster and shorter than the second
algorithm and is also easy to maintain.

<img width="1030" height="600" alt="image" src="https://github.com/user-attachments/assets/0ead340b-bc37-48e5-a76b-f6fcbf994b18" />


