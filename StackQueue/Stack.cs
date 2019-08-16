using System;
using System.Collections.Generic;
using System.Text;

namespace StackQueue
{
    public class Stack
    {
        public object[] stackArray;


        public Stack()
        {
            stackArray = new object[0];
        }
       
        public void pushStack(Object newElement)
        {
            Array.Resize(ref stackArray, stackArray.Length + 1);
            stackArray[stackArray.Length-1]= newElement;
        }

        public void popStack()
        {
            Array.Resize(ref stackArray, stackArray.Length - 1);
        }

        public void clear()
        {
            Array.Resize(ref stackArray, 0);
        }
    }
}
