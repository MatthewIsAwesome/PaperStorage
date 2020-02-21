using System;
using System.IO;
using System.Windows;
using System.Windows.Forms;
using System.Diagnostics;
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

        private void InputButton_Click(object sender, RoutedEventArgs e)
        {
            var myFolderBrowserDialog = new FolderBrowserDialog();
            Thread t = new Thread(() => myFolderBrowserDialog.ShowDialog());
            t.IsBackground = true;
            t.SetApartmentState(ApartmentState.STA);
            t.Start();
            t.Join();

            var path = myFolderBrowserDialog.SelectedPath;
            this.InputBox.Text = path; 
        }

        private void OutputButton_Click(object sender, RoutedEventArgs e)
        {
            var myFolderBrowserDialog = new FolderBrowserDialog();
            Thread t = new Thread(() => myFolderBrowserDialog.ShowDialog());
            t.IsBackground = true;
            t.SetApartmentState(ApartmentState.STA);
            t.Start();
            t.Join();

            var path = myFolderBrowserDialog.SelectedPath;
            this.OutputBox.Text = path;
        }
        private void run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "./python/python.exe";
            start.Arguments = string.Format("{0} {1}", cmd, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                    this.Output.Text = result;

                }
            }
        }

        private void Start_Click(object sender, RoutedEventArgs e)
        {
            var height = this.HeightBox.Text;
            var width = this.WidthBox.Text;
            var input = this.InputBox.Text;
            var output = this.OutputBox.Text;
            var cmd = "./main.py";
            var args = "-path "+input+" -outpath "+output+" -width "+width+" -height "+height;
            run_cmd(cmd, args);
        }
    }
}
