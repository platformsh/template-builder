# ASP.NET Core for Platform.sh

This template builds the ASP.NET Core framework for Platform.sh. It includes a minimalist application skeleton for demonstration, but you are free to alter it as needed.

ASP.NET Core is an open-source and cross-platform .NET framework for building modern cloud-based web applications.

## Services

* .NET 2.2
* MariaDB 10.4
* Redis 5.0

## Customizations

This repository was created from an ASP.NET Core MVC template and most of it still resembles that. The following files and additions make the framework work on Platform.sh. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh. You may customize them as you see fit.
* The `Program.cs` file has been modified to look for Platform-specific environment variables on startup, and listen on the correct TCP port.
* The `Startup.cs` file has been modified to include a `DbContext` and a `DistributedRedisCache` to handle the configured services. The typical `app.UseHttpsRedirection();` line has been removed as it is handled in `.platform/routes.yaml`.
* A class at `PlatformConfig/PlatformRelationship.cs` has been added to retrieve connection strings and handle service credentials for MariaDB and Redis.


## References

* [ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-2.2)
* [.NET Core on Platform.sh](https://docs.platform.sh/languages/dotnet.html)
