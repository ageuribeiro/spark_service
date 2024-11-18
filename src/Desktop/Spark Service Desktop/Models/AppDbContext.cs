using System.IO;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.SqlServer;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;

namespace Spark_Service_Desktop.Models
{
    public class AppDbContext : DbContext
    {
        public DbSet<Users> Users { get; set; }
        public DbSet<Academy> Academies { get; set; }
        public DbSet<AccessLog> AccessLogs { get; set; }
        public DbSet<Exercise> Exercicies { get; set; }
        public DbSet<Person>Persons { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            var builder = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);

            var configuration = builder.Build();
            var connectionString = configuration.GetConnectionString("DefaultConnection");
            
            optionsBuilder.UseSqlServer(connectionString);
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Person>().ToTable("PERSON_TB").HasKey(p => p.PersonId);
            modelBuilder.Entity<Users>().ToTable("USER_TB").HasKey(u => u.UserId);
            modelBuilder.Entity<Academy>().ToTable("ACADEMY_TB").HasKey(a => a.AcademyId);
            modelBuilder.Entity<AccessLog>().ToTable("ACCESS_LOG_TB").HasKey(x => x.AccessLogId);
            modelBuilder.Entity<Exercise>().ToTable("EXERCISE_TB").HasKey(e => e.ExerciseId);


            base.OnModelCreating(modelBuilder);
        }
    }
}
