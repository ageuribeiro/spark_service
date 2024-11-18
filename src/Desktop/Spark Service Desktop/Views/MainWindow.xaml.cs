using System;
using System.Linq;
using System.Windows;
using System.Windows.Input;
using System.Windows.Controls;
using Microsoft.Extensions.Configuration;
using Spark_Service_Desktop.Models;

namespace Spark_Service_Desktop.Views
{
    public partial class MainWindow : Window
    {
        private readonly AppDbContext _context;

        public MainWindow()
        {
            InitializeComponent();
            _context = new AppDbContext();
            this.Loaded += MainWindow_Loaded;
            MainFrame.Navigate(new Uri("Views/DashboardPage.xaml", UriKind.Relative));
        }

        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            try
            {
                _context.Database.EnsureCreated();
                MainFrame.Navigate(new DashboardPage());
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao tentar conectar ao banco de dados: " + ex.Message);
                Application.Current.Shutdown();
            }
        }

        //NavigateToDashboard
        private void NavigateToDashboard(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/DashboardPage.xaml", UriKind.Relative));
        }

        //NavigateToUser
        private void NavigateToUser(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/UserPage.xaml", UriKind.Relative));
        }

        //NavigateToAcademy
        private void NavigateToAcademy(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/AcademyPage.xaml", UriKind.Relative));
        }

        //NavigateToExercises
        private void NavigateToExercises(object sender, RoutedEventArgs e)
        {
            MainFrame.Navigate(new Uri("Views/ExercisePage.xaml", UriKind.Relative));
        }
    }
}
