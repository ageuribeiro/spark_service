using System.Windows;
using Spark_Service_Desktop.Models;
using Spark_Service_Desktop.Views;

namespace Spark_Service_Desktop.Controllers
{
    public class LoginController
    {
        private readonly Users userModel;

        public LoginController()
        {
            userModel = new Users();
        }

        public void ShowLoginView()
        {
            var loginView = new LoginWindow();
            loginView.DataContext = this;
            loginView.ShowDialog();
        }

        public void Login(string password)
        {

            // Checking if  data in input is empty or null
            if (string.IsNullOrWhiteSpace(password))
            {
                MessageBox.Show("Username or password a have empty", "Login Error", MessageBoxButton.OK, MessageBoxImage.Error);             
                return;
            }

            
            string expertedPassword = "password";

            if (password != expertedPassword)
            {
                MessageBox.Show("Username or password is incorrect.", "Login Error", MessageBoxButton.OK, MessageBoxImage.Error);
               
                return;

            }
            else
            {
                MessageBox.Show("Login bem-sucedido!", "Login Success", MessageBoxButton.OK, MessageBoxImage.Information);
                MainWindow winMain = new MainWindow();
                winMain.Show();
               
            }

        }      
    }
}
