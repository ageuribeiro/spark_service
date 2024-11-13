using System;
using System.Windows;
using System.Windows.Controls;

namespace Spark_Service_Desktop.Views
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            MainFrame.Navigate(new Uri("Views/DashboardPage.xaml", UriKind.Relative));
        }

        private void NavigateToDashboard(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/DashboardPage.xaml", UriKind.Relative));
        }

        private void NavigateToRegisterUser(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/RegisterUserPage.xaml", UriKind.Relative));
        }

    }
}
