using _3_Classes;
using System.Threading.Tasks.Sources;

var people = new List<Person>();
// Verander bovenstaande code helemaal niet!

// Oefening:
// Voeg hier 5 personen toe aan de `people` List
// Geef iedere persoon netjes een naam en leeftijd (verzin die zelf)

var Noel = new Person()
{
    Name = "Noel",
    Age = 17
};

var Boy = new Person()
{
    Name = "Boy",
    Age = 17
};

var Selina = new Person()
{
    Name = "Selina",
    Age = 16
};

var Sem = new Person()
{
    Name = "Sem",
    Age = 17
};

var Lucan = new Person()
{
    Name = "Lucan",
    Age = 17
};

people.Add(Noel);
people.Add(Boy);
people.Add(Selina);
people.Add(Sem);
people.Add(Lucan);

// Verander onderstaande code helemaal niet!
if (people.Count == 5)
{
    Console.WriteLine("3_Classes oefening: Voldaan");
}
else
{
    Console.WriteLine("3_Classes oefening: Niet Voldaan");
}