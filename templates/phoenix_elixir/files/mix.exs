defmodule TemplateElixir.MixProject do
  use Mix.Project

  def project do
    [
      app: :template_elixir,
      version: "0.1.0",
      elixir: "~> 1.5",
      elixirc_paths: elixirc_paths(Mix.env()),
      compilers: [:platformsh_conf, :phoenix, :gettext ] ++ Mix.compilers(),
      default_task: "platformsh.config",
      platformsh_config: [:ecto, :environment], 
      build_embedded:  true,
      start_permanent: true,
      aliases: aliases(),
      deps: deps(),
    ]
  end

  def start(_type, _args) do
    IO.puts "starting"
    Task.start(fn -> :timer.sleep(1000); IO.puts("done sleeping") end)
  end
  

  # Configuration for the OTP application.
  #
  # Type `mix help compile.app` for more information.
  def application do
    [
      mod: {TemplateElixir.Application, []},
      extra_applications: [:logger, :runtime_tools]
    ]
  end

  # Specifies which paths to compile per environment.
  defp elixirc_paths(:test), do: ["lib", "test/support"]
  defp elixirc_paths(_), do: ["lib"]

  # Specifies your project dependencies.
  #
  # Type `mix help deps` for examples and options.
  defp deps do
    [
	  {:platformshconfig, "~> 0.1.2"},
      {:phoenix, "~> 1.4.9"},
      {:phoenix_pubsub, "~> 1.1"},
      {:phoenix_ecto, "~> 4.0"},
      {:ecto_sql, "~> 3.1"},
      {:postgrex, ">= 0.0.0"},
      {:phoenix_html, "~> 2.11"},
      {:phoenix_live_reload, "~> 1.2", only: :dev},
      {:gettext, "~> 0.11"},
      {:jason, "~> 1.0"},
      {:plug_cowboy, "~> 2.0"},
	  
    ]
  end

  # Aliases are shortcuts or tasks specific to the current project.
  # For example, to create, migrate and run the seeds file at once:
  #
  #     $ mix ecto.setup
  #
  # See the documentation for `Mix` for more info on aliases.
  defp aliases do
    [
      "ecto.setup": ["platformsh.config", "ecto.create --no-compile --quiet", "ecto.migrate --no-compile", "run priv/repo/seeds.exs"],
      "ecto.reset": ["ecto.drop --no-compile", "ecto.setup"],
      test: ["ecto.create --quiet", "ecto.migrate", "test"]
    ]
  end
end
