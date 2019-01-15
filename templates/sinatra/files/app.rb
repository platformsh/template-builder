require 'rubygems'
require 'sinatra/base'
require 'haml'
require 'redis'
#require 'sunspot'
#require 'elasticsearch'
#require 'mongo'
#require 'bunny'
#require 'dalli'
#require 'influxdb'

require 'platform_sh'

class Main < Sinatra::Base
  configure do
    if PlatformSH::on_platform?
      PlatformSH::export_services_urls
    end
  end

  get '/' do
    begin
      @version ="This is running Ruby #{RUBY_VERSION}"
      redis = Redis.new
      redis.set("brilliant_key_name", "But, hello, world, of course!")
      @message = redis.get("brilliant_key_name")
    rescue Exception => e
      @message = e.message
    end
    haml :index
  end

end