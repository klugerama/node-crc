{
  "targets": [
    {
      "target_name": "crc",
      "sources": [ "./src/crc.c" ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "crc" ],
      "conditions": [ 
        [ 
          "OS=='linux'", {
            "copies": [
              {
                "files": [ "<(PRODUCT_DIR)/crc.node" ],
                "destination": "./lib/binding/linux/"
              }
            ]
          }
        ],
        [ 
          "OS=='win'", {
            "copies": [
              {
                "files": [ "<(PRODUCT_DIR)/crc.node" ],
                "destination": "./lib/binding/win32/"
              }
            ]
          }
        ],
      ]
    }
  ]
}
