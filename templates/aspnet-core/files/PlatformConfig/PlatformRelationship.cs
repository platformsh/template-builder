using System;
using System.Buffers.Text;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Serialization;

namespace PlatformshAspNetCore.PlatformConfig
{
    // ReSharper disable once ClassNeverInstantiated.Global
    public class PlatformRelationship
    {
        public string Rel { get; set; }
        public string Service { get; set; }
        public string Scheme { get; set; }
        public string Type { get; set; }

        public string Ip { get; set; }
        public int Port { get; set; }

        public string Host { get; set; }
        public string Hostname { get; set; }
        public string Cluster { get; set; }

        public string Username { get; set; }
        public string Password { get; set; }
        public string Path { get; set; }

        public dynamic Query { get; set; }

        private PlatformRelationship() {}

        private static Dictionary<string, PlatformRelationship[]> _relationships;
        public static Dictionary<string, PlatformRelationship[]> Relationships
        {
            get
            {
                if (_relationships == null)
                {
                    var relationshipsStr = Environment.GetEnvironmentVariable("PLATFORM_RELATIONSHIPS");
                    if (relationshipsStr == null) {
                        _relationships = new Dictionary<string, PlatformRelationship[]>();
                    }
                    else
                    {
                        var jsonStr = Encoding.UTF8.GetString(Convert.FromBase64String(relationshipsStr));

                        var settings = new JsonSerializerSettings
                        {
                            ContractResolver = new CamelCasePropertyNamesContractResolver()
                        };
                        _relationships = JsonConvert.DeserializeObject<Dictionary<string, PlatformRelationship[]>>(jsonStr, settings);
                    }
                }

                return _relationships;
            }
        }

        public static bool Available => Relationships.Any();

        /// <summary>
        /// Parses PLATFORM_RELATIONSHIPS into a MySQL connection string.
        /// </summary>
        /// <param name="relationshipName">Name of relationship to be used, as defined in services.yaml. Optional if there is only 1 MySQL relationship defined.</param>
        /// <returns>A MySQL connection string.</returns>
        public static string GetMySqlConnString(string relationshipName = null)
        {
            var r = relationshipName != null
                ? Relationships[relationshipName].Single()
                : Relationships.Values.Single(x => x[0].Rel == "mysql").Single();

            return $"server={r.Host};uid={r.Username};pwd={r.Password};database={r.Path}";
        }

        /// <summary>
        /// Parses PLATFORM_RELATIONSHIPS into a Redis connection string.
        /// </summary>
        /// <param name="relationshipName">Name of relationship to be used, as defined in services.yaml. Optional if there is only 1 Redis relationship defined.</param>
        /// <returns>A Redis connection string.</returns>
        public static string GetRedisConnString(string relationshipName = null)
        {
            var r = relationshipName != null
                ? Relationships[relationshipName].Single()
                : Relationships.Values.Single(x => x[0].Rel == "redis").Single();

            return $"{r.Host}:{r.Port}";
        }
    }
}
