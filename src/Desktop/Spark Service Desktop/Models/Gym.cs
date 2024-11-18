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
        public List<Users> ? Owners { get; set; }
        public List<Users> ? Trainers { get; set; }
        public List<Users> ? Members { get; set; }
    }
}
