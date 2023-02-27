using System.Security.Cryptography.X509Certificates;

var attracties = new List<Attractie>();

attracties.Add(new Attractie
{
    Naam = "Debug Hero",
    Soort = "Achtbaan",
    BezoekersPerJaar = 11000,
    LaatsteOnderhoud = 320
});

attracties.Add(new Attractie
{
    Naam = "Bugs of Horror",
    Soort = "Achtbaan",
    BezoekersPerJaar = 9900,
    LaatsteOnderhoud = 430
});

attracties.Add(new Attractie
{
    Naam = "Fun Splash",
    Soort = "Water",
    BezoekersPerJaar = 20000,
    LaatsteOnderhoud = 100
});

attracties.Add(new Attractie
{
    Naam = "Turbo Turn 2000",
    Soort = "Water",
    BezoekersPerJaar = 8500,
    LaatsteOnderhoud = 260
});

attracties.Add(new Attractie
{
    Naam = "Magic Programmer",
    Soort = "Darkride",
    BezoekersPerJaar = 12500,
    LaatsteOnderhoud = 85
});

attracties.Add(new Attractie
{
    Naam = "Kids Park",
    Soort = "Anders",
    BezoekersPerJaar = 2100,
    LaatsteOnderhoud = 600
});

// Bonus Opdrachten
Console.WriteLine("Wil je zelf attracties toevoegen? (y/n): ");
string userAdd = Console.ReadLine();
if (userAdd.ToLower() == "y")
{
    while (true)
    {
        Console.Clear();

        Console.WriteLine("Naam attractie: ");
        string attractionName = Console.ReadLine();
        
        Console.WriteLine("\nSoort attractie: ");
        string attractionKind = Console.ReadLine();
        
        Console.WriteLine("\nAantal bezoers per jaar: ");
        string attractionGuestsRead = Console.ReadLine();
        int attractionGuests = int.Parse(attractionGuestsRead);
        
        Console.WriteLine("\nAantal dagen geleden van laatste onderhoud: ");
        string attractionMaintenanceRead = Console.ReadLine();
        int attractionMaintenance = int.Parse(attractionMaintenanceRead);

        Console.WriteLine("\nRating (../10): ");
        string attractionRatingReadConsole = Console.ReadLine();
        string attractionRatingRead = attractionRatingReadConsole.Replace('.', ','); 
        float attractionRating = float.Parse(attractionRatingRead);
        if (attractionRating !<= 10)
        {
            Console.WriteLine("Rating above 10. Error.");
            attractionRating = 0;
        }

        attracties.Add(new Attractie
        {
            Naam = attractionName,
            Soort = attractionKind,
            BezoekersPerJaar = attractionGuests,
            LaatsteOnderhoud = attractionMaintenance,
            Rating = attractionRating
        });

        Console.WriteLine("\nWil je nog een attractie toevoegen? (y/n): ");
        string userAddContinue = Console.ReadLine();
        if (userAddContinue.ToLower() != "y")
        {
            break;
        }
    }
}
// Einde Bonus Opdrachten

foreach (var item in attracties)
{
    if ((item.LaatsteOnderhoud > 300 && item.BezoekersPerJaar > 10000) || item.LaatsteOnderhoud > 500 || (item.Soort == "Water" && item.LaatsteOnderhoud > 200))
    {
        Console.Clear();
        Console.WriteLine(item.Naam + " (soort: " + item.Soort + ") moet onderhouden worden");
        Console.WriteLine(item.BezoekersPerJaar + " bezoekers per jaar");
        Console.WriteLine("Laatste onderhoud: " + item.LaatsteOnderhoud + " dagen geleden");
        if (item.Rating != 0)
        {
            Console.WriteLine("Rating: " + item.Rating + "/10");
        }
        else if (item.Rating == 0)
        {
            Console.WriteLine("Rating not found.");
        }
        Console.WriteLine("\nDruk op Enter voor volgende attractie");
        Console.ReadLine();
    }   
}