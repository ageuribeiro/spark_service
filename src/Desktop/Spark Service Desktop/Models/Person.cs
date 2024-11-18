using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spark_Service_Desktop.Models
{
    public class Person
    {
        public int PersonId { get; set; } // Chave Primaria
        public int AcademyId { get; set; }
        public string ? PersonFullName { get; set; }
        public int PersonAge { get; set; }
        public DateTime PersonBirthday { get; set; }
        public string ? PersonAddress { get; set; }
        public string ? PersonMail { get; set; }
        public string ? UserCode {  get; set; }
        public string? Role { get; set; }

    }
}
