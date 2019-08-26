package conf

import (
  psh "github.com/platformsh/config-reader-go/v2"
)

var PshConfig = createPshConfigObj()

func createPshConfigObj() *psh.RuntimeConfig {
  // The Config Reader library provides Platform.sh environment information mapped to Go structs.
  config, err := psh.NewRuntimeConfig()
  if err != nil {
  	panic(err)
  }
  return config
}
