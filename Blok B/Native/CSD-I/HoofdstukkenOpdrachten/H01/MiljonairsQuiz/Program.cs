while (true)
{
    Console.WriteLine("Welkom bij de MiljonairsQuiz!");
    Console.WriteLine("");

    Console.WriteLine("Vraag 1.");
    Console.WriteLine("Wat is C#\n" +
        "a. Spaans bedrijf.\n" +
        "b. Programmeertaal.\n" +
        "c. Computer.\n" +
        "d. Website op het internet.");
    Console.WriteLine();
    Console.WriteLine("Jouw antwoord: ");
    string answer = Console.ReadLine();

    if (answer.ToLower() != "b")
    {
        Console.WriteLine("Dat is helaas niet het goede antwoord.\nWilt u afsluiten? y/n");
        string exit = Console.ReadLine();
        if (exit.ToLower() == "y")
        {
            Environment.Exit(0);
        }
        continue;
    }

    Console.WriteLine("Vraag 2.");
    Console.WriteLine("Hoe vergelijk je in een programmeertaal?\na. Loop\nb. Functie\nc. If-statement\nd. Methode\n\nJouw Antwoord:");
    string answer2 = Console.ReadLine();

    if (answer2.ToLower() != "c")
    {
        Console.WriteLine("Dat is helaas niet het goede antwoord.\nWilt u afsluiten? y/n");
        string exit = Console.ReadLine();
        if (exit.ToLower() == "y")
        {
            Environment.Exit(0);
        }
        continue;
    }

    Console.WriteLine("Vraag 3.");
    Console.WriteLine("Hoe herhaal je in een programmeertaal?\na.Loop\nb.Functie\nc.Herhaal\nd.Return\n\nJouw Antwoord:");
    string answer3 = Console.ReadLine();

    if (answer3.ToLower() != "a")
    {
        Console.WriteLine("Dat is helaas niet het goede antwoord.\nWilt u afsluiten? y/n");
        string exit = Console.ReadLine();
        if (exit.ToLower() == "y")
        {
            Environment.Exit(0);
        }
        continue;
    }

    Console.WriteLine("Vraag 4");
    Console.WriteLine("Wie was een hoofdarchitect bij de ontwikkeling van C#\na. Bill gates\nb.Tim Lutt\nc. Anders Hejlsberg\nd.Steve Jobs\n\nJouw Antwoord:");
    string answer4 = Console.ReadLine();

    if (answer4.ToLower() != "c")
    {
        Console.WriteLine("Dat is helaas niet het goede antwoord.\nWilt u afsluiten? y/n");
        string exit = Console.ReadLine();
        if (exit.ToLower() == "y")
        {
            Environment.Exit(0);
        }
        continue;
    }

    Console.WriteLine("Vraag 5");
    Console.WriteLine("Wat kun je niet met C# maken?\na. Mobiele apps\nb.Desktopapplicaties\nc.Webapplicaties\nd.Frietje met mayo om op te eten\n\nJouw antwoord:");
    string answer5 = Console.ReadLine();

    if (answer5.ToLower() != "d")
    {
        Console.WriteLine("Dat is helaas niet het goede antwoord.\nWilt u afsluiten? y/n");
        string exit = Console.ReadLine();
        if (exit.ToLower() == "y")
        {
            Environment.Exit(0);
        }
        continue;
    }

    Console.WriteLine("Goed gedaan! Je hebt alle vragen goed beantwoord :)\nWilt u afsluiten? y/n");
    string exitFinal = Console.ReadLine();
    if (exitFinal.ToLower() == "y")
    {
        Environment.Exit(0);
    }
}