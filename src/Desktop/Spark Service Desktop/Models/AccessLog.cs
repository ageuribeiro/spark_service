using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spark_Service_Desktop.Models
{
    public class AccessLog
    {
        public int AccessLogId { get; set; }
        public int PersonId { get; set; }
        public int AcademyId { get; set; }
        public DateTime EntryTime { get; set; }
        public DateTime ExitTime { get; set; }
    }
}
