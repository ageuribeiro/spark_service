using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spark_Service_Desktop.Models
{
    public class User
    {
        public int Id { get; set; }
        public string ? Username { get; set; }
        public string ? Password { get; set; }
        public string ? Email { get; set; }
        public string Role { get; set; } // "Owner", "Trainer", "User" 
        public DateTime DateJoined { get; set; }
    }
}
