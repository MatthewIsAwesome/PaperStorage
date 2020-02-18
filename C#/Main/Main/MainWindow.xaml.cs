using System;
using System.IO;
using System.Windows;
using System.Windows.Forms;
using System.Drawing;
using System.Threading;

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

        private void File_Click(object sender, RoutedEventArgs e)
        {
            var myFolderBrowserDialog = new FolderBrowserDialog();
            Thread t = new Thread(() => myFolderBrowserDialog.ShowDialog());
            t.IsBackground = true;
            t.SetApartmentState(ApartmentState.STA);
            t.Start();
            t.Join();

            var path = myFolderBrowserDialog.SelectedPath;
            var send = ((Button)sender).Name;
        }
    }
}
