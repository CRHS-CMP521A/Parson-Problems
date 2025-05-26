---
layout: default
title: Parsons Problems [P1 Loops]
---

# P1 Loops

## Table of Contents

- [Loops - Length of Sequence](#loops---length-of-sequence)
- [Loops - Sum of Sequence](#loops---sum-of-sequence)
- [Loops - List of Squares](#loops---list-of-squares)
- [Loops - Number of Even Elements](#loops---number-of-even-elements)
- [Loops - Maximum of a Sequence](#loops---maximum-of-a-sequence)
- [Loops - Average of a Sequence](#loops---average-of-a-sequence)


## Loops - Length of Sequence 

Goal:  Count user integers. Stop with 0.

<div id="Loops - Length of Sequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops - Length of Sequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - Length of Sequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - Length of Sequence-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops - Length of Sequence-sortable",
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
  $("#Loops - Length of Sequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - Length of Sequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>


## Loops - Sum of Sequence

Goal:  Sum user integers. Stop with 0.

<div id="Loops - Sum of Sequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops - Sum of Sequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - Sum of Sequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - Sum of Sequence-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops - Sum of Sequence-sortable",
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
  $("#Loops - Sum of Sequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - Sum of Sequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - List of Squares

Goal: print all squares up to and including N

<div id="Loops - List of Squares-sortableTrash" class="sortable-code"></div> 
<div id="Loops - List of Squares-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - List of Squares-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - List of Squares-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "N = int(input()) \n" +
    "num = 1\n" +
    "while num**2 &lt;= N:\n" +
    "    print(num**2)\n" +
    "    num += 1";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Loops - List of Squares-sortable",
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
  $("#Loops - List of Squares-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - List of Squares-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Number of Even Elements

Goal:  Count number of even inputs. Stop with 0.

<div id="Loops - Number of Even Elements-sortableTrash" class="sortable-code"></div> 
<div id="Loops - Number of Even Elements-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - Number of Even Elements-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - Number of Even Elements-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops - Number of Even Elements-sortable",
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
  $("#Loops - Number of Even Elements-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - Number of Even Elements-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Maximum of a Sequence

Goal:  Find maximum of user’s integers. Stop with 0.

<div id="Loops - Maximum of Sequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops - Maximum of Sequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - Maximum of Sequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - Maximum of Sequence-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops - Maximum of Sequence-sortable",
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
  $("#Loops - Maximum of Sequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - Maximum of Sequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Loops - Average of a Sequence

Goal: Get user inputs and determine the average.

<div id="Loops - Average of a Sequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops - Average of a Sequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops - Average of a Sequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops - Average of a Sequence-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops - Average of a Sequence-sortable",
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
  $("#Loops - Average of a Sequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops - Average of a Sequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

[Main Page](/index.markdown)
