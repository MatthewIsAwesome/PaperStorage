using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Main
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void AdvancedEnable_Checked(object sender, RoutedEventArgs e)
        {
            this.WidthBox.IsEnabled = this.HeightBox.IsEnabled = true;
        }

        private void AdvancedEnable_Unchecked(object sender, RoutedEventArgs e)
        {
            this.WidthBox.IsEnabled = this.HeightBox.IsEnabled = false;
            this.WidthBox.Text = this.HeightBox.Text = "1000";
        }

        private void Reset_Click(object sender, RoutedEventArgs e)
        {
            this.InputBox.Text = this.OutputBox.Text =  "";
            this.WidthBox.Text = this.HeightBox.Text = "1000";
        }
    }
}
