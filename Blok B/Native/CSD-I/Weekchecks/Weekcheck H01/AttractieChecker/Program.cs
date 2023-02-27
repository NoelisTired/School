namespace Attracties
{
    public class Program
    {
        public static void accessDenied()
        {
            Console.WriteLine("Je mag niet in de attractie.");
            Environment.Exit(0);
        }

        public static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine(
                    "Attracties  ||  KeuzeMenu:\n" +
                    "1.Debug Hero\n" +
                    "2.Bugs of Horror\n" +
                    "3.Speedy XL\n" +
                    "4.Turbo Turn 2000"
                    );

                Console.WriteLine("Kies een attractie nummer: "); // Choice of choice menu
                string choiceNumberMenu = Console.ReadLine();
                int choiceNumber = int.Parse(choiceNumberMenu);

                if (choiceNumber == 1 || choiceNumber == 2 || choiceNumber == 4)
                {
                    Console.WriteLine("Wat is je leeftijd?: ");
                    string ageString = Console.ReadLine();
                    int age = int.Parse(ageString);

                    if (choiceNumber == 1)
                    {
                        if (age < 12)
                        {
                            accessDenied();
                        }

                        Console.WriteLine("Wat is je lengte in cm?: ");
                        string lengthString = Console.ReadLine();
                        int length = int.Parse(lengthString);

                        if (length < 120)
                        {
                            accessDenied();
                        }
                    }
                    else if (choiceNumber == 2)
                    {
                        if (age < 16)
                        {
                            accessDenied();
                        }

                        Console.WriteLine("Wat is je gewicht in kg?: ");
                        string weightStringA = Console.ReadLine();
                        int weight = int.Parse(weightStringA);

                        if (weight > 95)
                        {
                            accessDenied();
                        }
                    }
                    else if (choiceNumber == 4)
                    {
                        if (age < 12)
                        {
                            Console.WriteLine("Wat is je lengte in cm?: ");
                            string lengthString = Console.ReadLine();
                            int length = int.Parse(lengthString);

                            if (length < 100)
                            {
                                accessDenied();

                            }
                        }

                        Console.WriteLine("Wat is je gewicht in kg?: ");
                        string weightStringB = Console.ReadLine();
                        int weight = int.Parse(weightStringB);

                        if (weight > 120)
                        {
                            accessDenied();
                        }
                    }
                }
                else if (choiceNumber == 3)
                {
                    Console.WriteLine("Wat is je lengte in cm?: ");
                    string lengthString = Console.ReadLine();
                    int length = int.Parse(lengthString);

                    if (length < 90)
                    {
                        accessDenied();
                    }

                    Console.WriteLine("Wat is je gewicht in kg?: ");
                    string weightStringC = Console.ReadLine();
                    int weight = int.Parse(weightStringC);

                    if (weight > 120)
                    {
                        accessDenied();
                    }
                }

                Console.WriteLine("Je mag in de attractie!");
                Console.WriteLine("Wil je het programma sluiten? (y/n): ");
                string weightStringD = Console.ReadLine().ToLower();
                if (weightStringD == "y")
                {
                    Environment.Exit(0);
                }
            }
        }
    }
}





