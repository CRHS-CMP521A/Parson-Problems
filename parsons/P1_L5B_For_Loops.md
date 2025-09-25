---
layout: default
title: Parsons Problems [P1_L5B For Loops]
---

# P1 Loops

[Main Page](/Parson-Problems/index.html)

## Table of Contents

- [Length Of Sequence](#loops---length-of-sequence)
- [Sum Of Sequence](#loops---sum-of-sequence)
- [List Of Squares](#loops---list-of-squares)
- [Number Of Even Elements](#loops---number-of-even-elements)
- [Maximum Of Sequence](#loops---maximum-of-sequence)
- [Average Of A Sequence](#loops---average-of-a-sequence)

## Loops - For Range Function

Goal: Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

<div id="Loops_For_Range_Function-sortableTrash" class="sortable-code"></div> 
<div id="Loops_For_Range_Function-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_For_Range_Function-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_For_Range_Function-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = 
    "start = int(input('Start: '))\n" +
    "stop = int(input('Stop: '))\n" +
    "nums = range(start, stop + 1 )\n" +
    "for i in nums :\n" +
    "    print(i)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_For_Range_Function-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops_For_Range_Function-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_For_Range_Function-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - For Range and If

Goal: Given two integers A and B. Print all numbers from A to B inclusively, in increasing order, if A < B, or in decreasing order, if A ≥ B.

<div id="Loops_ForRangeAndIf-sortableTrash" class="sortable-code"></div> 
<div id="Loops_ForRangeAndIf-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_ForRangeAndIf-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_ForRangeAndIf-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "start = int(input('Start: '))\n" +
    "stop = int(input('Stop: '))\n" +
    "if start < stop: #go up\n" +
    "    nums = range(start, stop+1)\n" +
    "else: #go down\n" +
    "    nums = range(start, stop-1, -1 )\n" +
    "for i in nums:\n" +
    "    print(i)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_ForRangeAndIf-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops_ForRangeAndIf-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_ForRangeAndIf-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Sum Numbers from Input

Goal: 10 numbers are given in the input. Read them and print their sum.

<div id="Loops-For-Sum-Numbers-From-Input-sortableTrash" class="sortable-code"></div> 
<div id="Loops-For-Sum-Numbers-From-Input-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops-For-Sum-Numbers-From-Input-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops-For-Sum-Numbers-From-Input-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "total = 0
\n" +
    "for i in range(10): #repeat 10 times
\n" +
    "    num = int(input(&quot;Number: &quot;))
\n" +
    "    total = total + num
\n" +
    "print(&quot;Total: &quot; + str(total))";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops-For-Sum-Numbers-From-Input-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops-For-Sum-Numbers-From-Input-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops-For-Sum-Numbers-From-Input-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Sum N Numbers from Input

Goal: N numbers are given in the input. Read them and print their sum.

The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.

<div id="Loops-For-Sum-N-Numbers-From-Input-sortableTrash" class="sortable-code"></div> 
<div id="Loops-For-Sum-N-Numbers-From-Input-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops-For-Sum-N-Numbers-From-Input-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops-For-Sum-N-Numbers-From-Input-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "N = int(input(&quot;How many numbers? &quot;))
\n" +
    "total = 0
\n" +
    "for i in range(N): #repeat N times
\n" +
    "    num = int(input(&quot;Number: &quot;))
\n" +
    "    total = total + num
\n" +
    "print(&quot;Total: &quot; + str(total))";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops-For-Sum-N-Numbers-From-Input-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops-For-Sum-N-Numbers-From-Input-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops-For-Sum-N-Numbers-From-Input-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - For Count Number of Zeros

Goal: Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.

<div id="Loops-For-Count-Number-of-Zeros-sortableTrash" class="sortable-code"></div> 
<div id="Loops-For-Count-Number-of-Zeros-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops-For-Count-Number-of-Zeros-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops-For-Count-Number-of-Zeros-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "N = int(input(&quot;How many numbers? &quot;))\n" +
    "count = 0\n" +
    "for i in range(N):\n" +
    "    num = int(input(&quot;Number: &quot;))\n" +
    "    if num == 0:\n" +
    "        count += 0\n" +
    "\n" +
    "print(&quot;There were &quot; + str(count) + &quot; ZEROES.&quot;)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops-For-Count-Number-of-Zeros-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops-For-Count-Number-of-Zeros-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops-For-Count-Number-of-Zeros-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - For Sum of Cubes

Goal: For the given integer N calculate the following sum:
1³ + 2³ + ... + N³

<div id="Loops-For-Sum-Of-Cubes-sortableTrash" class="sortable-code"></div> 
<div id="Loops-For-Sum-Of-Cubes-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops-For-Sum-Of-Cubes-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops-For-Sum-Of-Cubes-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "N = int(input())
\n" +
    "total = 0
\n" +
    "for x in range(1, N+1):
\n" +
    "    total = total + x**3
\n" +
    "
\n" +
    "print(total)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops-For-Sum-Of-Cubes-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Loops-For-Sum-Of-Cubes-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops-For-Sum-Of-Cubes-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>
