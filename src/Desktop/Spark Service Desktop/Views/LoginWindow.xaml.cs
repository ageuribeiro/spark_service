using System.Diagnostics;
using System.Windows;
using System.Security.Cryptography;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Navigation;
using Spark_Service_Desktop.Controllers;
using Spark_Service_Desktop.Models;
using Microsoft.EntityFrameworkCore;


namespace Spark_Service_Desktop.Views
{
    public partial class LoginWindow : Window
    {
        private readonly AppDbContext _context;

        public LoginWindow()
        {
            InitializeComponent();
            _context = new AppDbContext();
        }

        private string GenerateRandomCode(int length)
        {
            using (var rng = RandomNumberGenerator.Create())
            {
                byte[] randomBytes = new byte[length];
                rng.GetBytes(randomBytes);
                return BitConverter.ToString(randomBytes).Replace("-","");
            }
        }
        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(passwordBox.Password))
            {
                ErrorMessage.Text = "Please, insert the code!";
                passwordBox.Focus();
            }
            else
            {
                ErrorMessage.Text = "";
                string userCode = passwordBox.Password;

                //Verifica se consta o usuário no banco de dados
                var user = _context.Users.FirstOrDefault(u => u.UserPass == passwordBox.Password);
                if (user != null)
                {
                    // Redireciona o usuario com base no seu perfil
                    if(user.UserRole == "Owner")
                    {
                        // Redirecionar para o perfil da academia
                        var academyWindow = new AcademyWindow();
                        academyWindow.Show();
                    }
                    else
                    {
                        //Redirecionar para o perfil de usuario
                        var userProfileWindow = new UserProfileWindow();
                        userProfileWindow.Show();
                    }
                    // Login bem-sucedido
                    var mainWindow = new MainWindow();
                    mainWindow.Show();
                    this.Close();
                }
                else
                {
                    ErrorMessage.Text = "Usuário ou senha inválidos.";
                    passwordBox.Focus();
                }
            }
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

        private void Hyperlink_RequestNavigate(object sender, RequestNavigateEventArgs e)
        {
            RegisterUserWindow registerUserWindow = new RegisterUserWindow();
            registerUserWindow.Show();
            //Process.Start(new ProcessStartInfo(e.Uri.AbsoluteUri) { UseShellExecute = true });
            //e.Handled = true;
        }
    }
}