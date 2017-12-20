// Rotate Array
// Level: 6kyu
/*
Create a method named "rotate" that returns a given array with the elements inside the array rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.
*/

public class Rotator {

	public Object[] rotate(Object[] data, int n) {
    
    if (n == 0) return data;
    
    if (n < 0) return rotateLeft(data, n*(-1));
    
    return rotateRight(data, n);
  }
  
  private Object[] rotateLeft(Object[] data, int n) {
    
    n = n%data.length;
    
    while(n > 0) {
      Object first = data[0];
      for (int i=0; i<data.length - 1; i++) {
        data[i] = data[i+1];
      }
      
      data[data.length - 1] = first;
      
      n--;
    }
    
    return data;
  }

  private Object[] rotateRight(Object[] data, int n) {
    
    n = n%data.length;
    
    while(n > 0) {
      Object last = data[data.length-1];
      for (int i=data.length - 1; i>0; i--) {
        data[i] = data[i-1];
      }
      
      data[0] = last;
      
      n--;
    }
    
    return data;
  }

}
