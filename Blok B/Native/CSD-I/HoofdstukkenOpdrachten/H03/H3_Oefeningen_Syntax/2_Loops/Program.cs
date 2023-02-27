// Verander deze variabelen en waardes niet!
int candyCount = 10;
var grades = new List<int>();
grades.Add(10);
grades.Add(8);
grades.Add(5);
grades.Add(8);
grades.Add(4);
grades.Add(7);
grades.Add(9);
grades.Add(3);
grades.Add(6);
// Verander bovenstaande code helemaal niet!


////////////////////////////////////////////////////
//
// Hieronder beginnen de oefeningen !
//
////////////////////////////////////////////////////
Console.Write("Oefening 1: ");
// Haal hieronder "true" weg en herhaal zolang:
// - `candyCount` (int) hoger is dan 0
// Pas de voorwaarde van de loop aan:
while (candyCount > 0) // <- Pas alleen deze regel aan - DONE
{
    candyCount--;

    if(candyCount < 0)
    {
        Console.WriteLine("Niet Voldaan");
        break;
    }
}

if(candyCount == 0)
{
    Console.WriteLine("Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 2: ");
// Haal hieronder "true" weg en herhaal zolang:
// - `candyCount` (int) lager is dan 15
// Pas de voorwaarde van de loop aan:
while (candyCount < 15) // <- Pas alleen deze regel aan - Done
{
    candyCount++;

    if (candyCount > 15)
    {
        Console.WriteLine("Niet Voldaan");
        break;
    }
}

if (candyCount == 15)
{
    Console.WriteLine("Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 3: ");
// We willen het totaal weten van alle cijfers in de lijst `grades` (List van int's)
// Voeg hieronder code toe om alle cijfers bij elkaar op te tellen.
//
// Tip: Gebruik foreach om door de `grades` te herhalen
int gradesSum = 0;

// <-- Maak hier een foreach loop
foreach (int grade in grades) 
{ 
    gradesSum += grade;
}

if (gradesSum == 60)
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 4: ");
// We willen het gemiddelde weten van de cijfers in de lijst `grades` (List van int's)
// Voeg hieronder code toe om het gemiddelde uit te rekenen.
//
// Tips:
// - Gebruik dezelfde logica om het gemiddelde uit te rekenen als je in Python gewend bent
// - Met deze code krijg je het aantal items in de lijst `grades`:  grades.Count
int sum = 0;

// <-- Maak hier een foreach loop
foreach (int grade in grades)
{
    sum += grade;
}

int average = sum / grades.Count(); // <-- Pas deze regel aan 

if (average == 6)
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}