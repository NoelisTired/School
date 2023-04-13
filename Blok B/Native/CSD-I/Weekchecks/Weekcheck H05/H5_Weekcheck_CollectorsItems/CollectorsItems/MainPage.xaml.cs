using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

namespace CollectorsItems
{
    public sealed partial class MainPage : Page
    {
        //TODO 2: Maak een klasse "CollectorsItem" met vier eigenschappen:
        //      - Name
        //      - Price
        //      - Type
        //      - IsSpecial

        List<CollectorsItem> itemList = new List<CollectorsItem>();

        public MainPage()
        {
            this.InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            //TODO 5a: Check of de invoer geldig is
            //      - Is de naam niet leeg ("")?
            //      - Bevat de prijs een geldig getal?
            //      - Is het type niet leeg (null)?

            string inputName = nameEl.Text;
            double inputPrice;
            string inputType = (string)typeEl.SelectedValue;
            bool inputCheck = false;


            bool priceCheck = double.TryParse(priceEl.Text, out inputPrice);

            if (checkEl.IsChecked == true)
            {
                inputCheck = true;
            }

            if ((inputName != "") && (priceCheck) && (inputType != null))
            {
                notificationEl.Text = "Item is toegevoegd👍";
            }
            else if (inputName == "")
            {
                notificationEl.Text = "Vul een geldige naam in!";
                return;
            }
            else if (!priceCheck)
            {
                notificationEl.Text = "Vul een geldig bedrag in!";
                return;
            }
            else if (inputType == null)
            {
                notificationEl.Text = "Vul een type aan!";
                return;
            }
            else
            {
                notificationEl.Text = $"ERROR\n {inputName}, {inputPrice}, {inputType}";
                return;
            }

            //TODO 5b: voeg het item toe aan de lijst "itemList", waarbij je alle vierde waarden meegeeft:
            itemList.Add(new CollectorsItem {
                Name = inputName,
                Price = inputPrice,
                Type = inputType,
                IsSpecial = inputCheck
            });


            //TODO 5c: maak de textboxes met lijsten leeg (pas hier zonodig de namen aan):
            normalItemsEl.Text = "";
            specialItemsEl.Text = "";

            //TODO 5d: loop door de lijst, kijk of het item speciaal is en voeg het toe (+=) aan de juiste TextBox

            foreach (var item in itemList)
            {
                if (item.IsSpecial)
                {
                    specialItemsEl.Text += $"{item.Type}: {item.Name} voor €{item.Price}\n";
                }
                else
                {
                    normalItemsEl.Text += $"{item.Type}: {item.Name} voor €{item.Price}\n";
                }
            }
        }
    }
}
