using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.Storage.Pickers;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Media.Imaging;
using Windows.UI.Xaml.Navigation;

namespace H7_Weekcheck_AttractieScherm
{
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }

        private async void Button_Click(object sender, RoutedEventArgs e)
        {
            spAttractie.Visibility = Visibility.Collapsed;

            var picker = new FileOpenPicker();
            picker.SuggestedStartLocation = PickerLocationId.Downloads;
            picker.FileTypeFilter.Add(".attrinfo");

            var file = await picker.PickSingleFileAsync();

            if (file == null)
            {
                tbFileInfo.Text = "Geen geldig bestand gekozen! Kies een .attrinfo bestand.";
                return;
            }
            else
            {
                tbFileInfo.Text = file.Path;
            }

            using (var fileAcces = await file.OpenReadAsync())
            {
                using(var stream = fileAcces.AsStreamForRead())
                {
                    
                    using (var reader = new StreamReader(stream))
                    {
                        string imageUrl = reader.ReadLine();
                        attracName.Text = reader.ReadLine();
                        attracTheme.Text = reader.ReadLine();
                        attracInfo.Text = reader.ReadLine();
                        attracLength.Text = reader.ReadLine();
                        string fastPass = reader.ReadLine();
                        if (fastPass.ToLower() == "ja")
                        {
                            attracPass.Visibility = Visibility.Visible;
                        }
                        else
                        {
                            attracPass.Visibility = Visibility.Collapsed;
                        }

                        imgAttractie.Source = new BitmapImage(new Uri(imageUrl, UriKind.Absolute)); 
                        spAttractie.Visibility = Visibility.Visible;

                        

                    }
                }

            }

                



        }
    }
}
