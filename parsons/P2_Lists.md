---
layout: default
title: Parsons Problems [P2 Lists]
---

# P2 Lists

[Main Page](/Parson-Problems/index.html)

## Table of Contents

- [Lists - Creating a Sorted List of Colours](#lists---creating-a-sorted-list-of-colours)
- [Lists - Printing Numbers Which Are Even](#lists---printing-numbers-which-are-even)
- [Lists - Printing Part Of A Water Depth List](#lists---printing-part-of-a-water-depth-list)

## Lists - Creating a Sorted List of Colours

Get the user to input colours and store this in a list. Print out the sorted colours, one colour per line.

<div id="Lists_CreatingASortedListOfColours-sortableTrash" class="sortable-code"></div> 
<div id="Lists_CreatingASortedListOfColours-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists_CreatingASortedListOfColours-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists_CreatingASortedListOfColours-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Lists_CreatingASortedListOfColours-sortable",
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
  $("#Lists_CreatingASortedListOfColours-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists_CreatingASortedListOfColours-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Lists - Printing Numbers Which Are Even

Collect User Numbers. Then output all the even ones.

<div id="Lists_PrintingNumbersWhichAreEven-sortableTrash" class="sortable-code"></div> 
<div id="Lists_PrintingNumbersWhichAreEven-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists_PrintingNumbersWhichAreEven-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists_PrintingNumbersWhichAreEven-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Lists_PrintingNumbersWhichAreEven-sortable",
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
  $("#Lists_PrintingNumbersWhichAreEven-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists_PrintingNumbersWhichAreEven-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

## Lists - Printing Part Of A Water Depth List

From Daily Water Level Data, print each day until level exceeds 2.

<div id="Lists_PrintingPartOfAWaterDepthList-sortableTrash" class="sortable-code"></div> 
<div id="Lists_PrintingPartOfAWaterDepthList-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Lists_PrintingPartOfAWaterDepthList-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Lists_PrintingPartOfAWaterDepthList-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Lists_PrintingPartOfAWaterDepthList-sortable",
    "max_wrong_lines": 10,
    "grader": ParsonsWidget._graders.LineBasedGrader,
    "exec_limit": 2500,
    "can_indent": true,
    "x_indent": 50,
    "lang": "en",
    "show_feedback": true
    "trashId": "Lists_PrintingPartOfAWaterDepthList-sortableTrash"
  });
  parsonsPuzzle.init(initial);
  parsonsPuzzle.shuffleLines();
  $("#Lists_PrintingPartOfAWaterDepthList-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Lists_PrintingPartOfAWaterDepthList-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>
