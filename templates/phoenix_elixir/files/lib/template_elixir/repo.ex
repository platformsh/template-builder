defmodule TemplateElixir.Repo do
  use Ecto.Repo,
    otp_app: :template_elixir,
    adapter: Ecto.Adapters.Postgres
	
    @doc """
    Dynamically loads the repository configuration from the environment variables.
    """
    def init(_) do
      url = System.get_env("DATABASE_URL")
      {:ok, Ecto.Repo.Supervisor.parse_url(url)}
    end
end
