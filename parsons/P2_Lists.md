---
layout: default
title: Parsons Problems [P2 Lists]
---

# P2 Lists

## Table of Contents

- [Lists - Creating a Sorted List of Colours](#lists---creating-a-sorted-list-of-colours)
- [Lists - Printing Numbers Which are Even](#lists---printing-numbers-which-are-even)
- [Lists - Printing part of a Water Depth List](#lists---printing-part-of-a-water-depth-list)


## Lists - Creating a Sorted List of Colours

<div id="Lists -  Creating a Sorted List of Colours-sortableTrash" class="sortable-code"></div> 
<div id="Lists -  Creating a Sorted List of Colours-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists -  Creating a Sorted List of Colours-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists -  Creating a Sorted List of Colours-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "myList = []\n" +
    "colour = input(&quot;First colour? D for done. &quot;)\n" +
    "while colour != &quot;D&quot;:\n" +
    "    myList.append(colour)\n" +
    "    colour = input(&quot;Next colour? D for done. &quot;)\n" +
    "myList.sort()\n" +
    "for el in myList:\n" +
    "    print(el)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Lists -  Creating a Sorted List of Colours-sortable",
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
  $("#Lists -  Creating a Sorted List of Colours-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists -  Creating a Sorted List of Colours-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Lists - Printing Numbers Which are Even

Collect User Numbers. Then output all the even ones.

<div id="Lists - Printing Numbers Which are Even-sortableTrash" class="sortable-code"></div> 
<div id="Lists - Printing Numbers Which are Even-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists - Printing Numbers Which are Even-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists - Printing Numbers Which are Even-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "myList = []\n" +
    "num = int(input(&quot;Enter first number. 0 to stop.&quot;))\n" +
    "while num != 0:\n" +
    "    myList.append(num)\n" +
    "    num = int(input(&quot;Enter next number. 0 to stop.&quot;))\n" +
    "for num in myList:\n" +
    "    if num % 2 == 0:\n" +
    "        print(num)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Lists - Printing Numbers Which are Even-sortable",
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
  $("#Lists - Printing Numbers Which are Even-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists - Printing Numbers Which are Even-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Lists - Printing part of a Water Depth List

From Daily Water Level Data, print each day until level exceeds 2

<div id="Lists - Printing part of a Water Depth List-sortableTrash" class="sortable-code"></div> 
<div id="Lists - Printing part of a Water Depth List-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists - Printing part of a Water Depth List-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists - Printing part of a Water Depth List-newInstanceLink" value="Reset Problem" type="button" /> 
</p> 
<script type="text/javascript"> 
(function(){
  var initial = "waterDepth = [1.2, 0.8, 1.0, 1.5, 1.9, 2.1, 2.5, 2.7]\n" +
    "for i in range(len(waterDepth)):\n" +
    "    curDepth = waterDepth[i]\n" +
    "    if curDepth &gt; 2:\n" +
    "        break\n" +
    "    print(i, curDepth)";
  var parsonsPuzzle = new ParsonsWidget({
    "sortableId": "Lists - Printing part of a Water Depth List-sortable",
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
  $("#Lists - Printing part of a Water Depth List-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists - Printing part of a Water Depth List-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>


[Main Page](/index.markdown)