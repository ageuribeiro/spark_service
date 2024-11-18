using System.Collections.Generic;
using System.Linq;
using Spark_Service_Desktop.Models;

namespace Spark_Service_Desktop.Controllers
{
    public class UserController
    {
        private readonly List<Users> ? users;

        public UserController()
        {
            // Initialize the of user list or load of database
            users = new List<Users>();
        }

        public bool RegisterUser(Users user, string createByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createByUsername);
            if (creator != null || creator.UserRole != "Owner")
            {
                return false; // Just Owner
            }

            users.Add(user);
            return true;
        }

        public bool RegisterExercise(Exercise exercise, string createdByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createdByUsername);
            if (creator == null || creator.UserRole != "Owner")
            {
                return false;
            }

            return true;
               
        }

        public bool RegisterGym(Gym gym, string createdByUsername)
        {
            var creator = users.FirstOrDefault(u=> u.Username == createdByUsername);
            if (creator == null || creator.UserRole != "Owner")
            {
                return false;   
            }
            users.Add(new Users { Username = createdByUsername, UserRole = "Owner" });
            return true;
        }
    }
}
