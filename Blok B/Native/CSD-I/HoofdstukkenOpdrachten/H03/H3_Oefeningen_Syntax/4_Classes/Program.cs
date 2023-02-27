using _4_Classes;

// Oefening:
// De code hieronder werkt niet omdat de klasse `BankAccount` nog niet alle
// eigenschappen heeft.
//
// Ga naar BankAccount.cs en voeg deze eigenschappen toe:
// - Iban (string)
// - Balance (decimal)
// - Name

// Hieronder hoef je dus niks aan te passen
var account1 = new BankAccount
{
    Iban = "NL49 RABO 0 1234 1234 0000",
    Balance = 10.50M,
    Name = "T.W. Ramma"
};

var account2 = new BankAccount
{
    Iban = "NL49 RABO 0 0000 1234 1234",
    Balance = 1201.92M,
    Name = "A.R.A. Ting"
};

var account3 = new BankAccount
{
    Iban = "NL49 RABO 0 1234 0000 1234",
    Balance = 21123.24M,
    Name = "M. Zarumu"
};


Console.WriteLine("4_Classes oefening: Voldaan");