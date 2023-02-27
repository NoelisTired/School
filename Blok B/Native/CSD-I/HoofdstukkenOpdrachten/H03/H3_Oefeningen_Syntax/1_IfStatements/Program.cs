using _1_IfStatements;

// Verander deze variabelen niet!
int ageBob = 17;
int ageSally = 23;

string personGraduated = "Sally";
string personExempt = "Bob";

string playerJoining = "[NL] GamerYeah!";
string playerBanned = "xLeetGamert076x";

bool hasAnyoneGraduated = true;
int averageScore = 65;

var john = new Person
{
    Name = "John Ice",
    Age = 22,
    DrivingYears = 4,
    Nationality = "NL"
};
// Verander bovenstaande code helemaal niet!


////////////////////////////////////////////////////
//
// Hieronder beginnen de oefeningen !
//
////////////////////////////////////////////////////
Console.Write("Oefening 1: ");
// De if-statement hieronder klopt niet. We willen controleren of:
// - `ageBob` (int) lager is dan 18
// Pas de if-statement aan
if (ageBob < 18) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 2: ");
// Haal hieronder "false" weg en controleer of:
// - `ageSally` (int) hoger is of gelijk aan 18
if (ageSally >= 18) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 3: ");
// Haal hieronder "false" weg en controleer of:
// - `ageBob` (int) lager is dan 18
// En ook of:
// - `ageSally` (int) hoger is of gelijk aan 18
if (ageBob < 18 && ageSally >=18) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 4: ");
// Haal hieronder "false" weg en controleer of:
// - `personGraduated` (string) gelijk is aan "Bob"
// Of dat:
// - `personExempt` (string) gelijk is aan "Bob"
if (personGraduated == "Bob" || personExempt == "Bob") // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 5: ");
// Haal hieronder "false" weg en controleer of:
// - `hasAnyoneGraduated` (bool) waar is
// En ook dat:
// - `averageScore` (int) hoger is dan 60
if (hasAnyoneGraduated && averageScore > 60) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
//
// In de onderstaande oefeningen krijg je een verhaaltje.
// Je moet zelf bedenken hoe de if-statement gaat werken.
//
////////////////////////////////////////////////////
Console.Write("Oefening 6: ");
// Haal hieronder "false" weg en los dit op:
// Op een online spelletje wordt via naam gecontroleerd of iemand niet verbannen is
// voordat deze wordt toegelaten op het spel. 
// Er komt een nieuwe speler binnen, controleer of de speler het spel in mag
// 
// Extra informatie:
// - de naam van de speler staat in `playerJoining` (string)
// - de naam van de verbannen speler staat in `playerBanned` (string)
if (playerJoining != playerBanned) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 7: ");
// Haal hieronder "false" weg en los dit op:
// Bij DevRental in de Verenigde Staten (USA) moet je minimaal 21 jaar oud zijn om
// een auto te huren.
//
// Kijk of `john` (Person) oud genoeg is.
//
// Extra informatie:
// - `john` is een variabele met als datatype: Person (zie Person.cs)
// - controleer de `Age` (int) van `john` (Person)
if (john.Age >= 21) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 8: ");
// Haal hieronder "false" weg en los dit op:
// Bij CrazyRental in de Verenigde Staten (USA) moet je minimaal 18 zijn en
// altijd ten minste 4 jaar rijervaring hebben om een auto te mogen huren.
//
// Kijk of `john` (Person) oud genoeg is en genoeg rijervaring heeft.
//
// Extra informatie:
// - `john` is een variabele met als datatype: Person (zie Person.cs)
// - controleer de `Age` (int) van `john` (Person)
// - controleer ook de `DrivingYears` (int) van `john`
if (john.Age >= 18 && john.DrivingYears >= 4) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}


////////////////////////////////////////////////////
Console.Write("Oefening 9: ");
// Haal hieronder "false" weg en los dit op:
// Bij CompetingRental in de Verenigde Staten (USA) moet je om een auto te huren:
// - minimaal 25 jaar oud zijn
// OF:
// - minimaal 21 jaar oud, maar ook:
// - 4 of meer jaar rijervaring hebben
//
// Kijk of `john` (Person) oud genoeg of genoeg rijervaring heeft.
//
// Extra informatie:
// - `john` is een variabele met als datatype: Person (zie Person.cs)
// - controleer de `Age` (int) van `john` (Person)
// - controleer ook de `DrivingYears` (int) van `john`
if (john.Age >= 25 || (john.Age >= 21 && john.DrivingYears >= 4)) // <- Pas alleen deze regel aan - DONE
{
    Console.WriteLine("Voldaan");
}
else
{
    Console.WriteLine("Niet Voldaan");
}