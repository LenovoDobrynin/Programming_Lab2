﻿
using System;

namespace Задание_4
{
    class Program
    {
        static int F(int i)
        {
            if (i == 0)
            {
                return 1;
            }
            else
            {
                return i * F(i - 1);
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Введите значение cos(x)");
            int x = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите количество слагаемых (q) ");
            int q = int.Parse(Console.ReadLine());
            if (q == 0)
            {
                while (q == 0)
                {
                    Console.WriteLine("Количество слагаемых (q) не может быть равно нулю!");
                    q = int.Parse(Console.ReadLine());
                }
            }
            double a;
            double cos = 1;
            int b = 2;
            int z = -1;
            int j = 0;
            int i = 2;
            do
            {
                a = (Math.Pow(x, b) / F(i));
                cos += a * z;
                b += 2;
                i += 2;
                z *= -1;
                j++;
            } while (Math.Abs(a) > q);
            Console.WriteLine($"cos(x) =  {cos}");
            Console.WriteLine($"Количество учтенных слагаемых: {j} ");
        }
    }
}