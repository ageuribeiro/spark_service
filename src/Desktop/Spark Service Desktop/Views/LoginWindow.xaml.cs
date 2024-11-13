using System.Diagnostics;
using System.Windows;
using System.Windows.Input;
using System.Windows.Navigation;
using Spark_Service_Desktop.Controllers;



namespace Spark_Service_Desktop.Views
{
    public partial class LoginWindow : Window
    {
        private readonly LoginController _controller;

        public LoginWindow()
        {
            InitializeComponent();
            _controller = new LoginController();
            this.Loaded += LoginWindow_Loaded;

        }

        private void LoginWindow_Loaded(object sender, RoutedEventArgs e)
        {
            passwordBox.Focus();
        }

        private void LoginButton_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
            {
                LoginButton_Click(this, new RoutedEventArgs());
            }
        }

        private void LoginCode_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
            {
                LoginButton_Click(this, new RoutedEventArgs());
            }
        }

        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(passwordBox.Password))
            {
                ErrorMessage.Text = "Please, insert the code!";
            }
            else
            {
                ErrorMessage.Text = "";
                string password = passwordBox.Password;
                _controller.Login(password);
                this.Close();
            }

        }

        private void Hyperlink_RequestNavigate(object sender, RequestNavigateEventArgs e)
        {
            Process.Start(new ProcessStartInfo(e.Uri.AbsoluteUri) { UseShellExecute = true });
            e.Handled = true;
        }
    }
}