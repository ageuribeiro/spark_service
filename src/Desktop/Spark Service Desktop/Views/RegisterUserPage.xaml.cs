using System.Windows;
using System.Windows.Controls;
using Spark_Service_Desktop.Controllers;
using Spark_Service_Desktop.Models;

namespace Spark_Service_Desktop.Views
{
    public partial class RegisterUserPage : Page
    {
        private readonly UserController _userController;
        public RegisterUserPage()
        {
            InitializeComponent();
            _userController = new UserController();
        }

        private void RegisterButton_Click(object sender, RoutedEventArgs e)
        {
            var user = new User
            {
                Username = usernameBox.Text,
                Password = passwordBox.Password,
                Email = emailBox.Text,
                Role = ((ComboBoxItem)roleComboBox.SelectedItem).Content.ToString(),
                DateJoined = DateTime.Now
            };

            var createdBy = "currentUssername";
            if(_userController.RegisterUser(user, createdBy))
            {
                MessageBox.Show("Usuário registrado com sucesso!", "Register User", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else 
            {
                MessageBox.Show("Você não tem permissão para registrar um novo usuário.", "Register Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }
    }
}
