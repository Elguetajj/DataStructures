using NUnit.Framework;
using SimpleAlgorithms;
using System.Collections;
using System;

namespace Tests
{
    [TestFixture]
    public class GradeLiteralsUnitTests
    {
        [Test, TestCaseSource(typeof(GradesDataProvider), "TestCases")]
        public char GraderTest(int x)
        {
            return GradeLiterals.GradeLiteral(x);
        }

        [Test, TestCaseSource(typeof(GradesDataProvider), "OverHundredExceptionTestCases")]
        public void GradeBelowZeroTest(int x)
        {
            var ex = Assert.Throws<ArgumentOutOfRangeException>(() => GradeLiterals.GradeLiteral(x));
            Assert.That(ex.Message, Is.EqualTo($@"Grade must be between 0 and 100.
Parameter name: x"));
        }
        [Test, TestCaseSource(typeof(GradesDataProvider), "UnderZeroExceptionTestCases")]
        public void GradeOverHundredTest(int x)
        {
            var ex = Assert.Throws<ArgumentOutOfRangeException>(() => GradeLiterals.GradeLiteral(x));
            Assert.That(ex.Message, Is.EqualTo($@"Grade must be between 0 and 100.
Parameter name: x"));
        }
    }

    public class GradesDataProvider
    {
        public static IEnumerable TestCases
        {
            get
            {
                for (int i = 0; i <= 40; i++)
                {
                    yield return new TestCaseData(i).Returns('D');
                }
                for (int i = 41; i <= 50; i++)
                {
                    yield return new TestCaseData(i).Returns('C');
                }
                for (int i = 51; i <= 60; i++)
                {
                    yield return new TestCaseData(i).Returns('B');
                }
                for (int i = 61; i <= 75; i++)
                {
                    yield return new TestCaseData(i).Returns('A');
                }
                for (int i = 76; i <= 100; i++)
                {
                    yield return new TestCaseData(i).Returns('S');
                }
            }
        }

        public static IEnumerable UnderZeroExceptionTestCases
        {
            get
            {
                for (int i = -10; i < 0; i++)
                {
                    yield return new TestCaseData(i);
                }
            }
        }

        public static IEnumerable OverHundredExceptionTestCases
        {
            get
            {
                for (int i = 101; i <= 111; i++)
                {
                    yield return new TestCaseData(i);
                }
            }
        }
    }
}