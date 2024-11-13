using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spark_Service_Desktop.Models
{
    public class Gym
    {
        public int Id { get; set; }
        public string ? Name { get; set; }
        public string ? Location { get; set; }
        public List<User> ? Owners { get; set; }
        public List<User> ? Trainers { get; set; }
        public List<User> ? Members { get; set; }
    }
}
