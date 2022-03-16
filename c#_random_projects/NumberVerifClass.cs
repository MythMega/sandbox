using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JMUtils
{
    internal class NumberVerifClass
    {
        public bool isNotTooBig(int aVerif)
        {
            if (aVerif > 2147483647)
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        public List<int> getDivisor(int monNombre)
        {
            int divisors = 0;
            List<int> list_divisors = new List<int>();
            int maxACheck = monNombre;
            for (int i = 2; i < maxACheck; i++)
            {
                if (monNombre % i == 0)
                {
                    divisors = i;
                    list_divisors.Add(divisors);
                }
            }
            return list_divisors;

        }

        public void isPrime(int myNumber)
        {
            bool is_prime = true;
            int divisor = 0;
            for (int i = 2; i < myNumber; i++)
            {
                if (myNumber % i == 0)
                {
                    is_prime = false;
                    divisor = i;
                    break;
                }
            }
            if (is_prime == true) { Console.WriteLine("Le nombre " + myNumber.ToString() + " est premier"); }

            else { Console.WriteLine("Le nombre " + myNumber.ToString() + " n'est pas premier, il est divisible par " + divisor.ToString()); }
        }

        public bool isPrimeBool(int myNumber)
        {
            bool is_prime = true;
            int divisor = 0;
            for (int i = 2; i < myNumber; i++)
            {
                if (myNumber % i == 0)
                {
                    is_prime = false;
                    divisor = i;
                    break;
                }
            }
            if (is_prime == true) { return true; }

            else { return false; }
        }

        public bool isPair(int myTest)
        {
            if(myTest%2==0) {return true;}
            else { return false; }
        }

        public bool isPositive(int myTest)
        {
            if(myTest>-1) { return true; } else { return false; }
        }

        public double toPositive(double myNumber) {
            return Math.Sqrt(myNumber*myNumber);
        }

        public bool isPerfect(int myTest)
        {
            List<int> myDivisorList = new List<int>();
            int currentCalcul = 0;
            for(int i=1; i < myTest; i++)
            {
                if (myTest%i==0)
                {
                    myDivisorList.Add(i);
                }
            }
            for(int j = 1; j < myDivisorList.Count; j++)
            {
                currentCalcul += myDivisorList[j];
            }
            if(currentCalcul == myTest) { return true; }
            else { return false; }

        }
    }
}
