using AbboChecker;
using System.Runtime.InteropServices;

var abonnementen = AbonnementenLijst.HaalAbonnementenOp();

while(true)
{
    Console.Clear();
    Console.WriteLine("1. Toon de gemiddelde leeftijd van alle abonnementhouders"+
                      "\n2. Toon alle Regulier abonnementen die nog niet betaald zijn"+
                      "\n3. Toon aantal abonnementen van medewerkers met het type Abbo XL die nog niet zijn betaald."+
                      "\n4. Verleng alle abonnementen die verlopen zijn en verhoog de prijs met X%"+
                      "\n5. Verleng alle abonnementen die van een 65+'er of medewerker zijn en geef X% korting." +
                      "\n0. Sluit het programma");
    
    Console.WriteLine("Kies een optie: ");
    string optionConsole = Console.ReadLine();
    int option = int.Parse(optionConsole);

    if (option == 0)
    {
        Environment.Exit(0);
    }
    else if (option == 1)
    {
        int totalAge = 0;
        int amountOfPeople = 0;
        foreach (var item in abonnementen)
        {
            totalAge += item.Leeftijd;
            amountOfPeople += 1;
        }
        Console.WriteLine("Gemiddelde leeftijd van alle abonnementhouders: " + totalAge / amountOfPeople + "\nEnter om door te gaan...");
        Console.ReadLine();
    }
    else if (option == 2)
    {
        Console.WriteLine("Regulier abonnementen die nog niet betaald zijn:\n");
        foreach (var item in abonnementen)
        {
            if (item.Type == "Regulier" && item.IsBetaald == false)
            {
                Console.WriteLine("Abonnement nummer: " + item.Nummer + "\n");
            }
        }
        Console.WriteLine("\nEnter om door te gaan...");
        Console.ReadLine();
    }
    else if (option == 3)
    {
        Console.WriteLine("Abbo XL abonnementen van medewerkers die nog niet zijn betaald:\n");
        foreach (var item in abonnementen)
        {
            if (item.Type == "Abbo XL" && item.IsMedewerker == true && item.IsBetaald == false)
            {
                Console.WriteLine("Abonnement nummer: " + item.Nummer + "\n");
            }
        }
        Console.WriteLine("\nEnter om door te gaan...");
        Console.ReadLine();
    }
    else if (option == 4)
    {
        Console.WriteLine("Met hoeveel procent moet de prijs omhoog?: ");
        string increasePriceConsole = Console.ReadLine();
        int increasePrice = int.Parse(increasePriceConsole);

        foreach (var item in abonnementen)
        {
            if (item.AantalDagenOud > 360)
            {
                item.Prijs = item.Prijs + (item.Prijs * increasePrice / 100);
                Console.WriteLine("Oude prijs voor nummer " + item.Nummer + ": " + item.Prijs +
                                  "\nNieuwe prijs voor nummer " + item.Nummer + ": " + item.Prijs + "\n");
            }
        }
        Console.WriteLine("\nEnter om door te gaan...");
        Console.ReadLine();
    }
    else if (option == 5)
    {
        Console.WriteLine("Met hoeveel procent moet de prijs omlaag?: ");
        string decreasePriceConsole = Console.ReadLine();
        int decreasePrice = int.Parse(decreasePriceConsole);

        foreach (var item in abonnementen)
        {
            if ((item.Leeftijd > 65) || (item.IsMedewerker = true))
            {
                item.Prijs = item.Prijs + (item.Prijs * decreasePrice / 100);
            }
        }
    }
}
