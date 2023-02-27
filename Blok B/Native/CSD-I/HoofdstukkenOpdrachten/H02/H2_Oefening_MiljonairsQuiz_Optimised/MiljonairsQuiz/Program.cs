Console.WriteLine("Welkom bij de Miljonairs Quiz!");
Console.WriteLine("");

var questions = new List<QuizQuestion>();

var question1 = new QuizQuestion();
question1.Text = "Wat is C#?";
question1.Answers =
    "a. Spaans bedrijf\n" +
    "b. Programmeertaal\n" +
    "c. Computer\n" +
    "d. Website op het internet";
question1.CorrectAnswer = "b";
questions.Add(question1);

// TODO: Hier de overige vragen toevoegen op dezelfde manier zoals is voorgedaan bij quizvraag 1
var question2 = new QuizQuestion();
question2.Text = "Wat is nos.nl";
question2.Answers =
    "a. Spaans bedrijf\n" +
    "b. Programmeertaal\n" +
    "c. Computer\n" +
    "d. Website op het internet";
question2.CorrectAnswer = "d";
questions.Add(question2);

int i = 0;
foreach (var question in questions)
{
    Console.WriteLine("Vraag " + (i + 1));

    // TODO: Hier de vraagtekst laten zien

    Console.WriteLine();
    Console.WriteLine(question.Answers);

    Console.WriteLine();
    Console.Write("Your answer: ");
    string answer = Console.ReadLine();

    // TODO: Hier de code die controleert of het antwoord (answer) onjuist is en de quiz sluit
    //if ()
    //{
    //    Console.WriteLine("Dat is helaas niet het goede antwoord!");
    //    Console.WriteLine();
    //    Console.WriteLine("De Quiz sluit nu af...");
    //
    //    // TODO: Applicatie hier afsluiten
    //}

    i += 1;
}

Console.WriteLine("Goed gedaan! Je hebt alle vragen goed beantwoord :)");
