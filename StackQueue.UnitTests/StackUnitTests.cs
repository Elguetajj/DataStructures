using NUnit.Framework;
using StackQueue;
using System.Collections;

namespace Tests
{
    public class StackUnitTests
    {
        [SetUp]
        public void Setup()
        {
            var stack = new StackQueue.Stack();
        }

        [Test]
        public void Test1()
        {

        }
    }
    
    public class StackUnitTestsDP
    {
        public IEnumerable TestCases
        {
            get
            {
                yield return new TestCaseData()
            }
        }

    }
}