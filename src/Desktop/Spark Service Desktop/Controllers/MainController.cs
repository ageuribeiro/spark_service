using Spark_Service_Desktop.Views;

namespace Spark_Service_Desktop.Controllers
{
    public class MainController
    {
        public void ShowLoginView()
        {
            var loginView = new LoginWindow();
            loginView.Show();
        }

        public void ShowDashboard()
        {
            var dashboardView = new MainWindow();
            dashboardView.Show();
        }
    }
}
