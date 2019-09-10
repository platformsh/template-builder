using Microsoft.EntityFrameworkCore;

namespace PlatformshAspNetCore.Data
{
    public class MyDbContext : DbContext
    {
        protected MyDbContext()
        {
        }

        public MyDbContext(DbContextOptions options) : base(options)
        {
        }
    }
}
