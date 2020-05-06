defmodule TemplateElixirWeb.PageController do
  use TemplateElixirWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
