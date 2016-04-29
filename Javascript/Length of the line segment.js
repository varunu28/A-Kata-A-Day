//Length of the line segment
//Level: 7kyu
/*
<<<<<<< HEAD
Problem Description: Find the length between 2 co-ordinates. The co-ordinates are made of integers between -20 and 20 
and will be given in the form of a 2D array:
=======
Problem Description: Find the length between 2 co-ordinates. The co-ordinates are made of integers between -20 and 20 and will be given 
in the form of a 2D array:
>>>>>>> a38376b4697a5f276263a59173311fdbddc1945b

(0,0) and (5,-7) would be [ [ 0 , 0 ] , [ 5, -7 ] ]

The function must return the answer rounded to 2 decimal places in the form of a string.

lengthOfLine([ [ 0 , 0 ] , [ 5, -7 ] ]); => "8.60"
If the 2 given co-ordinates are the same, the returned length should be "0.00"
*/
<<<<<<< HEAD

=======
>>>>>>> a38376b4697a5f276263a59173311fdbddc1945b
function lengthOfLine(array){
  var x1=array[0][0];
  var y1=array[0][1];
  var x2=array[1][0];
  var y2=array[1][1];
  
  var ans = Math.sqrt(Math.pow(y2-y1,2)+Math.pow(x2-x1,2));
  ans = ans.toString();
  var ans_round=parseFloat(ans).toFixed(2);
  
  return ans_round;
}
