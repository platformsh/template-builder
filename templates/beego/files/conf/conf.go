package conf

import (
  psh "github.com/platformsh/config-reader-go/v2"
)

var Config = createConfigObj()

func createConfigObj() *psh.RuntimeConfig {
  // The Config Reader library provides Platform.sh environment information mapped to Go structs.
  config, err := psh.NewRuntimeConfig()
  if err != nil {
  	panic("Not in a Platform.sh Environment.")
  }
  return config
}
