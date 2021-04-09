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
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/crc.node" ],
          "destination": "./lib/"
        }
      ]
    }
  ]
}
