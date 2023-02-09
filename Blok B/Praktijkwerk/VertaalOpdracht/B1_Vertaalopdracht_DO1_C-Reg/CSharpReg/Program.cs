using System;

namespace CSharpReg
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("========== C#Reg ===========");
            Console.WriteLine("Welkom bij C#Reg, het Python KassaSysteem voor en door DeveloperLand!");
            Console.WriteLine("Tel de kassa, en geef op hoeveel er nu in zit.");
            Console.WriteLine("Bedrag in kassa?");
            decimal bedragInKassaBegin = decimal.Parse(Console.ReadLine());

            string keuze = "";
            decimal dagTotaal = 0;
            int aantalBonnen = 0;
            decimal dagTotaalTerug = 0;

            while (keuze != "9")
            {
                Console.Clear();
                Console.WriteLine("======== HOOFDMENU =========");
                Console.WriteLine("1. Nieuwe bon");
                Console.WriteLine("2. Retour");
                Console.WriteLine("3. Toon kassatotaal");
                Console.WriteLine("9. Afsluiten");
                Console.WriteLine("============================");

                Console.WriteLine("Maak uw keuze en druk op <ENTER>.");

                keuze = Console.ReadLine();

                if (keuze == "1")
                {
                    string bestelKeuze = "";
                    decimal bonTotaal = 0;
                    string bonString = "";
                    while (bestelKeuze != "9")
                    {
                        Console.WriteLine("========= BON MENU =========");
                        Console.WriteLine("Bon " + aantalBonnen.ToString());
                        Console.WriteLine("1. Volwassene                     € 19,-");
                        Console.WriteLine("2. Kinderen tot 12jr              € 9,-");
                        Console.WriteLine("3. Familiepas (2x volw. 3x kind)  € 49");
                        Console.WriteLine("4. DeveloperLand-kaart            € 4,50");
                        Console.WriteLine("5. Kinderwagen/bolderkar (1 dag)  € 6");
                        Console.WriteLine("6. Parkeerdagkaart                € 9");
                        Console.WriteLine("9. Afronden bon");
                        Console.WriteLine("Z. Bon annuleren");
                        Console.WriteLine("============================");
                        Console.WriteLine("Maak uw keuze en druk op <ENTER>.");
                        bestelKeuze = Console.ReadLine();

                        if (bestelKeuze == "1")
                        {
                            bonTotaal = bonTotaal + 19;
                            bonString = bonString + "1x Volwassene                  € 19\r\n";
                        }
                        else if (bestelKeuze == "2")
                        {
                            bonTotaal = bonTotaal + 9;
                            bonString = bonString + "1x kind (tot 12jr)             € 9\r\n";
                        }
                        else if (bestelKeuze == "3")
                        {
                            bonTotaal = bonTotaal + 49;
                            bonString = bonString + "1x Familiepas                  € 49\r\n";
                        }
                        else if (bestelKeuze == "4")
                        {
                            bonTotaal = bonTotaal + 4.50m;
                            bonString = bonString + "1x Parkkaart                   € 4,50\r\n";
                        }
                        else if (bestelKeuze == "5")
                        {
                            bonTotaal = bonTotaal + 6;
                            bonString = bonString + "1x kinderwagen/bolderkarhuur   € 6\r\n";
                        }
                        else if (bestelKeuze == "6")
                        {
                            bonTotaal = bonTotaal + 9;
                            bonString = bonString + "1x Parkeerdagkaart             € 9\r\n";
                        }
                        else if (bestelKeuze == "9")
                        {
                            aantalBonnen = aantalBonnen + 1;
                            dagTotaal = dagTotaal + bonTotaal;
                            Console.WriteLine(bonString);
                            Console.WriteLine("======== BON TOTAAL ========");
                            Console.WriteLine("Te betalen: " + bonTotaal.ToString());
                            Console.WriteLine("Betaald: ");
                            decimal betaald = decimal.Parse(Console.ReadLine());
                            decimal terug = bonTotaal - betaald;
                            Console.WriteLine("Terug:     " + terug.ToString());
                            Console.WriteLine("Druk op <ENTER> om door te gaan.");
                            Console.ReadLine();
                        }
                        else if (bestelKeuze == "Z" || bestelKeuze == "z")
                        {
                            bestelKeuze = "9";
                            bonTotaal = 0;
                            bonString = "";
                        }
                    }
                }
                else if (keuze == "2")
                {
                    Console.WriteLine("Uitvoeren terugbetaling");
                    
                    Console.WriteLine("Bedrag originele bon: ");
                    decimal terugTeGeven = decimal.Parse(Console.ReadLine());

                    Console.WriteLine("Reden retour: ");
                    string reden = Console.ReadLine();

                    dagTotaalTerug = dagTotaalTerug + terugTeGeven;
                }
                else if (keuze == "3")
                {
                    decimal inKassaPrint = bedragInKassaBegin + dagTotaal - dagTotaalTerug;
                    Console.WriteLine(
                        "======= DAG TOTALEN ========" +
                        "\nIn kassa begin:    " + bedragInKassaBegin +
                        "\nVerkocht:          " + dagTotaal +
                        "\nRetour:            " + dagTotaalTerug +
                        "\nIn Kassa:          " + inKassaPrint +
                        "\n\nDruk op <ENTER> om door te gaan."
                        );
                    Console.ReadLine();
                }
            }
            Console.WriteLine("Hoeveel zit er nu in de kassa?");
            decimal inKassa = decimal.Parse(Console.ReadLine());
            while (inKassa != (bedragInKassaBegin + dagTotaal - dagTotaalTerug))
            {
                Console.WriteLine("Je hebt een kassaverschil! Tel de kassa opnieuw");
                Console.WriteLine("Hoeveel zit er nu in de kassa?");
                inKassa = decimal.Parse(Console.ReadLine());
            }

            Console.Clear();
            Console.WriteLine("Kassa klopt, programma wordt afgesloten.");
            Console.WriteLine("======== DAGTOTALEN ========");
            Console.WriteLine("Aantal bonnen: " + aantalBonnen.ToString());
            Console.WriteLine("Verkocht:      " + dagTotaal.ToString());
            Console.WriteLine("Totaal retour: " + dagTotaalTerug.ToString());
            Console.WriteLine("In kassa:      " + inKassa.ToString());
            Console.WriteLine("============================");
        }
    }
}
