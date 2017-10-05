// Convert a linked list to a string
// Level : 7kyu

public class Kata {

  public static String stringify(Node list) {
    String s = "";
    while(list != null) {
      s = s + String.valueOf(list.getData());
      s = s + " -> ";
      list = list.getNext();
    }
    s =s + "null";
    return s;
  }

}
