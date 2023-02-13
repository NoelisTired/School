using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.ApplicationModel.Activation;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace H4_HuisBerekenen
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }

        private void calcButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                int width = int.Parse(WidthBox.Text);
                int length = int.Parse(LengthBox.Text);
                int height = int.Parse(HeightBox.Text);
                int floors = int.Parse(FloorsBox.Text);

                int surfacePerFloor = (width * length) / floors;
                int surfaceTotal = width * length;
                int cubic = width * length * height;

                surfaceEl.Text = surfacePerFloor.ToString();
                totSurfaceEl.Text = surfaceTotal.ToString();
                cubicEl.Text = cubic.ToString();
                warningEl.Text = "";
            }
            catch
            {
                warningEl.Text = "Vul alle gegevens in.";
            };
        }
    }
}
