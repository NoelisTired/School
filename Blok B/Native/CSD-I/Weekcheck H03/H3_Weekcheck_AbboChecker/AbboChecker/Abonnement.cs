using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbboChecker
{
    internal class Abonnement
    {
        public int Nummer { get; set; }
        public bool HeeftAutomatischVerlengen { get; set; }
        public int Leeftijd { get; set; }
        public bool IsMedewerker { get; set; }
        public string Type { get; set; } 
        public float Prijs { get; set; }
        public int AantalDagenOud { get; set; }
        public bool IsBetaald { get; set; }
        public string Bankrekening { get; set; }
    }
}
