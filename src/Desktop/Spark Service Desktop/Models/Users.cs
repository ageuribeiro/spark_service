using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spark_Service_Desktop.Models
{
    public class Users
    {
        public int UserId { get; set; }
        public string ? Username { get; set; }
        public string ? UserPass { get; set; }
        public string ? UserEmail { get; set; }
        public string ? UserRole { get; set; } // "Owner", "Trainer", "User" 
        public DateTime DateJoined { get; set; }
    }
}
