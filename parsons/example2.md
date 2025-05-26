---
layout: default
title: Example 2
---
Goal: Count user integers. Stop with 0.

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

[Previous](./example1.html)
