using System.Collections.Generic;
using System.Linq;
using Spark_Service_Desktop.Models;

namespace Spark_Service_Desktop.Controllers
{
    public class UserController
    {
        private readonly List<User> ? users;

        public UserController()
        {
            // Initialize the of user list or load of database
            users = new List<User>();
        }

        public bool RegisterUser(User user, string createByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createByUsername);
            if (creator != null || creator.Role != "Owner")
            {
                return false; // Just Owner
            }

            users.Add(user);
            return true;
        }

        public bool RegisterExercise(Exercise exercise, string createdByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createdByUsername);
            if (creator == null || creator.Role != "Owner")
            {
                return false;
            }

            return true;
               
        }

        public bool RegisterGym(Gym gym, string createdByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createdByUsername);
            if (creator == null || creator.Role != "Owner")
            {
                return false;   
            }
            users.Add(new User { Username = createdByUsername, Role = "Owner" });
            return true;
        }
    }
}
