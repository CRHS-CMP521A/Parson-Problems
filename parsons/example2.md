---
layout: default
title: Example 2
---

Goal: Count user integers. Stop with 0.

<div id="Loops_Average_of_Sequence-sortableTrash" class="sortable-code"></div> 
<div id="Loops_Average_of_Sequence-sortable" class="sortable-code"></div> 
<div style="clear:both;"></div> 
<p> 
    <input id="Loops_Average_of_Sequence-feedbackLink" value="Get Feedback" type="button" /> 
    <input id="Loops_Average_of_Sequence-newInstanceLink" value="Reset Problem" type="button" /> 
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
    "sortableId": "Loops_Average_of_Sequence-sortable",
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
  $("#Loops_Average_of_Sequence-newInstanceLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.shuffleLines(); 
  }); 
  $("#Loops_Average_of_Sequence-feedbackLink").click(function(event){ 
      event.preventDefault(); 
      parsonsPuzzle.getFeedback(); 
  }); 
})(); 
</script>

[Previous](./example1.html)
