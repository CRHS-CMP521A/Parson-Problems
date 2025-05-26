---
layout: default
title: Parsons Problems [P1 Loops]
---

# P1 Loops
[Main Page](/Parson-Problems/index.html)

## Table of Contents

- [Loops_LengthOfSequence](#loops---length-of-sequence)
- [Loops_SumOfSequence](#loops---sum-of-sequence)
- [Loops_ListOfSquares](#loops---list-of-squares)
- [Loops_NumberOfEvenElements](#loops---number-of-even-elements)
- [Loops - Maximum of a Sequence](#loops---maximum-of-a-sequence)
- [Loops_AverageOfASequence](#loops---average-of-a-sequence)

## Loops_LengthOfSequence

Goal: Count user integers. Stop with 0.

<div id="Loops_LengthOfSequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops_LengthOfSequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_LengthOfSequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_LengthOfSequence-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "num = int(input(“First number? 0 to stop.”)) #get first input\n" +
    "count = 0\n" +
    "while num != 0:\n" +
    "  count += 1\n" +
    "  num = int(input(“Next number? 0 to stop.”)) #get next input\n" +
    "print(count)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_LengthOfSequence-sortable",
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
  $("#Loops_LengthOfSequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_LengthOfSequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops_SumOfSequence

Goal: Sum user integers. Stop with 0.

<div id="Loops_SumOfSequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops_SumOfSequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_SumOfSequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_SumOfSequence-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "num = int(input(“First number? 0 to stop.”)) #get first input\n" +
    "sum = 0\n" +
    "while num != 0:\n" +
    "  sum = sum + num\n" +
    "  num = int(input(“Next number? 0 to stop.”)) #get next input\n" +
    "print(sum)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_SumOfSequence-sortable",
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
  $("#Loops_SumOfSequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_SumOfSequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops_ListOfSquares

Goal: print all squares up to and including N

<div id="Loops_ListOfSquares-sortableTrash" class="sortable-code"></div> 
<div id="Loops_ListOfSquares-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_ListOfSquares-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_ListOfSquares-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "N = int(input()) \n" +
    "num = 1\n" +
    "while num**2 &lt;= N:\n" +
    "    print(num**2)\n" +
    "    num += 1";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_ListOfSquares-sortable",
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
  $("#Loops_ListOfSquares-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_ListOfSquares-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops_NumberOfEvenElements

Goal: Count number of even inputs. Stop with 0.

<div id="Loops_NumberOfEvenElements-sortableTrash" class="sortable-code"></div> 
<div id="Loops_NumberOfEvenElements-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_NumberOfEvenElements-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_NumberOfEvenElements-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "num = int(input(“First number? 0 to stop.”)) #get first input\n" +
    "countEven = 0\n" +
    "while num != 0:\n" +
    "    if num % 2 == 0: #number is even\n" +
    "        countEven +=1\n" +
    "    num = int(input(“Next number? 0 to stop.”)) #get next input\n" +
    "print(countEven)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_NumberOfEvenElements-sortable",
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
  $("#Loops_NumberOfEvenElements-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_NumberOfEvenElements-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Maximum of a Sequence

Goal: Find maximum of user’s integers. Stop with 0.

<div id="Loops_MaximumOfSequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops_MaximumOfSequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_MaximumOfSequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_MaximumOfSequence-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "num = int(input(“First number? 0 to stop.”)) #get first input\n" +
    "maxNum = 0\n" +
    "while num != 0:\n" +
    "    if num &gt; maxNum: #if user enters number great max\n" +
    "        maxNum = num\n" +
    "    num = int(input(“Next number? 0 to stop.”)) #get next input\n" +
    "print(maxNum)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_MaximumOfSequence-sortable",
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
  $("#Loops_MaximumOfSequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_MaximumOfSequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops_AverageOfASequence

Goal: Get user inputs and determine the average.

<div id="Loops_AverageOfASequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops_AverageOfASequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_AverageOfASequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_AverageOfASequence-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "num = int(input(“First number? 0 to stop.”)) #get first input\n" +
    "count = 0\n" +
    "sum = 0\n" +
    "while num != 0:\n" +
    "    count += 1\n" +
    "    sum = sum + num\n" +
    "        num = int(input(“Next number? 0 to stop.”)) #get next input\n" +
    "average = sum / count\n" +
    "print(average)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops_AverageOfASequence-sortable",
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
  $("#Loops_AverageOfASequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_AverageOfASequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>


