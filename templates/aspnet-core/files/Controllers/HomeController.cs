using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using PlatformshAspNetCore.Data;
using Microsoft.AspNetCore.Mvc;
using PlatformshAspNetCore.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.Extensions.Caching.Distributed;
using Microsoft.Extensions.Caching.Memory;
using Microsoft.Extensions.Caching.Redis;

namespace PlatformshAspNetCore.Controllers
{
    public class HomeController : Controller
    {
        private readonly MyDbContext _myDbContext;
        private readonly IDistributedCache _cache;

        public HomeController(MyDbContext myDbContext, IDistributedCache cache)
        {
            _myDbContext = myDbContext;
            _cache = cache;
        }

        public IActionResult Index()
        {
            // dummy DB operation
            _myDbContext.Database.ExecuteSqlCommand("SELECT 1");

            // dummy mem cache operation
            _cache.SetString("test", "1");

            ViewData["DbBackend"] = _myDbContext.Database.ProviderName;
            ViewData["CacheBackend"] = _cache.GetType().FullName;

            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel {RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier});
        }
    }
}
