using System;
using System.Collections.Generic;
using System.Text;

namespace StackQueue
{
    public class Queue
    {
        public object[] queueArray;

        public Queue()
        {
            queueArray = new object[0];
        }

        public void popQueue()
        {
            Array.Resize(ref queueArray, queueArray.Length - 1);
        }

        public void pushQueue(object newElement)
        {
            Array.Resize(ref queueArray, queueArray.Length + 1);
            for (int i= queueArray.Length-1; i>0; i--)
            {
                queueArray[i] = queueArray[i-1];
            }
            queueArray[0] = newElement;
        }

        public void clear()
        {
            Array.Resize(ref queueArray, 0);
        }
    }
}
