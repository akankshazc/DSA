/**
 * Stack implementation in Java.
 * Provides push, pop, size, isEmpty, isFull, and printStack operations.
 */
public class Stack {
  private int[] arr;
  private int top;
  private int capacity;

  /**
   * Creates a stack with the given size.
   * size = the capacity of the stack
   */
  public Stack(int size) {
    arr = new int[size];
    capacity = size;
    top = -1;
  }

  /**
   * Adds an element to the stack.
   * x = the element to add
   */
  public void push(int x) {
    if (isFull()) {
      System.out.println("Overflow\nProgram Terminated\n");
      System.exit(1);
    }
    System.out.println("Inserting " + x);
    arr[++top] = x;
  }

  /**
   * Removes and returns the top element from the stack.
   * return the popped element
   */
  public int pop() {
    if (isEmpty()) {
      System.out.println("STACK EMPTY");
      System.exit(1);
    }
    return arr[top--];
  }

  /**
   * Returns the current size of the stack.
   * return the number of elements in the stack
   */
  public int size() {
    return top + 1;
  }

  /**
   * Checks if the stack is empty.
   * return true if empty, false otherwise
   */
  public boolean isEmpty() {
    return top == -1;
  }

  /**
   * Checks if the stack is full.
   * return true if full, false otherwise
   */
  public boolean isFull() {
    return top == capacity - 1;
  }

  /**
   * Prints all elements in the stack.
   */
  public void printStack() {
    for (int i = 0; i <= top; i++) {
      System.out.println(arr[i]);
    }
  }

  /**
   * Main method to demonstrate stack operations.
   * args = command-line arguments
   */
  public static void main(String[] args) {
    Stack stack = new Stack(5);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.pop();
    System.out.println("\nAfter popping out");
    stack.printStack();
  }
}